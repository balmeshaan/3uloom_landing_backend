from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView

from .models import Tutor, Student
from .forms import TutorForm, StudentForm
# Create your views here.

def welcome(request):
	return render(request, 'welcome.html')


def tutor_create(request):
	form = TutorForm()
	if request.method == "POST":
		form = TutorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('welcome')
	context = {
		'form': form
	}
	return render(request, 'tutor_newsletter.html', context)

def student_create(request):
	form = StudentForm()
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('welcome')
	context = {
		'form' : form
	}
	return render(request, 'student_newsletter.html', context)