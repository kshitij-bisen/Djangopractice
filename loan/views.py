from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def personal_loan(response):
    return HttpResponse ("<h1>welcome to personal loan page </h1>")

def personal_loan(r):
    return HttpResponse ("<h1>welcome to personal loan page </h1>")

def home_loan(r):
    return HttpResponse ("<h1>welcome to Home loan page </h1>")

def car_loan(r):
    return HttpResponse ("<h1>welcome to car loan page </h1>")

def agri_loan(r):
    return ("<h1>welcome to agri loan page </h1>")