# Generated by Django 3.2.5 on 2021-08-06 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_college_rollno'),
        ('attendence', '0007_rename_user_id_attendence_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college'),
        ),
    ]