# Generated by Django 3.2.7 on 2021-09-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0013_project_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='notes',
            field=models.TextField(blank=True, help_text='Notes for this project.', null=True),
        ),
    ]