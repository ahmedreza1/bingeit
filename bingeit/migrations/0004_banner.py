# Generated by Django 2.2.5 on 2020-07-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bingeit', '0003_auto_20200723_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=500)),
                ('main_img', models.ImageField(null=True, upload_to='image\\')),
                ('link', models.CharField(max_length=240)),
                ('Short_description', models.CharField(max_length=240)),
            ],
        ),
    ]
