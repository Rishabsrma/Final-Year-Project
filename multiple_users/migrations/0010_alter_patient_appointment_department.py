# Generated by Django 4.0 on 2022-04-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_users', '0009_alter_patient_appointment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_appointment',
            name='Department',
            field=models.CharField(choices=[('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), ('Oncologist', 'Oncologist')], max_length=50, null=True),
        ),
    ]
