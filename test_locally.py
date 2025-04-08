import os
import requests
import base64
import json
import argparse
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# API key
API_KEY = os.environ.get('DEEPSEEK_API_KEY')  # We'll use this for OpenAI too

def analyze_image_with_ai(image_path):
    """
    Analyze food image using OpenAI's Vision API
    """
    try:
        # Check if API key is available
        if not API_KEY:
            return "Error: API key not found. Please add it to your .env file."
        
        # Read and encode the image
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
        # OpenAI API endpoint
        url = "https://api.openai.com/v1/chat/completions"
        
        # Prepare the request payload
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        payload = {
            "model": "gpt-4-vision-preview",
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
        print("Sending image to OpenAI API...")
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze food image for nutritional information')
    parser.add_argument('image_path', help='Path to the food image')
    args = parser.parse_args()
    
    # Check if the image exists
    if not os.path.exists(args.image_path):
        print(f"Error: Image file not found at {args.image_path}")
        exit(1)
    
    # Analyze the image
    print("Analyzing food image...")
    analysis = analyze_image_with_ai(args.image_path)
    print("\nNutritional Analysis:")
    print(analysis) 