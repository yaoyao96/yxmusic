# Generated by Django 2.2.3 on 2019-09-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20190901_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpaid',
            name='number_of_course',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='number_of_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
