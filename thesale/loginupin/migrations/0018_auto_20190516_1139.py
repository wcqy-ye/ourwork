# Generated by Django 2.1.7 on 2019-05-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginupin', '0017_auto_20190516_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='评论数'),
        ),
    ]
