# Generated by Django 3.0.3 on 2020-05-02 19:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_grade_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercourserelationship',
            unique_together={('user', 'course')},
        ),
    ]