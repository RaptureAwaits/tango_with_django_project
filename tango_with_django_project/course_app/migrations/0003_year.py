# Generated by Django 2.2.27 on 2022-03-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_auto_20220322_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=1)),
            ],
        ),
    ]
