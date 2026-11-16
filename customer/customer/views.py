from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!This is the home page of blinkit")

def about(request):
    return HttpResponse("""
                        Welcome to Blinkit!<br>
        Blinkit is an online grocery delivery platform.<br>
        We deliver fresh groceries and daily essentials to your doorstep.<br>
        Thank you for visiting our About page!""")