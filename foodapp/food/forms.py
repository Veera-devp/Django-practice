from django import forms
from .models import course

class CourseForm(forms.ModelForm):
      class Meta:
            model = course
            fields = ['course_name','course_desc','course_price','course_image']
