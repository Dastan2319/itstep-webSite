# Generated by Django 3.0.3 on 2020-03-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_add', models.DateTimeField()),
                ('date_complete', models.DateTimeField()),
            ],
        ),
    ]
