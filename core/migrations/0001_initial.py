# Generated by Django 2.2.6 on 2019-10-28 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mahasiswa')),
            ],
        ),
    ]