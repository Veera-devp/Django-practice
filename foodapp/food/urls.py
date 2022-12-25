from . import views
from django.urls import path

app_name = "food"
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/',views.detail,name='detail'),
    path('courses/',views.courses,name='courses'),
    
]