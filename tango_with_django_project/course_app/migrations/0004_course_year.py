# Generated by Django 2.2.27 on 2022-03-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='course_app.Year'),
        ),
    ]