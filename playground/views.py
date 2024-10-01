from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer
# Create your views here.


def say_hello(request):
    # return HttpResponse("hello world")
    # objects perform as an interface to the database
    # help to interact with the database without writing SQL queries directly to the database 
    #  ORM (Object Relational Mapping) is a programming technique that allows developers to interact with a relational database using an object-oriented programming language. 
    query_set = Customer.objects.all()
    for x in query_set:
        print(x.first_name)
    return render(request, "hello.html", {'name': "Sheryar"})
