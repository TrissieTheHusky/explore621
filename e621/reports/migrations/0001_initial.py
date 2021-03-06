# Generated by Django 2.1.3 on 2018-12-05 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.TextField()),
                ('key', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('frequency', models.TextField(choices=[('on_demand', 'On-demand'), ('yearly', 'Yearly'), ('monthly', 'Monthly'), ('weekly', 'Weekly'), ('daily', 'Daily')])),
                ('runner', models.TextField()),
                ('attributes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(auto_now=True)),
                ('result', models.TextField(blank=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
            ],
        ),
        migrations.AddField(
            model_name='datum',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Run'),
        ),
    ]
