# Generated by Django 5.1.1 on 2024-11-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_rename_create_when_passwordreset_created_when'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]