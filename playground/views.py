from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Sum, Avg, Min, Max
from django.db.models import Value
from store.models import Customer, Order
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

    # ----------------------------- here using Q object to perform complex filtering -------------------------------
    #  here ~ is used for not
    # customers = Customer.objects.filter(
    #     Q(id__gt=2) & ~Q(first_name__startswith='A'))

    # ----------here using F object for Referencing the value of a field in another field --------------------------
    # customers = Customer.objects.filter(first_name__startswith=F('last_name'))

    # ------------------------------------------sorting data in ascending order----------------------------------
    # customers = Customer.objects.order_by('-first_name')
    # customers = Customer.objects.earliest('-first_name')
    # customers = Customer.objects.latest('-first_name')

    # -------------------------------- limiting the number of records ----------------------------
    # customers = Customer.objects.all()[2:10]

    # ------------------------- selecting field like column in table or joinging table ------------------------
    # customers = Customer.objects.values('id', 'first_name') #this return dict #(values_list) this return tuple
    # this return only selected fields
    # customers = Customer.objects.only('id', 'first_name')
    # this return all the fields except id and first_name
    # customers = Customer.objects.defer('id', 'first_name')

    # ---------------------------------------pre load the collections select_related(1) -------------------------
    # product = Product.objects.select_related('collection').all() # this is used to pre load the foreign key fields

    # this is used to pre load the many to many fields
    # product = Product.objects.prefetch_related('promotions').all()

    # excercise
    # order = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]

    #  Aggrigate methods like Count, Sum, Avg, Min, Max
    customers = Customer.objects.aggregate(count=Count('id'))

    # annotate fucntion
    # querylist = Customer.objects.annotate(new_id=F('Id'))
    querylist = Customer.objects.annotate(fullname=Func(
        F('first_name'), F('last_name'), Value(' '), function='CONCAT'))

    querylist = Customer.objects.annotate(fullname=Concat(
        'first_name', Value(' '), 'last_name'))
    # print('helooo', list(querylist))
    # query_set = Customer.objects.all()
    # for x in query_set:
    #     print(x.first_name)
    return render(request, "hello.html", {'customers': list(customers), 'result': list(querylist)})
# this return all the fields except id and first_name
