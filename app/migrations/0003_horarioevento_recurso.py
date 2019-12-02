# Generated by Django 2.2.7 on 2019-12-02 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_disertante_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('icono', models.CharField(blank=True, max_length=200, null=True)),
                ('archivo', models.FileField(upload_to='recursos')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos', to='app.Evento')),
            ],
            options={
                'db_table': 'recursos',
            },
        ),
        migrations.CreateModel(
            name='HorarioEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('inicio', models.TimeField()),
                ('fin', models.TimeField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='app.Evento')),
            ],
            options={
                'db_table': 'horarios_evento',
            },
        ),
    ]
