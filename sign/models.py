from django.db import models


# Create your models here.
# 会表
class Event(models.Model):
    name = models.CharField(max_length=100)            # 标题
    limit = models.IntegerField()                      # 参会人数
    status = models.BooleanField()                     # 状态
    address = models.CharField(max_length=200)         # 地址
    start_time = models.DateTimeField('events time')   # 时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间(自动获取当前时间)

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=True)    # 关联发布会id
    real_name = models.CharField(max_length=64)          # 姓名
    phone = models.CharField(max_length=16)             # 手机号
    email = models.EmailField()                         # 邮箱
    sign = models.BooleanField()                        # 签到状态
    create_time = models.DateTimeField(auto_now=True)   # 创建时间(自动获取当前时间)

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.real_name