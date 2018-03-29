from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from worksite import models
from django.views import View
import time
import logging
# Create your views here.

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
    datefmt='%a, %d %b %Y %H:%M:%S',  
    filename='log/debug.log',  
    filemode='w')  

# 鉴权函数 
def auth(func):
    def inner(request, *args, **kwargs):
        username = request.session.get("username")
        logging.debug("auth-username: %s"%username)
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect("/login")
    return inner

from django.utils.decorators import method_decorator
from utils.pagination import Page

@method_decorator(auth, name="dispatch")
class Index(View):
    def get(self, request):
        # 显示页面：默认首页
        page = int(request.GET.get("page", "1"))
        # 显示数据：默认10个数据
        per_page = int(request.COOKIES.get("per_page", "10"))
        # per_page =10
        
        # 获取首页信息，查询使用
        current_time=time.strftime("%Y-%m-%d", time.localtime())

        logging.debug("current_time: %s"%current_time)

        title = request.GET.get("search-title", "")
        date = request.GET.get("search-date", current_time)

        # 数据修正
        if date == "": date = current_time
        if title =="None": title=""

        logging.debug("search-title：%s %s"%(type(title), title))
        logging.debug("search-date%s"%date)

        struct_time = time.strptime(date, "%Y-%m-%d")
        logging.debug("day: %s"%struct_time.tm_mday)

         # 计算页面显示条数
        start = (page-1) * per_page
        end = per_page + start
        # 搜索当天的订单返回
        # 按时间进行排序，最后添加的显示在最前面
        if title != "":
            items = models.Item.objects.filter(
                title__icontains = title,
                status=1
                ).order_by("grade")[start : end]
            total = models.Item.objects.filter(
                title__icontains = title,
                status=1
                ).count()
        else:
            items = models.Item.objects.filter(
                time__year=struct_time.tm_year,
                time__month=struct_time.tm_mon,
                time__day=struct_time.tm_mday,
                status=1
                ).order_by("grade")[start : end]
            total = models.Item.objects.filter(
                time__year=struct_time.tm_year,
                time__month=struct_time.tm_mon,
                time__day=struct_time.tm_mday,
                status=1
                ).count()

        # 当天没有排产
        if total==0:
            return render(request, "notdata.html",{
                "search_title":title,
                "search_date":date
            })

       
        paging =Page(total, per_page)
        # 页面显示的页码
        total_page = paging.getTotalPage()
        
        if total_page < page:  # 如果当前页大于总页数，则跳转到首页
            return redirect("/")
        pages = paging.getPages(page)

        # 上一页，下一页
        prev_page = paging.getPrevPage(page)
        next_page = paging.getNextPage(page)

        # 模糊查询      
        states = models.State.objects.all()

        dct = {
            "items": items, 
            "states": states,
            "total": total_page, 
            "pages": pages,
            "prev_page": prev_page, 
            "next_page": next_page,  
            "current_page": page,
            "search_date": date,
            "search_title": title,
            "item_count": total,
            "start": start
        }
        logging.debug("index-get")
        return render(request, "index.html", dct)


@auth
def delete(request):
    if request.method == "POST":
        item_id = request.POST.get("item-id")

        logging.debug("删除项目：uid=%s"%item_id)

        models.Item.objects.filter(uid=item_id).update(
            status_id = 2)
        return redirect("/")

@auth
def edit(request):
    if request.method == "POST":
        edit_id = request.POST.get("edit-id")
        edit_area = request.POST.get("edit-area")
        edit_title = request.POST.get("edit-title")
        edit_content = request.POST.get("edit-content")
        edit_predata = request.POST.get("edit-predata")
        edit_data = request.POST.get("edit-data")
        edit_label = request.POST.get("edit-label")
        edit_card = request.POST.get("edit-card")
        edit_grade = request.POST.get("edit-grade")
        edit_chip = request.POST.get("edit-chip")
        edit_time = request.POST.get("edit-time")

        logging.debug("edit_id:%s"%edit_id)
        logging.debug("edit_time:%s"%edit_time)

        username = request.session.get("username")
        """权限说明
            //1、admin
            //2、jihua
            //3、shuju
            //4、biaoqian
            //5、wuliao
        """
        if username=="admin":
            data_dct ={
                    "title": edit_title,
                    "area": edit_area,
                    "predata_id": edit_predata,
                    "data_id": edit_data,
                    "label_id": edit_label,
                    "card_id": edit_card,  
                    "chip_id": edit_chip,
                    "grade_id": edit_grade,
                    "time": edit_time,
                    "content": edit_content,
                }
        elif username=="jihua":
            data_dct ={
                    "title": edit_title,
                    "area": edit_area,
                    "grade_id": edit_grade,
                    "time": edit_time,
                    "content": edit_content,
                }
        elif username=="shuju":
            data_dct ={            
                    "predata_id": edit_predata,  
                    "data_id": edit_data,
                    "content": edit_content,
                }
        elif username=="biaoqian":
            data_dct ={
                   
                    "label_id": edit_label,
                 
                    "content": edit_content,
                }
        elif username=="wuliao":
            data_dct ={
                    
                    "card_id": edit_card,  
                    "chip_id": edit_chip,
                   
                    "content": edit_content,
                }
        else:
            data_dct ={}

        # 修改
        if edit_id != "":   
            models.Item.objects.filter(uid=edit_id).update(**data_dct)
            logging.debug("修改成功")

        # 新增
        else:
            models.Item.objects.create(**data_dct)
            logging.debug("新增成功")
        return redirect("/")

    if request.method == "GET":
        uid = request.GET.get("uid")
        logging.debug("uid:%s"%uid)
        item = None
        edit_mode = "新增" # 模式
        if uid:
            item = models.Item.objects.filter(uid=uid).first()
            edit_mode = "修改"  
        states = models.State.objects.all()
        grades = models.Grade.objects.all()
        logging.debug("item: %s"%item)
        
        dct =  {
            "item": item, 
            "states":states, 
            "grades": grades, 
            "edit_mode":edit_mode
        }

        return render(request, "edit.html", dct)

def login(request):
    if request.method == "POST":
        username_post = request.POST.get("username")
        pwd_post = request.POST.get("pwd")

        user = models.User.objects.filter(name=username_post).first()
        logging.debug("user: %s"%user)
        if user:
            logging.debug("user.name %s"%user.name)
            logging.debug("user.pwd %s"%user.pwd)
            if username_post==user.name and pwd_post==user.pwd:
                # 设置session
                request.session["username"] = username_post
                return redirect("/")

    elif request.method == "GET":
        username = request.session.get("username")
        if username:
            logging.debug("login-username: %s"%username)
            return redirect("/")

    return render(request, "login.html")


def logout(request):
    request.session.clear()  # 清除session
    logging.debug("logout")
    return redirect("/login")


def init(request):
    from worksite import init
    init.main()
    logging.debug("init")
    return HttpResponse("初始化完成")

# 404
@auth
def notfind(request):
    logging.debug("notfind: %s"%request.path_info)
    return render(request, "404.html")