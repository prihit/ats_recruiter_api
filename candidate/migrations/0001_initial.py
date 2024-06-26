# Generated by Django 5.0.4 on 2024-04-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('years_of_exp', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('current_salary', models.FloatField()),
                ('expected_salary', models.FloatField()),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Rejected', 'Rejected'), ('Shortlisted', 'Shortlisted')], default='Applied', max_length=20)),
            ],
        ),
    ]
