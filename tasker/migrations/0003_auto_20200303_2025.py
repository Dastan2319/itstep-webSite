# Generated by Django 3.0.3 on 2020-03-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_auto_20200302_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]