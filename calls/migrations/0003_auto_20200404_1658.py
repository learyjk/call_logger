# Generated by Django 3.0.5 on 2020-04-04 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calls', '0002_auto_20200404_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='caller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
