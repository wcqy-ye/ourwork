# Generated by Django 2.1.7 on 2019-05-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theteam', '0011_auto_20190520_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=15, verbose_name='发起人')),
                ('category', models.CharField(max_length=20, verbose_name='比赛类别')),
                ('telephone', models.IntegerField(max_length=15, verbose_name='联系方式')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱可选')),
                ('competition', models.CharField(max_length=20, verbose_name='比赛')),
                ('teamer', models.CharField(max_length=55, verbose_name='现有队员')),
                ('description', models.CharField(max_length=100, verbose_name='需要描述')),
            ],
            options={
                'verbose_name': '组队',
                'verbose_name_plural': '组队',
                'db_table': 'theteam_team',
            },
        ),
        migrations.CreateModel(
            name='teams_img',
            fields=[
                ('img', models.ImageField(upload_to='img2')),
                ('name', models.CharField(max_length=20)),
                ('img_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
