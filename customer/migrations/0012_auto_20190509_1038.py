# Generated by Django 2.2 on 2019-05-09 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0011_reservation_register_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buypackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_added', models.IntegerField()),
                ('add_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='regist_user',
            name='user',
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='Regist_user',
        ),
    ]
