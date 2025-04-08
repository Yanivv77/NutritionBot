# WhatsApp Nutrition Bot Setup Guide

This guide will help you set up your WhatsApp nutrition bot using Twilio and DeepSeek AI.

## Prerequisites

- Python 3.8 or above
- Twilio account (free tier available)
- DeepSeek API key
- ngrok (free tier) or similar tunneling service

## Step 1: Set Up Your Environment

1. Clone this repository and navigate to the project folder
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Step 2: Set Up DeepSeek API

1. Sign up for a [DeepSeek account](https://platform.deepseek.com/)
2. Get your API key from the dashboard
3. DeepSeek offers competitive pricing for advanced vision model usage

## Step 3: Set Up Twilio for WhatsApp

1. Sign up for a [Twilio account](https://www.twilio.com/try-twilio)
2. Navigate to the Twilio Console
3. In the Twilio Console, go to "Messaging" > "Try it Out" > "Send a WhatsApp Message"
4. Follow the instructions to connect your WhatsApp number to the Twilio Sandbox
5. Note your Account SID and Auth Token from the Twilio Dashboard
6. Also note your Twilio WhatsApp number (usually starts with "whatsapp:+14155238886")

## Step 4: Configure the Application

1. Copy the `.env.example` file to a new file named `.env`:
   ```
   cp .env.example .env
   ```
2. Edit the `.env` file with your credentials:
   - Add your DeepSeek API key
   - Add your Twilio Account SID and Auth Token
   - Add your Twilio WhatsApp number
   - Add your personal WhatsApp number (without the "+" sign)

## Step 5: Run the Application Locally

1. Start your Flask application:
   ```
   python app.py
   ```
2. The server will run on `http://localhost:5000`

## Step 6: Expose Your Local Server

1. Download and install [ngrok](https://ngrok.com/download)
2. Run ngrok to create a tunnel to your local server:
   ```
   ngrok http 5000
   ```
3. Note the HTTPS URL provided by ngrok (e.g., `https://abc123.ngrok.io`)

## Step 7: Configure Twilio Webhook

1. Go to your Twilio Console
2. Navigate to "Phone Numbers" > "Manage" > "Active Numbers"
3. Select your WhatsApp Sandbox number
4. In the Messaging section, find "A MESSAGE COMES IN"
5. Set the webhook URL to your ngrok URL + `/webhook`:
   ```
   https://abc123.ngrok.io/webhook
   ```
6. Save your settings

## Step 8: Test Your Bot

1. Send a message to your Twilio WhatsApp Sandbox number
2. Send an image of food to get nutritional analysis
3. Type "help" to see instructions

## Cost-Saving Tips

1. DeepSeek API: 
   - Pay-as-you-go pricing model
   - Set up spending limits in your account

2. Twilio: 
   - Free tier includes a starting balance
   - Each WhatsApp message costs a small amount (check current pricing)

3. ngrok:
   - Free tier changes the URL each time you restart
   - For a fixed URL, the Pro plan starts at $10/month

4. Hosting alternatives:
   - Consider using Heroku (free tier) or PythonAnywhere (free tier) instead of running locally 