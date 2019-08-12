#  myapp/models.py
from __future__ import unicode_literals # future between underscores, 2 on each side
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from django.db import connection
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models
from django.contrib.auth.models import User
from cassandra.cqlengine.management import sync_table

# Create your models here.
class Test1(DjangoCassandraModel):
    
    _table_name = "test1"
    __keyspace__ = "mykeyspace"
    nid   = columns.Integer(primary_key=True,required=False)
    age  = columns.Text(required=False)


    def __str__(self):
        return (self.nid,self.age)
       


class Test2(DjangoCassandraModel):
    
    _table_name = "test2"
    __keyspace__ = "test_space"
	
    id   = columns.Integer(primary_key=True,required=False)
    name  = columns.Text(required=False)
   
    def __str__(self):
        return (self.id,self.name)
