# Generated by Django 3.0.5 on 2022-12-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_desc', models.CharField(max_length=200)),
                ('course_price', models.IntegerField()),
            ],
        ),
    ]
