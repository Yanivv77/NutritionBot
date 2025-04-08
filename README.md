# WhatsApp Nutrition Bot

A WhatsApp bot that analyzes food images to provide nutritional information using Twilio and DeepSeek AI.

## Features

- Send food images to get nutritional analysis
- Analyzes macro nutrients (proteins, carbs, fats)
- Low-cost implementation using DeepSeek AI for advanced image analysis
- Direct WhatsApp integration using Twilio
- Easy setup and deployment

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your API keys:
   ```
   DEEPSEEK_API_KEY=your_deepseek_api_key
   YOUR_PHONE_NUMBER=your_phone_number_with_country_code
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
   ```

3. Run the server:
   ```
   python app.py
   ```

4. Set up a public URL using ngrok or similar:
   ```
   ngrok http 5000
   ```

5. Configure Twilio webhook (see SETUP_GUIDE.md) 