# Generated by Django 2.1.3 on 2018-12-02 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronica', '0009_auto_20181202_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiendas',
            name='productos',
        ),
        migrations.AddField(
            model_name='tiendas',
            name='productos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='electronica.Productos'),
            preserve_default=False,
        ),
    ]