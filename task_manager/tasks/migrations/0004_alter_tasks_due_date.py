# Generated by Django 5.0.1 on 2024-02-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(),
        ),
    ]
