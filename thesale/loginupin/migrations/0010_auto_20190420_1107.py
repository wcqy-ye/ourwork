# Generated by Django 2.1.7 on 2019-04-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginupin', '0009_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='users',
            name='user_money',
            field=models.IntegerField(default=0, verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.EmailField(max_length=254, verbose_name='用户邮箱'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户数'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_password',
            field=models.CharField(max_length=50, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_phone',
            field=models.CharField(max_length=50, verbose_name='用户电话'),
        ),
        migrations.AlterModelTable(
            name='users',
            table='users',
        ),
    ]
