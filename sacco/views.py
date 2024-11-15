from itertools import count

from django.http import HttpResponse

from sacco.app_forms import CustomerForm
from sacco.models import Customer, Deposit
from django.shortcuts import render

# Create your views here.
def test(request):
    # c1 = Customer(first_name='Saida', last_name='Ali', email='saida@x.com', dob='2000-11-28', gender='Female', weight=62)
    #
    # c1.save()
    #
    # c2 = Customer(first_name='Faida', last_name='Kimeto', email='kimeto@x.com', dob='2002-11-28', gender='Male', weight=67)
    # c2.save()



    customers = Customer.objects.count()
    #fetching one customer
    c1= Customer.objects.get(id=1)
    print(c1)
    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()

    return HttpResponse(f"Ok, Done We have {customers} customers")


def customers(request):
    data = Customer.objects.all()
    return render(request, 'customers.html', {'customers': data})


def add_customer(request):
    form=CustomerForm()
    return render(request, 'customer_form.html',{'form':form})