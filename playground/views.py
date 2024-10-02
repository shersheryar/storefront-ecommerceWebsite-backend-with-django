from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Customer
# Create your views here.


def say_hello(request):

    # objects perform as an interface to the database
    # help to interact with the database without writing SQL queries directly to the database
    #  ORM (Object Relational Mapping) is a programming technique that allows developers to interact with a relational database using an object-oriented programming language.

    # retrieve all the records from the database
    # try:
    #     customer = Customer.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     return HttpResponse("Customer does not exist")
    # customer = Customer.objects.first()

    # filtering data
    # customers = Customer.objects.filter(id__range=(1, 3))

    # complex filtering
    customers = Customer.objects.filter(
        id__gt=2).filter(first_name__startswith='A')
    print(list(customers))
    # query_set = Customer.objects.all()
    # for x in query_set:
    #     print(x.first_name)
    return render(request, "hello.html", {'customers': list(customers)})
