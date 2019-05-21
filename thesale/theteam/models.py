from django.db import models

#Create your models here.


class teams_img(models.Model):
    img = models.ImageField(upload_to='img2')
    name = models.CharField(max_length=20)
    img_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(first='published')

class team(models.Model):
    id = models.IntegerField(primary_key=True)
    first = models.CharField(null=False, max_length=15, verbose_name="发起人")
    category = models.CharField(null=False, max_length=20, verbose_name="比赛类别")
    telephone = models.IntegerField(null=False, max_length=15, verbose_name="联系方式")
    email = models.EmailField(null=True, verbose_name="邮箱可选")
    competition = models.CharField(null=False, max_length=20, verbose_name="比赛")
    teamer = models.CharField(null=False, max_length=55, verbose_name="现有队员")
    description = models.CharField(null=False, max_length=100, verbose_name="需要描述")
    objects = models.Manager()  # 默认的管理器
    published = PublishedManager()  # 自定义的管理器 以后我们只需要调用Post.published.all()就能获取所有已发布的

    class Meta:

        db_table ='theteam_team'

        verbose_name ="组队"

        verbose_name_plural = verbose_name

        # ordering = ['-createTime']

    def __str__(self):
        return self.first



