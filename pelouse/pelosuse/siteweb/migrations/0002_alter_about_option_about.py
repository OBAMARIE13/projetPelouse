# Generated by Django 3.2.3 on 2021-05-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='option_about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='siteweb.option_about'),
        ),
    ]
