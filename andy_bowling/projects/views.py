from django.shortcuts import render

def home_page(request):
	return render(request, 'home.html')
def project_page(request):
	return render(request, 'project.html')