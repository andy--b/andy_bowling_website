from django.shortcuts import render, HttpResponse
import os

def home_page(request):
	return render(request, 'home.html')
def project_page(request):
	return render(request, 'project.html')
def resume(request):
	# path = open(os.getcwd() + '/projects/static/bootstrap/files/Andy_Bowling_Resume.pdf')
	# response = HttpResponse(path)
	# response['Content-Type'] = "application/pdf"
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Andy_Bowling_Resume.pdf"'
	return HttpResponse(open(os.getcwd() + '/projects/static/bootstrap/files/Andy_Bowling_Resume.pdf'))