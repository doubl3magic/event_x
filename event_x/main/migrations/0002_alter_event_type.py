# Generated by Django 4.0.3 on 2022-04-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Concert', 'Concert'), ('Theatrical', 'Theatrical'), ('Fan meeting', 'Fan meeting'), ('Seminar', 'Seminar'), ('Ceremonies', 'Ceremonies')], max_length=11),
        ),
    ]
