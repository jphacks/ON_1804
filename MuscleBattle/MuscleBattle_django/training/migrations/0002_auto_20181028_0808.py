# Generated by Django 2.1.2 on 2018-10-27 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingmenu',
            old_name='week',
            new_name='week1',
        ),
        migrations.AddField(
            model_name='trainingmenu',
            name='week2',
            field=models.IntegerField(default=0),
        ),
    ]
