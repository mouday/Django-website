from worksite import models
import random
import time
import datetime

def initItem():
    areas = ["北京移动", "中国联通", "江苏电信"]
    first_title = "HHSR09-2018-%s-%s"
    contents = ["异常", "ok", "其他"]

    print("Item 初始化开始。。。")
    for i in range(100):
        items = []
        for j in range(10000):

            now_time = datetime.datetime.now()
            r = [x for x in range(-5, 6)]

            # 默认为天
            random_time= now_time + datetime.timedelta(days=random.choice(r))
            current_time=random_time.strftime("%Y-%m-%d")

            item = models.Item(
                title = "HHSR09-2018-%s-%s"%(i, j), 
                area = random.choice(areas), 
                content = random.choice(contents), 
                predata_id = random.choice([1, 2, 3]), 
                data_id = random.choice([1, 2, 3]), 
                label_id =  random.choice([1, 2, 3]),
                card_id =  random.choice([1, 2, 3]),
                chip_id =  random.choice([1, 2, 3]),
                grade_id =  random.choice([1, 2]),
                time = current_time
                )
            items.append(item)
            # 时间转换参考：https://www.cnblogs.com/lxmhhy/p/6030730.html
        models.Item.objects.bulk_create(items)
        # print("Item insert 10000...")
    print("Item 初始化完成！")


def initState():
    models.State.objects.create(name ="未处理")
    models.State.objects.create(name ="已处理")
    models.State.objects.create(name ="异常")
    print("State 初始化完成！")

def initItemState():
    models.ItemState.objects.create(name ="正常")
    models.ItemState.objects.create(name ="已删除")
    print("ItemState 初始化完成！")

def initGrade():
    models.Grade.objects.create(name ="白班")
    models.Grade.objects.create(name ="夜班")
    print("Grade 初始化完成！")

def initUser():
    models.User.objects.create(name = "admin", pwd = "123456")
    models.User.objects.create(name = "jihua", pwd = "123456")
    models.User.objects.create(name = "shuju", pwd = "123456")
    models.User.objects.create(name = "biaoqian", pwd = "123456")
    models.User.objects.create(name = "wuliao", pwd = "123456")
    models.User.objects.create(name = "fengzhuang", pwd = "123456")
    models.User.objects.create(name = "yugerenhua", pwd = "123456")
    models.User.objects.create(name = "gerenhua", pwd = "123456")
    models.User.objects.create(name = "tiebiao", pwd = "123456")
    models.User.objects.create(name = "baozhuang", pwd = "123456")
    models.User.objects.create(name = "feidianxin", pwd = "123456")
    models.User.objects.create(name = "kufang", pwd = "123456")
    print("User 初始化完成！")

def main():
    initState()
    initItemState()
    initGrade()
    initUser()
    # initItem()
