# Nutrition Bot 🤖

A WhatsApp bot that analyzes food images and provides detailed nutritional information using OpenAI's Vision API. Built with Flask, Twilio, and deployed on Railway.

## Features

- 📸 Analyze food images via WhatsApp
- 🔍 Detailed nutritional breakdown (calories, proteins, carbs, fats)
- 🤖 Automated responses using OpenAI's Vision API
- 🚀 Easy deployment with Railway
- 🔒 Secure environment variable management

## Prerequisites

- Python 3.10.12
- Twilio account
- OpenAI API key
- Railway account (for deployment)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nutrition-bot.git
cd nutrition-bot
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the root directory with the following variables:
```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key

# Your WhatsApp phone number for receiving nutrition analysis (include country code)
YOUR_PHONE_NUMBER=your_phone_number

# Twilio Credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=whatsapp:+14155238886
```

### 5. Local Testing
Run the test script to verify your setup:
```bash
python test_locally.py path/to/your/food/image.jpg
```

## Deployment on Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Add the following environment variables in Railway:
   - `OPENAI_API_KEY`
   - `YOUR_PHONE_NUMBER`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`

4. Deploy your application

## Twilio Setup

1. Create a Twilio account at [twilio.com](https://www.twilio.com)
2. Get your Account SID and Auth Token
3. Set up a WhatsApp sandbox:
   - Go to Twilio Console > Messaging > Try WhatsApp
   - Follow the instructions to connect your WhatsApp number
   - Note down the sandbox number provided by Twilio

## Usage

1. Send a food image to your WhatsApp bot
2. The bot will analyze the image and respond with:
   - Food identification
   - Portion size
   - Caloric content
   - Macronutrient breakdown (proteins, carbs, fats)

## Testing Endpoints

- Status Check: `GET /status`
- Test Message: `GET /test_message?to=PHONE_NUMBER&message=YOUR_MESSAGE`

## Security Notes

- Never commit your `.env` file
- Keep your API keys secure
- Use environment variables for sensitive information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or need help:
1. Check the error logs
2. Verify your environment variables
3. Ensure your Twilio sandbox is properly configured

## Contributing

Feel free to submit issues and enhancement requests! 