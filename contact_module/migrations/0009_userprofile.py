# Generated by Django 4.2.4 on 2023-09-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0008_alter_contact_is_read_by_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pf', models.FileField(upload_to='images')),
            ],
        ),
    ]
