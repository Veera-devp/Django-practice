from django.db import models

# Create your models here.
class course(models.Model):

    def __str__(self):
        return self.course_name

    course_name = models.CharField(max_length=200)
    course_desc = models.CharField(max_length=200)
    course_price = models.IntegerField()
