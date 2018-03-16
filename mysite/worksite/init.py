from worksite import models
import random

def main():
    areas = ["北京移动", "中国联通", "江苏电信"]
    first_title = "HHSR09-2018-001-"
    contents = ["异常", "ok", "其他"]
    count = 0
    for i in range(100):
        count += 1
        models.Item.objects.create(
            title = first_title + str(count), 
            area = random.choice(areas), 
            content = random.choice(contents), 
            data_id = random.choice([1, 2, 3]), 
            handle_id = random.choice([1, 2, 3]))
    print("初始化完成！")


if __name__ == '__main__':
    main()