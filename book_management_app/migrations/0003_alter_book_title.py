# Generated by Django 5.1.1 on 2024-09-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management_app', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
