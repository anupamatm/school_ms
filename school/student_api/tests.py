from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('index') # to get url pattern using name attribute
        res = self.client.get(url)  # to get response from the curresponding url(here response will be 'congratulations, you have created an API' ) 
        #here res.data contains message 'congratulations, you have created an API'     
        self.assertEquals(res.data, 'congratulations, you have created an API') # assertEquals method compare two strings
    
    def test_number(self):
        url = reverse('number') # to get url pattern using name attribute
        res = self.client.get(url)  # to get response from the curresponding url(here response will be 'congratulations, you have created an API' ) 
        #here res.data contains message 'congratulations, you have created an API'     
        self.assertEqual(res.data,5)