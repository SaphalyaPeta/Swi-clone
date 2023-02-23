# Generated by Django 4.0.5 on 2022-06-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swiggy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=30)),
                ('food', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
