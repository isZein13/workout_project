# Generated by Django 4.0 on 2024-03-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_img', models.ImageField(upload_to='')),
                ('prog_text', models.CharField(max_length=300)),
            ],
        ),
    ]
