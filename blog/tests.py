from django.test import TestCase
from django_redis import get_redis_connection

# Create your tests here.


def tearDown(self):
    get_redis_connection("default").flushall()
