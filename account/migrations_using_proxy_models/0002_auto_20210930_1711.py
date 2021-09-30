# Generated by Django 3.2.7 on 2021-09-30 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('SPY', 'Spy'), ('DRIVER', 'Driver')], default='SPY', max_length=50),
        ),
        migrations.CreateModel(
            name='DriverMore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.driver')),
            ],
        ),
    ]
