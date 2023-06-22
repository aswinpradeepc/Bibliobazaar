from django.shortcuts import render, redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from book_shop.models import Order, Cart

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


# checkout.html class view for handling checkout.html with authentication.

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def payment_handler(request):
    print("payment handler called")
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            order = Order.objects.filter(razorpay_order_id=razorpay_order_id).first()
            if result is not None:
                amount = int(order.price) * 100
                try:

                    # capture the payment
                    razorpay_client.payment.capture(payment_id, amount)
                    # render success page on successful capture of payment
                    return redirect('/dashboard/orders/pending/')
                except Exception as e:
                    print(e)
                    # if there is an error while capturing payment.
                    return render(request, 'payment/fail.html')
            else:
                # if signature verification fails.
                return render(request, 'payment/fail.html')
        except Exception as e:
            print(f"{e =}")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()


def success_view(request):
    context = {}
    return render(request, 'payment/success.html', context)
