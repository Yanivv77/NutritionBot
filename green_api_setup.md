# Green API Setup Guide for Nutrition Bot

This guide provides detailed steps for setting up Green API to connect your WhatsApp account with the nutrition bot.

## Step 1: Create a Green API Account

1. Visit [Green API's website](https://green-api.com/) and sign up for an account
2. Complete the registration process with your email

[IMAGE PLACEHOLDER: Screenshot of Green API signup page]

## Step 2: Create a New Instance

1. After logging in, go to the dashboard
2. Click on "Create Instance"
3. Give your instance a name (e.g., "Nutrition Bot")
4. Select "WhatsApp" as the messenger type
5. Choose the pricing plan that suits your needs (there's typically a free trial)
6. Click "Create"

[IMAGE PLACEHOLDER: Screenshot of creating new instance]

## Step 3: Connect Your WhatsApp Account

1. Once your instance is created, you'll be shown a QR code
2. Open WhatsApp on your mobile device
3. Go to Settings > Linked Devices
4. Tap on "Link a Device"
5. Scan the QR code shown on the Green API website
6. Wait for the connection to be established

[IMAGE PLACEHOLDER: Screenshot of QR code scanning]

## Step 4: Get Your Instance ID and API Token

1. After your WhatsApp is connected, go to your instance settings
2. Note your Instance ID (a numeric value)
3. Note your API Token (a long alphanumeric string)
4. You'll need these values for your `.env` file

[IMAGE PLACEHOLDER: Screenshot of Instance ID and API Token]

## Step 5: Configure Webhook Notifications

1. In your instance settings, navigate to the "Notifications" tab
2. Enter your webhook URL in the "Webhook URL for incoming notifications" field:
   ```
   https://your-ngrok-url.ngrok.io/webhook
   ```
3. Enable the following notifications:
   - Incoming messages
   - State instances (optional)
   - Outgoing messages (optional, for logging)
   - Outgoing API messages (optional, for logging)
4. Click "Save"

[IMAGE PLACEHOLDER: Screenshot of webhook configuration]

## Step 6: Test the Connection

1. Send a message to yourself or another WhatsApp number
2. Check your server logs to see if the webhook is receiving notifications
3. Try sending an image to test the full functionality

## Common Issues and Troubleshooting

### QR Code Expired
If the QR code expires before you can scan it, simply refresh the page or click "Reload QR code" to generate a new one.

### Connection Problems
- Make sure your phone has a stable internet connection
- Ensure you're not already connected to WhatsApp Web on too many devices
- Try logging out of other WhatsApp Web sessions

### Webhook Not Receiving Notifications
- Verify your ngrok URL is correct and running
- Check that your server is running and accessible
- Ensure the webhook URL is properly configured in Green API
- Check your server logs for any errors

## Security Best Practices

1. Never share your API Token publicly
2. Implement proper authentication in your webhook endpoint
3. Use HTTPS for all communications
4. Regularly check your API usage to detect any unauthorized access
5. Set up notifications for unusual activity

## API Rate Limits

Green API typically has rate limits on their service:
- Free tier: ~1,000 messages per day
- Paid tiers: Higher limits depending on your plan

Check the [Green API documentation](https://green-api.com/docs/) for the most up-to-date information on rate limits and pricing. 