# Generated by Django 4.0 on 2022-04-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiple_users', '0002_remove_user_is_customer_remove_user_is_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('request', models.TextField(blank=True)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField()),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
