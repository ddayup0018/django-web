from django.shortcuts import render,HttpResponse
from people.models import People
from car.models import Car
from django.db.utils import OperationalError

def db_check(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            return HttpResponse('数据库连接错误!')
    return inner

# 首页
@db_check
def index(request):
    people_counts = People.objects.all().count()
    car_counts = Car.objects.all().count()
    context = {'people_counts': people_counts,'car_counts':car_counts}
    return render(request, 'html/index.html', context)

# 用户模块首页,显示全部信息
@db_check
def user(request):
    user_list = People.objects.all()
    context ={'user_data':user_list}
    return render(request, 'html/people/user.html', context)

# 添加页面
@db_check
def new(request):
    return render(request, 'html/people/new.html')

# 执行添加
@db_check
def new_insert(request):
    try:
        ob = People()
        ob.xm = request.POST['xm']
        ob.sfzh = request.POST['sfzh']
        ob.sjhm = request.POST['sjhm']
        ob.xb = request.POST['xb']
        ob.nl = request.POST['nl']
        ob.zw = request.POST['zw']
        ob.gj = request.POST['gj']
        ob.xl = request.POST['xl']
        ob.hyzk = request.POST['hyzk']
        ob.zzmm = request.POST['zzmm']
        ob.hjxx = request.POST['hjxx']
        ob.tc = request.POST['tc']
        ob.save()
        context={'info':'添加成功!'}
    except:
        context = {'info':'添加失败!'}
    return render(request, 'html/people/info.html', context)

# 删除单个
@db_check
def del_one(request,uxm=''):
    try:
        ob =People.objects.get(xm=uxm)
        ob.delete()
        context={'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request, 'html/people/info.html', context)

# 删除全部
@db_check
def del_all(request):
    try:
        ob =People.objects.all()
        ob.delete()
        context={'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request, 'html/people/info.html', context)

# 查找单个
@db_check
def find_one(request):
    uxm = request.POST['find_xm']
    find_user_list = People.objects.filter(xm=uxm)
    context = {'user_data': find_user_list}
    return render(request, 'html/people/find.html', context)

# 修改页面
@db_check
def edit(request,uid=0):
    ob = People.objects.get(id=uid)
    context = {'item':ob}
    return render(request, 'html/people/edit.html', context)

# 执行修改
@db_check
def edit_update(request):
    try:
        uid = request.POST['id']
        ob = People.objects.get(id = uid)

        ob.id = request.POST['id']
        ob.xm = request.POST['xm']
        ob.sfzh = request.POST['sfzh']
        ob.sjhm = request.POST['sjhm']
        ob.xb = request.POST['xb']
        ob.nl = request.POST['nl']
        ob.zw = request.POST['zw']
        ob.gj = request.POST['gj']
        ob.xl = request.POST['xl']
        ob.hyzk = request.POST['hyzk']
        ob.zzmm = request.POST['zzmm']
        ob.hjxx = request.POST['hjxx']
        ob.tc = request.POST['tc']
        ob.save()
        context={'info':'修改成功!'}
    except:
        context = {'info':'修改失败!'}
    return render(request, 'html/people/info.html', context)

