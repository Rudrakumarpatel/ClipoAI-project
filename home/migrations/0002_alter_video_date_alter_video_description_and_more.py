# Generated by Django 5.0.6 on 2024-05-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='video',
            name='status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='', upload_to='videos/%y'),
        ),
    ]