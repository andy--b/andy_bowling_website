from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return HttpResponse('<html><title>Home - Andy Bowling</title></html>')
