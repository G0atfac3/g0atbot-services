# STRIPE SETUP ACTION

## What You Need To Do (Graham)

### Step 1: Create Stripe Account
1. Go to https://stripe.com
2. Sign up with email: g0atbotuk@gmail.com
3. Verify email

### Step 2: Get API Keys
1. Go to https://dashboard.stripe.com/apikeys
2. Copy "Publishable key" (starts with pk_test_...)
3. Copy "Secret key" (starts with sk_test_...)
4. Send me both keys

### Step 3: Create Payment Links
1. Go to https://dashboard.stripe.com/payment-links
2. Create links for:
   - Lead Gen Setup ($500): https://buy.stripe.com/xxx
   - Lead Gen Monthly ($200): https://buy.stripe.com/xxx
   - AI Setup Package ($497): https://buy.stripe.com/xxx
   - Content Setup ($300): https://buy.stripe.com/xxx

### Step 4: Set Up Webhook
1. Go to https://dashboard.stripe.com/webhooks
2. Add endpoint: `https://your-domain.com/webhook`
3. Events: `checkout.session.completed`
4. Copy webhook secret

### Send Me:
- Publishable key
- Secret key  
- Payment link URLs
- Webhook secret

I'll handle the rest!
