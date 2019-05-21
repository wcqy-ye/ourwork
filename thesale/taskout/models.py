from django.db import models

# Create your models here.



class tasks_img(models.Model):
    img = models.ImageField(upload_to='img1')
    name = models.CharField(max_length=20)
    img_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.name


class tasks(models.Model):
    task_id = models.AutoField(primary_key=True, verbose_name="任务序号")
    task_class = models.CharField(max_length=20, verbose_name="任务类别")
    task_name = models.CharField(max_length=200, verbose_name="任务名称")
    task_description = models.CharField(max_length=300, verbose_name="任务描述")
    task_publisher = models.CharField(max_length=50, verbose_name="发布者")

    class Meta:

        db_table ='taskout_task'

        verbose_name ="任务"

        verbose_name_plural = verbose_name

        # ordering = ['-createTime']

    def __str__(self):
        return self.task_name