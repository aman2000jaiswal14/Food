# Generated by Django 3.2.6 on 2022-02-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fooditems',
            fields=[
                ('foodid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('minutes', models.IntegerField()),
                ('n_steps', models.IntegerField()),
                ('steps', models.JSONField()),
                ('ingredients', models.JSONField()),
                ('n_ingredients', models.IntegerField()),
            ],
        ),
    ]