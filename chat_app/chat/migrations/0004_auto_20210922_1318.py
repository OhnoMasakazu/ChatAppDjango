# Generated by Django 3.2.7 on 2021-09-22 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210921_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='image'),
        ),
    ]