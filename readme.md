# 项目名称：企业流程管理系统

# 项目说明：
    根据企业流程，将各个工序的状态显示到前端，管理人员可以随时查看订单状态，包括异常反馈，减少沟通成本，功能还在完善中

# 项目技术路线：
    前端：html + css(bootstrap) + javascript(jQuery)
    后端：python(Django)
    数据库：sqlite

# 项目主要功能截图：

<center>登录</center>

![登录](img\login.png)

<center>主页</center>

![主页](img\index.png)
    
<center>增加</center>

![主页](img\add.png)

<center>删除</center>

![主页](img\delete.png)

<center>修改</center>

![主页](img\update.png)

<center>查询</center>

![主页](img\select.png)

# 项目主要结构：
    mysite
        - mysite 站点配置文件等
        - static 静态文件，css、js文件
        - templates 模板文件，html文件
        - utils 自定义工具类
        - db.sqlite3 站点数据库
        - run.py 封装的启动脚本
        - manage.py 站点管理脚本
        - worksite 站点app
            - urls.py 站点路由
            - views.py 站点视图
            - models.py 站点模型