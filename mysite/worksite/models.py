from django.db import models
import django.utils.timezone as timezone
import datetime

now_time = datetime.datetime.now()
current_time=now_time.strftime("%Y-%m-%d")

# Create your models here.

# 工序状态 未处理1 已处理2 异常3
class State(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12) # 状态名


# 班次 白班1 夜班2
class Grade(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12) # 状态名


# 订单状态  正常1 删除2
class ItemState(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12) # 状态名

# 项目记录
class Item(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)  # 订单号
    area = models.CharField(max_length=64)  # 订单地区
    time = models.DateTimeField(default = current_time)   # 添加时间
    predata = models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                             default=1, related_name="predata_state")             # 预个人化数据状态
    data = models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                             default=1, related_name="data_state")             # 个人化数据状态
    label =  models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="label_state")          # 标签
    card =  models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="card_state")           # 卡基
    chip =  models.ForeignKey("State", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="chip_state")           # 模块芯片
    status =  models.ForeignKey("ItemState", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="status_state")         # 订单状态
    grade = models.ForeignKey("Grade", to_field="uid", on_delete=models.CASCADE,
                               default=1, related_name="grade_name")         #  排产时间状态
    content = models.TextField()    # 备注


# 用户，账号密码
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # 姓名
    pwd = models.CharField(max_length=64)  # 密码
