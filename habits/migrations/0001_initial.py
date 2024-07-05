# Generated by Django 5.0.6 on 2024-07-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, help_text='Укажите место выполнения привычки', max_length=100, null=True, verbose_name='Место выполнения привычки')),
                ('time', models.TimeField(help_text='Укажите время выполнения привычки', verbose_name='Время выполнения привычки')),
                ('action', models.CharField(help_text='Укажите действие привычки', max_length=150, verbose_name='Действие привычки')),
                ('is_pleasant_habit', models.BooleanField(default=False, help_text='Укажите, приятная ли привычка', verbose_name='Приятная привычка')),
                ('periodicity', models.PositiveIntegerField(default=1, help_text='Укажите периодичность выполнения привычки', verbose_name='Периодичность выполнения привычки')),
                ('award', models.CharField(blank=True, help_text='Укажите вознаграждение', max_length=150, null=True, verbose_name='Вознаграждение')),
                ('time_complete', models.PositiveIntegerField(default=1, help_text='Укажите время на выполнение привычки', verbose_name='Время на выполнение привычки')),
                ('is_publication', models.BooleanField(default=False, help_text='Укажите признак публикации', verbose_name='Признак публикации')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ['location'],
            },
        ),
    ]
