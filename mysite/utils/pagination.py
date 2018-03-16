class Page(object):
    # 分页使用的类
    def __init__(self, data_length, per_page):
        self.data_length = data_length
        self.per_page = per_page
        self.total = self.getTotalPage()

    def getTotalPage(self):
        # 求总页数
        total, remainder = divmod(self.data_length, self.per_page)
        if remainder > 0:
            total += 1
        print(total)
        return total

    def getPages(self, current_page, show_page = 10):
        # 页面显示的页码
        half = int(show_page/2)
        print(half)
        if self.total <= show_page:  # 总页数小于每页数量
                pages = [i for i in range(1 , self.total + 1)]
        elif current_page < half + 1:  # 前几页
            pages = [i for i in range(1, show_page + 2)]   # 1-12
            print("111")
        elif current_page > self.total - half:  # 后几页
            pages = [i for i in range(self.total - show_page , self.total + 1)]  # (100-10 101)
            print("current_page",current_page)
            print("self.total - half", self.total - half)
            print("222")

        else:  # 中间页
            pages = [i for i in range(current_page - half , current_page + half+1)] # 
            print("333")
        return pages

    def getPrevPage(self, current_page):
        # 上一页
        prev_page = current_page - 1
        if prev_page <= 0:
            prev_page = 1
        return prev_page

    def getNextPage(self, current_page):
        # 下一页
        next_page = current_page + 1 
        if next_page >= self.total:
            next_page = self.total 
        return next_page