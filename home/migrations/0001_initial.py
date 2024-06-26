# Generated by Django 5.0.6 on 2024-05-13 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_file', models.FileField(upload_to='videos/%y')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.video')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='videos',
            field=models.ManyToManyField(related_name='users', through='home.UserVideo', to='home.video'),
        ),
    ]
