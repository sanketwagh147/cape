import os

SEMIANNUAL_SUBSCRIPTION_ID = os.environ.get("SEMIANNUAL_SUBSCRIPTION_ID")
MONTHLY_SUBSCRIPTION_ID = os.environ.get("MONTHLY_SUBSCRIPTION_ID")
ANNUAL_SUBSCRIPTION_ID = os.environ.get("ANNUAL_SUBSCRIPTION_ID")

STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")