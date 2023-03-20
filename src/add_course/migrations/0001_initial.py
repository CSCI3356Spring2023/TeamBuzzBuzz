# Generated by Django 4.1.7 on 2023-03-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('discussion', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=100)),
                ('ta_required', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]