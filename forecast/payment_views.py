from django.shortcuts import render, redirect
from .models import Forecast
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import HttpResponse
from user.models import User
import typing
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def subscribe(request):
    return render(request, 'subscribe.html')


@csrf_exempt
def stripe_configuration(request):
    if request.method == "GET":
        stripe_config = {
            "publicKey": settings.STRIPE_PUBLISHABLE_KEY,
            "monthlySubscription": "",
            "subannualSubscription": "",
            "annualSubscription": ""
        }
        return JsonResponse(stripe_config, safe=False)
    else:
        return HttpResponse(
            status=405
        )
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET' and request.user.is_authenticated:
        domain_url = settings.FRONTEND_DOMAIN
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id,
                success_url=domain_url + 'forecast/',
                cancel_url=domain_url + 'forecast/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.SEMIANNUAL_SUBSCRIPTION_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return HttpResponse(
            status=405
        )


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        print("Here!")
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(e)
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        user.stripe_subscription_id = stripe_subscription_id
        user.stripe_customer_id = stripe_customer_id
        user.save()

    return HttpResponse(status=200)