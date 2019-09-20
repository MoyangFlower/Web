from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

	def clean_tel(self):
		cleaned_data = self.cleaned_data['tel']
		if not cleaned_data.isdigit():
			raise forms.ValidationError('tel must be number!')
		return int(cleaned_data)

	class Meta:
		model = Student
		fields = (
			'name', 'gender', 'profession', 'email', 'tel'
		)

