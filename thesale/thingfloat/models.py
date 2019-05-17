from django.db import models

# Create your models here.

class things(models.Model):
    thing_id = models.AutoField(primary_key=True, verbose_name="东西序号")
    thing_class = models.CharField(max_length=20, verbose_name="东西类别")
    thing_name = models.CharField(max_length=200, verbose_name="东西名称")
    thing_description = models.CharField(max_length=300, verbose_name="东西描述")
    thing_publisher = models.CharField(max_length=50, verbose_name="发布者")

    class Meta:

        db_table ='thingfloat_thing'

        verbose_name ="物品"

        verbose_name_plural = verbose_name

        # ordering = ['-createTime']

    def __str__(self):
        return self.thing_name
