from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="用户数")
    user_name = models.CharField(null=False, max_length=50, verbose_name="用户名")
    user_phone = models.CharField(null=False, max_length=50, verbose_name="用户电话")
    user_password = models.CharField(null=False, max_length=50,verbose_name="用户密码")
    user_email = models.EmailField(null=False, verbose_name="用户邮箱")
    user_money = models.IntegerField(null=False, default=0, verbose_name="积分")
    class Meta:

        db_table ='loginupin_users'

        verbose_name ="用户"

        verbose_name_plural = verbose_name

        # ordering = ['-createTime']

    def __str__(self):
        return self.user_name


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')

    gender = models.CharField(max_length=10, default='男', choices=(("男", "男"), ("女", "女")), verbose_name='性别')

    age = models.IntegerField(default=0, verbose_name='年龄')

    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


    class Meta:

        db_table ='loginupin_Student'

        verbose_name ="学生"

        verbose_name_plural = verbose_name

        ordering = ['-createTime']

    def __str__(self):
        return self.name

class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, max_length=100,verbose_name='评论数')
    comment_or = models.CharField(max_length=50, verbose_name='评论者')
    comments = models.CharField(max_length=100, verbose_name='评论')
    comment_time = models.DateField(verbose_name='评论时间')
    class Meta:

        db_table ='loginupin_comment'

        verbose_name ="评论表"

        verbose_name_plural = verbose_name

        # ordering = ['-createTime']

    def __str__(self):
        return self.comment_or

