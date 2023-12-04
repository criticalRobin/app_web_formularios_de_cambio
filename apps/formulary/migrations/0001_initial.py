# Generated by Django 4.2.7 on 2023-11-29 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Formulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_surname', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=40)),
                ('change', models.CharField(max_length=30)),
                ('change_description', models.CharField(max_length=120)),
                ('change_justification', models.CharField(max_length=120)),
                ('priority', models.CharField(choices=[('Low', 'Baja'), ('Medium', 'Media'), ('High', 'Alta')], default='Low', max_length=6)),
                ('status', models.CharField(choices=[('Pending', 'Pendiente'), ('Approved', 'Aprobado'), ('Rejected', 'Rechazado')], default='Pending', max_length=8)),
                ('comment', models.CharField(blank=True, max_length=120)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulary.project')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
