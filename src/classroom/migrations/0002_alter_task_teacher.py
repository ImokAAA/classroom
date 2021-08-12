# Generated by Django 3.2.3 on 2021-07-31 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_teacher'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
    ]