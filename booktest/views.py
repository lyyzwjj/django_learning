from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo


def my_render(request, template_path, context_dict={}):
    # 使用模板文件
    # 1.加载模板文件
    temp = loader.get_template(template_path)
    # 2.定义模板上下文:给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3.模板渲染:产生标准的html内容
    res_html = temp.render({'context': context})
    # 4.返回给浏览器
    return HttpResponse(res_html)


# 1. 定义视图函数,HttpRequest
# 2. 进行url配置,建立url地址和视图的对应的关系
def index(request):
    # return my_render(request, "booktest/index.html", {'content': 'hello world'})
    return render(request, "booktest/index.html", {'content': 'hello world', 'list': list(range(1, 10))})


# M和T交互
# return HttpResponse('老铁,没毛病')


def index2(request):
    # M和T交互
    return HttpResponse('老铁,没毛病2')


def show_books(request):
    ''' 显示图书信息'''
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})


def detail(request, bid):
    '''查询图书关联的英雄信息'''
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
