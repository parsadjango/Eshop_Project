# Generated by Django 4.2.4 on 2023-09-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0005_alter_contact_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='response',
            field=models.TextField(blank=True, default=False),
        ),
    ]
