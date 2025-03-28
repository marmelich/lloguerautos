# Generated by Django 4.2 on 2025-03-28 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lloguer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inici', models.DateField()),
                ('data_fi', models.DateField(blank=True, null=True)),
                ('automobil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lloguer.automobil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('automobil', 'data_inici')},
            },
        ),
    ]
