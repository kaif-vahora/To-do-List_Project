# Generated by Django 4.0.2 on 2022-02-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='update_at',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
