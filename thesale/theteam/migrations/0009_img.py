# Generated by Django 2.1.7 on 2019-05-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theteam', '0008_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('img', models.ImageField(upload_to='img2')),
                ('name', models.CharField(max_length=20)),
                ('img_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
