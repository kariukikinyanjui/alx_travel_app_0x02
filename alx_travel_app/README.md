# ALX Travel App (Payment Integration)

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14-blue)](https://www.django-rest-framework.org/)
[![Chapa](https://img.shields.io/badge/Payment-Chapa_API-orange)](https://developer.chapa.co/)

A travel listing platform with integrated payment processing using Chapa API. This version (0x02) adds secure payment workflows for bookings.

## Features

- **User Authentication**: JWT-based secure access
- **Travel Listings Management**: CRUD operations for properties
- **Booking System**: Date-based reservations with status tracking
- **Payment Processing**: Chapa API integration for secure transactions
- **Email Notifications**: Celery-powered async confirmation emails
- **API Documentation**: Swagger/OpenAPI support
- **Database**: MYSQL with Django ORM

1. **Clone Repository**
```
git clone https://github.com/<your-username>/alx_travel_app_0x02.git
cd alx_travel_app_0x02
```
2. **Set Up Virtual Environment**
```
python -m venv env
. env/bin/activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Database Setup**
```
CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

5. **Apply Migrations**
```
python manage.py migrate
```

6. **Run Development Server**
```
python manage.py runserver
```

# Payment Integration

## Configuration

1. Get Chapa API keys from [developer.chapa.co](https://developer.chapa.co)
2. Add to `.env`

```
CHAPA_SECRET_KEY=your_secret_key
CHAPA_WEBHOOK_URL=https://your-domain.com/chapa/webhook/
```
## API Endpoints
--------------------------------------|--------------|----------------------|
Endpoint                              |Method        |Description           |
--------------------------------------|--------------|----------------------|
`/api/payments/initiate/<booking_id>/`|   POST       | Start payment process|
--------------------------------------|--------------|----------------------|
`/api/payments/verify/<tx_ref>/`      |   GET        | Verify payment status|
--------------------------------------|--------------|----------------------|

## Payment Workflow

1. User creates booking
2. System initiates payment with Chapa
3. User redirected to Chapa payment page
4. Chapa sends payment confirmation via webhook
5. System updates booking status and sends confirmation email

## Testing Payment System
1. **User Sandbox Credentials**
```
CHAPA_SECRET_KEY=CHASECK_TEST-YourTestKey
```

2. **Test Card Details**
- Card Number: 4242 4242 4242 4242
- Expiry: Any future date
- CVV: 123

3. **Simulate Payment Flow**
```
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"listing": 1, "check_in_date": "2024-03-01", "check_out_date": "2024-03-05"}'
```
