# Generated by Django 3.2.5 on 2021-07-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=255)),
                ('rollno', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('mobile', models.IntegerField(default='')),
                ('image', models.ImageField(default='', upload_to='upload')),
            ],
        ),
    ]
