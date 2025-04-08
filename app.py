import os
import requests
import base64
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import time
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# API keys
API_KEY = os.environ.get('OPENAI_API_KEY')  # For OpenAI Vision API

# Twilio credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Your WhatsApp number for receiving messages
YOUR_PHONE_NUMBER = os.environ.get('YOUR_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def analyze_image_with_ai(image_url):
    """
    Analyze food image using OpenAI's Vision API
    """
    try:
        # Download the image
        response = requests.get(image_url)
        if response.status_code != 200:
            return f"Error downloading image: {response.status_code}"
        
        # Convert the image to base64
        image_data = base64.b64encode(response.content).decode('utf-8')
        
        # OpenAI API endpoint
        url = "https://api.openai.com/v1/chat/completions"
        
        # Prepare the request payload
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please analyze this food image and provide detailed nutritional information. Focus on identifying the food and estimating its macro nutrients (proteins, carbs, fats) and calorie content. Format your response in a clear, structured way showing each nutrient value."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 800
        }
        
        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check if the request was successful
        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"
        
        # Parse the response
        data = response.json()
        analysis = data.get('choices', [{}])[0].get('message', {}).get('content', '')
        
        # Format the result
        result = f"""📊 Nutritional Analysis:

{analysis}

⚙️ Analyzed with AI Vision"""
        
        return result
    
    except Exception as e:
        return f"Error analyzing image: {str(e)}"

def send_whatsapp_message(to_number, message):
    """
    Send a WhatsApp message using Twilio
    """
    try:
        print(f"Sending message to: {to_number}")
        
        # Format the phone number for Twilio
        # Twilio requires the format 'whatsapp:+1234567890'
        if not to_number.startswith('whatsapp:'):
            # Make sure the number starts with a plus sign
            if not to_number.startswith('+'):
                to_number = '+' + to_number
            
            to_number = f"whatsapp:{to_number}"
        
        # Format the Twilio number too
        from_number = TWILIO_PHONE_NUMBER
        if not from_number.startswith('whatsapp:'):
            if not from_number.startswith('+'):
                from_number = '+' + from_number
            
            from_number = f"whatsapp:{from_number}"
        
        print(f"Formatted number: {to_number}")
        print(f"From number: {from_number}")
        
        # Send the message
        message = twilio_client.messages.create(
            from_=from_number,
            body=message,
            to=to_number
        )
        
        print(f"Message sent successfully with SID: {message.sid}")
        return {"success": True, "sid": message.sid}
    
    except Exception as e:
        print(f"Exception in send_whatsapp_message: {str(e)}")
        return {"success": False, "error": str(e)}

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint for Twilio WhatsApp messages
    """
    try:
        print("\n\n==== WEBHOOK RECEIVED ====")
        print("Headers:", request.headers)
        print("Form data:", request.form)
        
        # Extract message information from Twilio's request
        from_number = request.form.get('From', '')
        body = request.form.get('Body', '').lower()
        num_media = int(request.form.get('NumMedia', 0))
        
        print(f"From: {from_number}")
        print(f"Body: {body}")
        print(f"NumMedia: {num_media}")
        
        # Initialize the Twilio response
        resp = MessagingResponse()
        
        # Handle image messages
        if num_media > 0:
            media_url = request.form.get('MediaUrl0', '')
            content_type = request.form.get('MediaContentType0', '')
            
            print(f"Media URL: {media_url}")
            print(f"Content Type: {content_type}")
            
            if 'image' in content_type:
                print("Processing image...")
                analysis = analyze_image_with_ai(media_url)
                resp.message(analysis)
                print("Image analysis complete")
            else:
                resp.message("Please send an image of food for nutritional analysis.")
        
        # Handle text messages
        elif body:
            if 'help' in body:
                help_message = "📸 Send me a photo of your food, and I'll analyze its nutritional content!"
                resp.message(help_message)
            else:
                default_message = "Please send a food image for nutritional analysis. Type 'help' for instructions."
                resp.message(default_message)
        
        return str(resp)
    
    except Exception as e:
        print(f"Error in webhook: {str(e)}")
        resp = MessagingResponse()
        resp.message("Sorry, an error occurred. Please try again later.")
        return str(resp)

@app.route('/status', methods=['GET'])
def status():
    """
    Status endpoint to check if the server is running
    """
    return jsonify({"status": "online", "timestamp": time.time()})

@app.route('/test_message', methods=['GET'])
def test_message():
    """
    Test endpoint to directly send a WhatsApp message via Twilio
    """
    try:
        to_number = request.args.get('to', YOUR_PHONE_NUMBER)
        message = request.args.get('message', f"Test message from Nutrition Bot at {time.strftime('%H:%M:%S')}")
        
        result = send_whatsapp_message(to_number, message)
        
        if result.get("success"):
            return jsonify({"status": "success", "message": "Test message sent", "sid": result.get("sid")})
        else:
            return jsonify({"status": "error", "error": result.get("error")})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000) 