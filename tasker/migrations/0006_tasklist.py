# Generated by Django 3.0.3 on 2020-03-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0005_auto_20200304_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('tasks', models.ManyToManyField(related_name='lists', to='tasker.Task')),
            ],
        ),
    ]
