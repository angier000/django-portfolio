# Generated by Django 4.2.5 on 2023-10-01 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_student_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
    ]
