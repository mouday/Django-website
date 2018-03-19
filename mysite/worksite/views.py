from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from worksite import models
from django.views import View
import time

# Create your views here.

# 鉴权函数 
def auth(func):
    def inner(request, *args, **kwargs):
        username = request.session.get("username")
        print("auth-username: ", username)
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

        start = (page-1) * per_page
        end = per_page + start

        # 按时间进行排序，最后添加的显示在最前面
        items_all = models.Item.objects.all().order_by("-time")
        items = items_all[start : end]
        states = models.State.objects.all()

        print("index-get")
        paging =Page(len(items_all), per_page)
        # 页面显示的页码
        total = paging.getTotalPage()
        if total < page:  # 如果当前页大于总页数，则跳转到首页
            return redirect("/")
        pages = paging.getPages(page)
        # 上一页，下一页
        prev_page = paging.getPrevPage(page)
        next_page = paging.getNextPage(page)

        dct = {
            "items": items, 
            "states": states,  
            "total": total, 
            "pages": pages,
            "prev_page": prev_page, 
            "next_page": next_page,  
            "current_page": page
        }
        return render(request, "index.html", dct)

    def post(self, request):
        area = request.POST.get("area")
        title = request.POST.get("title")
        content = request.POST.get("content")
        data = request.POST.get("data")
        handle = request.POST.get("handle")

        print("index-post")
        if len(title)>0:
            item =  models.Item(
                title=title, 
                area = area, 
                content=content, 
                data_id=data, 
                handle_id=handle)
            item.save()
        return redirect("/")

@auth
def delete(request):
    if request.method == "POST":
        item_id = request.POST.get("item-id")
        print(item_id)
        models.Item.objects.filter(uid=item_id).delete()
        return redirect("/")

@auth
def edit(request):
    if request.method == "POST":
        edit_id = request.POST.get("edit-id")
        edit_area = request.POST.get("edit-area")
        edit_title = request.POST.get("edit-title")
        edit_content = request.POST.get("edit-content")
        edit_data = request.POST.get("edit-data")
        edit_handle = request.POST.get("edit-handle")

        models.Item.objects.filter(uid=edit_id).update(
            title = edit_title,
            area = edit_area,
            data = edit_data,
            handle= edit_handle,
            content= edit_content)

        return redirect("/")

def login(request):
    
    if request.method == "POST":
        username_post = request.POST.get("username")
        pwd_post = request.POST.get("pwd")

        user = models.User.objects.filter(name=username_post).first()

        print("user.name", user.name)
        print("user.pwd", user.pwd)
        if username_post==user.name and pwd_post==user.pwd:
            # 设置session
            request.session["username"] = username_post
            return redirect("/")

    elif request.method == "GET":
        username = request.session.get("username")
        if username:
            print("login-username: ", username)
            return redirect("/")

    return render(request, "login.html")

def logout(request):
    request.session.clear()  # 清除session
    return redirect("/login")

def init(request):
    from worksite import init
    init.main()
    return HttpResponse("初始化完成")

def search(request):
    title = request.GET.get("search-title")
    # 模糊查询
    items = models.Item.objects.filter(title__icontains=title)
    states = models.State.objects.all()

    return render(request, "search.html", {"items": items, "states": states})