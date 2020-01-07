# Generated by Django 3.0 on 2019-12-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=128)),
                ('Lname', models.CharField(max_length=128)),
                ('Email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
