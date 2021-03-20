# Generated by Django 3.1.7 on 2021-03-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_hash', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]