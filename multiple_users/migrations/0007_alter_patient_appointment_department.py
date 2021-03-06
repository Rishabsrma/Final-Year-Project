# Generated by Django 4.0 on 2022-04-17 15:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_users', '0006_rename_title_patient_appointment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_appointment',
            name='Department',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), ('Oncologist', 'Oncologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Pulmonologist', 'Pulmonologist'), ('Nephrologist', 'Nephrologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Otolaryngologist', 'Otolaryngologist'), ('Dermatologist', 'Dermatologist'), ('Psychiatrist', 'Psychiatrist'), ('Neurologist', 'Neurologist'), ('Radiologist', 'Radiologist'), ('Anesthesiologist', 'Anesthesiologist'), ('Surgeon', 'Surgeon')], max_length=191, null=True),
        ),
    ]
