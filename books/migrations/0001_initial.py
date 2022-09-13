# Generated by Django 4.1.1 on 2022-09-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_title', models.CharField(default='', max_length=140)),
                ('publisher', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('dev', 'Development'), ('design', 'Design'), ('PM', 'project manage')], max_length=20)),
                ('private', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=140, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
