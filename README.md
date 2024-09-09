
# PaymentGateWay_vue_django_stripe

This project is a modern payment gateway that integrates **Vue.js**, **Django**, and **Stripe** for seamless payment processing. It includes a front-end built in Vue.js and a back-end powered by Django, with Stripe handling the payment processing.

## Blog Documentation

For a detailed guide on how this project was built, refer to the blog post:  
[Building a Modern Payment Gateway with Django, Vue.js, and Stripe](https://nchilaka.hashnode.dev/building-a-modern-payment-gateway-with-django-vuejs-and-stripe)

## Tech Stack

- **Vue.js**: Front-end framework for building user interfaces.
- **Django**: Backend web framework for handling authentication, business logic, and Stripe integration.
- **Stripe**: Payment processing platform.

## Project Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-repo/PaymentGateWay_vue_django_stripe.git
cd PaymentGateWay_vue_django_stripe
```

### 2. Backend Setup (Django)

Navigate to the backend directory and follow these steps:

- **Create a virtual environment and activate it:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

- **Install the dependencies:**

```bash
pip install -r requirements.txt
```

- **Set up the environment variables by creating a `.env` file:**

```bash
STRIPE_SECRET_KEY=<your-stripe-secret-key>
STRIPE_PUBLISHABLE_KEY=<your-stripe-publishable-key>
```

- **Apply migrations:**

```bash
python manage.py migrate
```

- **Start the Django development server:**

```bash
python manage.py runserver
```

### 3. Frontend Setup (Vue.js)

Navigate to the frontend directory and follow these steps:

- **Install the dependencies:**

```bash
npm install
```

- **Start the Vue development server:**

```bash
npm run serve
```

### 4. Stripe Setup

Make sure you have a Stripe account and obtain your API keys. Set the `STRIPE_SECRET_KEY` and `STRIPE_PUBLISHABLE_KEY` in the `.env` file for both the frontend and backend.

## Running the Application

Once both the backend (Django) and frontend (Vue.js) are running, access the app at:

```bash
http://localhost:8080
```

### Features:

- **User Authentication**: Register, log in, and manage accounts.
- **Product Listings**: Display sample products for testing payments.
- **Payment Gateway**: Secure payment processing using Stripe.
- **Cost Calculation**: Automatically calculate product costs based on user selection.

### Key Commands:

- **Backend (Django):**

```bash
python manage.py runserver
```

- **Frontend (Vue.js):**

```bash
npm run serve
```
