from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import course
from django.template import loader
from .forms import CourseForm
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

def create_course(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/course-form.html',{'form':form})

def update_course(request,id):
    course_update = course.objects.get(id=id)
    form = CourseForm(request.POST or None, instance=course_update)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    
    return render(request,'food/course-form.html',{'form':form,'course': course})

def delete_course(request,id):
    course_del = course.objects.get(id=id)
    if request.method == "POST":
        course_del.delete()
        return redirect('food:index')

    return render(request,'food/course-delete.html',{'course_del':course_del})
