# Generated by Django 5.1.3 on 2024-11-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('pic', models.ImageField(blank=True, default='images/Default_pic.jpg', null=True, upload_to='images/')),
                ('price', models.FloatField()),
            ],
        ),
    ]