from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/',views.detail,name='detail'),
    path('courses/',views.courses,name='courses'),
    path('add/',views.create_course,name='create_course'),
    path('update/<int:id>/',views.update_course,name="update_course"),
    path('delete/<int:id>/',views.delete_course,name='delete_course'),
]