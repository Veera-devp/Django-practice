from django.shortcuts import render
from django.http import HttpResponse
from .models import course
from django.template import loader
# Create your views here.

def index(request):
    course_list = course.objects.all()
    context = {
        'course_list':course_list,
    }
    return render(request,'food/index.html',context)

def courses(request):
    return HttpResponse("This is an Course view")


def detail(request,course_id):
    course_del = course.objects.get(pk=course_id)
    context = {
        'course':course_del,
    }

    return render(request,'food/detail.html',context)
