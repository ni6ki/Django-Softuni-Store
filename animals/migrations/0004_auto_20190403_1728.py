# Generated by Django 2.2 on 2019-04-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20190403_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='animal',
        ),
        migrations.AddField(
            model_name='animal',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.Owner'),
        ),
    ]
