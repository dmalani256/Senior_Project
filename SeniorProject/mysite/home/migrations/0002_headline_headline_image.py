# Generated by Django 4.1.6 on 2023-02-25 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='headline_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbdpd2opUVxL2tYnU2Z2KlayBAbtfWUUuMYvu1_YpSUg&usqp=CAU&ec=48600113', max_length=1000),
        ),
    ]
