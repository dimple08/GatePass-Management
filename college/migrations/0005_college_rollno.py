# Generated by Django 3.2.5 on 2021-07-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_rename_colleges_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='rollno',
            field=models.CharField(default='', max_length=10),
        ),
    ]
