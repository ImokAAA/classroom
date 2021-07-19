# Generated by Django 3.2.3 on 2021-06-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('student', models.ManyToManyField(to='users.Student')),
                ('teacher', models.ManyToManyField(to='users.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('max_grade', models.IntegerField()),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_finish', models.DateTimeField()),
                ('auditory', models.ManyToManyField(to='classroom.Auditory')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('date_assigned', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classroom.task')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
    ]