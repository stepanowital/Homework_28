# Generated by Django 4.1.7 on 2023-03-21 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('admin', 'Админ'), ('member', 'Пользователь'), ('moderator', 'Модератор')], max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.location')),
            ],
        ),
    ]
