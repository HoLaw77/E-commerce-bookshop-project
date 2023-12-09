from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe Webhook"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle unexpected Event"""

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status = 200
        )

    def handle_payment_intent_success(self, event):
        intent = event.data.object
        print(intent)
        """Handle successful payment intent event webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status = 200
        )

    def handle_payment_intent_fail(self, event):
        """Handle fail payment intent event webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status = 200
        )