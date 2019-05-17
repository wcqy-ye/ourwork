# Generated by Django 2.1.7 on 2019-05-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='things',
            fields=[
                ('thing_id', models.AutoField(primary_key=True, serialize=False, verbose_name='东西序号')),
                ('thing_class', models.CharField(max_length=20, verbose_name='东西类别')),
                ('thing_name', models.CharField(max_length=200, verbose_name='东西名称')),
                ('thing_description', models.CharField(max_length=300, verbose_name='东西描述')),
                ('thing_publisher', models.CharField(max_length=50, verbose_name='发布者')),
            ],
            options={
                'verbose_name': '物品',
                'verbose_name_plural': '物品',
                'db_table': 'thingfloat_thing',
            },
        ),
    ]
