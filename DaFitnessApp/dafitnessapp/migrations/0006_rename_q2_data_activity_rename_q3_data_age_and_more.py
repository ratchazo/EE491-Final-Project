# Generated by Django 4.0.5 on 2022-07-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dafitnessapp', '0005_pie_snacks_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='q2',
            new_name='activity',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='q3',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='q4',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='q5',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='data',
            name='q1',
        ),
        migrations.AddField(
            model_name='data',
            name='gender',
            field=models.CharField(choices=[('m', 'm'), ('f', 'f')], max_length=1, null=True),
        ),
    ]
