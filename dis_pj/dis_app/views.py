from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,Http404
from .models import Test1,Test2
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
# Create your views here.
def get_data(request):
	print(list(Test2.objects.all()))
	print(list(Test1.objects.all()))
	return render(request, 'retrieve_data.html',{'Test1':list(Test1.objects.all())},{'Test2':list(Test2.objects.all())})

def index(request):
    return render(request, 'hello world')