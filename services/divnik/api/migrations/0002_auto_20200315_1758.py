# Generated by Django 3.0.3 on 2020-03-15 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='reward',
            field=models.CharField(default='flag', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='api.UserCourseRelationship'),
        ),
        migrations.AlterField(
            model_name='usercourserelationship',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uc_rels', to='api.Course'),
        ),
        migrations.AlterField(
            model_name='usercourserelationship',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='uc_rels', to=settings.AUTH_USER_MODEL),
        ),
    ]
