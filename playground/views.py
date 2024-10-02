from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
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
    # customers = Customer.objects.filter(
    #     id__gt=2).filter(first_name__startswith='A')

    # here using Q object to perform complex filtering
    #  here ~ is used for not
    # customers = Customer.objects.filter(
    #     Q(id__gt=2) & ~Q(first_name__startswith='A'))

    # here using F object for Referencing the value of a field in another field
    # customers = Customer.objects.filter(first_name__startswith=F('last_name'))

    # sorting data in ascending order
    # customers = Customer.objects.order_by('-first_name')
    # customers = Customer.objects.earliest('-first_name')
    # customers = Customer.objects.latest('-first_name')

    # limiting the number of records
    customers = Customer.objects.all()[2:10]
    print(list(customers))
    # query_set = Customer.objects.all()
    # for x in query_set:
    #     print(x.first_name)
    return render(request, "hello.html", {'customers': list(customers)})
