# Generated by Django 4.0.6 on 2022-07-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='labels.labels'),
        ),
    ]