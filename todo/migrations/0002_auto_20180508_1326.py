# Generated by Django 2.0.5 on 2018-05-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rollnumber',
            field=models.IntegerField(default=None, null=True),
        ),
    ]