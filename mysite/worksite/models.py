from django.db import models
import django.utils.timezone as timezone
import datetime
# Create your models here.
class State(models.Model):
    uid = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=12) # 状态名

class Item(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)  # 订单号
    area = models.CharField(max_length=64)  # 订单地区
    time = models.DateTimeField(default = timezone.now)   # 添加时间，
    data = models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                             default=1, related_name="data_state")  # 数据状态
    handle = models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="handle_state")  # 二次处理状态
    content = models.TextField()    # 备注

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # 姓名
    pwd = models.CharField(max_length=64)  # 密码
