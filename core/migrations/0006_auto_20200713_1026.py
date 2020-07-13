# Generated by Django 3.0.8 on 2020-07-13 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200713_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_fr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='response_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_fr', to=settings.AUTH_USER_MODEL),
        ),
    ]