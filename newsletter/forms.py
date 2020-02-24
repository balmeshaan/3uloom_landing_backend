from django import forms
from .models import Tutor, Student

class TutorForm(forms.ModelForm):
	class Meta:
		model = Tutor
		fields = '__all__'


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'