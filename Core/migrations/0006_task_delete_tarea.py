# Generated by Django 5.1.1 on 2024-11-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_tarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
    ]