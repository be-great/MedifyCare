# Run app using virtualenv
```bash
./init.sh
```

# Run app using Docker
## build the image
```bash
docker build -t auth .
```
## run it 
```bash
docker run -d -p 5000:5000 auth
```

## Payment Steps:-

```bash
Start
  |
  v
1. Get Publishable Key
  | 
  |-- Send AJAX Request to Flask Endpoint for Publishable Key
  |-- Flask Endpoint Responds with Publishable Key
  |-- Client-Side Creates Stripe.js Instance with Key
  |
  v
2. Create Checkout Session
  | 
  |-- Send AJAX Request to Flask Endpoint for Checkout Session ID
  |-- Flask Endpoint Generates Checkout Session and Sends ID
  |-- Client-Side Redirects to Checkout Page
  |
  v
3. Payment Outcome
  |
  |-- Redirect to Success Page or Cancellation Page
  |
  v
4. Confirm Payment with Webhooks
  |
  |-- Set Up Webhook Endpoint
  |-- Test Endpoint with Stripe CLI
  |-- Register Webhook with Stripe
  |
  v
End

Helping-URL: https://testdriven.io/blog/flask-stripe-tutorial/
Test-Card: 4242 4242 4242 4242

```