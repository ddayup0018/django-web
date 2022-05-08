from django.shortcuts import render,HttpResponse
from car.models import Car,Car_anpai
from django.db.utils import OperationalError
import shutil
from django.db.models import Q

# Create your views here.
def db_check(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            return HttpResponse('数据库连接错误!')
    return inner

@db_check
def car(request):
    car_list = Car.objects.all()
    context={'car_data':car_list}
    return render(request, 'html/car/car.html', context)

def new(request):
    return render(request,'html/car/new.html')

def new_insert(request):
    try:
        ob =Car()
        ob.cym = request.POST['cym']
        ob.cphm = request.POST['cphm']
        ob.xszzb = request.FILES['xszzb']
        ob.xszfb = request.FILES['xszfb']
        ob.cldjsj = request.POST['cldjsj']
        ob.clgls = request.POST['clgls']
        ob.clzk = request.POST['clzk']
        ob.pcqk = '空闲'
        ob.save()
        context={'info':'新增成功!'}
        return render(request,'html/car/info.html',context)
    except:
        context = {'info': '新增失败!'}
        return render(request, 'html/car/info.html', context)

def anpai(request,ucym=''):
    print(ucym)
    ob= Car.objects.get(cym=ucym)
    print(ob)
    context = {'item':ob}
    return render(request,'html/car/anpai.html',context)

def anpai_insert(request):
    try:
        ob = Car_anpai()
        for i in Car_anpai.objects.all():
            if i.pcqk =='车辆已派出' and i.cym == request.POST['cym']:
                context = {'info': '该车辆已派出!'}
                return render(request, 'html/car/info.html', context)

        ob.cym = request.POST['cym']
        ob.jsy = request.POST['jsy']
        ob.ycsy = request.POST['ycsy']
        ob.pcqk = '车辆已派出'
        ob.save()


        ob_car = Car.objects.get(cym=ob.cym)
        ob_car.pcqk = ob.pcqk
        ob_car.save()
        context={'info':'派车成功!'}
        return render(request, 'html/car/info.html', context)
    except:
        context = {'info': '该车辆已派出!'}
        return render(request, 'html/car/info.html', context)

def guihuan(request,ucym=''):
    temp = Car.objects.get(cym=ucym)
    ghcym=temp.cym
    try:
        wantdata=Car_anpai.objects.get(pcqk='车辆已派出',cym=ucym)
        ob =Car_anpai.objects.get(id = wantdata.id)
        if ob.cym==ghcym:
            context ={'item':ob}
            return render(request,'html/car/guihuan.html',context)
        else:
            context = {'info': '该车辆空闲不可归还!'}
            return render(request, 'html/car/info.html', context)
    except:
            context = {'info': '该车辆空闲不可归还!'}
            return render(request, 'html/car/info.html', context)

def guihuan_update(request):
    try:
        uid = request.POST['id']
        ob = Car_anpai.objects.get(id=uid)
        ob.cym = request.POST['cym']
        ob.jsy = request.POST['jsy']
        ob.csyf = request.POST['csyf']
        ob.csgls = request.POST['csgls']
        ob.syclzk = request.POST['syclzk']
        ob.pcqk = '空闲'
        ob.save()

        ob_car = Car.objects.get(cym=ob.cym)
        ob_car.pcqk = ob.pcqk
        ob_car.save()

        wantdata = Car.objects.get(cym=request.POST['cym'])
        if ob.syclzk !='':
            wantdata.clzk=ob.syclzk
            wantdata.save()
        if ob.csgls !='':
            wantdata.clgls = int(wantdata.clgls)+int(ob.csgls)
            wantdata.save()
        context = {'info': '归还成功!'}
        return render(request, 'html/car/info.html', context)
    except:
        context = {'info': '归还失败'}
        return render(request, 'html/car/info.html', context)

def del_one(request,ucym=''):
    try:
        ob=Car.objects.get(cym=ucym)
        ob.delete()
        context={'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request, 'html/car/info.html', context)

def del_all(request):

    try:
        ob=Car.objects.all()
        ob.delete()
        context={'info':'删除成功!'}
    except:
        context = {'info':'删除失败!'}
    return render(request, 'html/car/info.html', context)

def del_allinfo(request):
    try:
        ob=Car.objects.all()
        ob.delete()
        ob_carinfo=Car_anpai.objects.all()
        ob_carinfo.delete()
        shutil.rmtree('media/car/pictures')
        context={'info':'清空成功!'}
    except:
        context = {'info':'清空失败!'}
    return render(request, 'html/car/info.html', context)

def edit(request, ucym = ''):

    ob = Car.objects.get(cym=ucym)
    context ={'item': ob}
    return render(request,'html/car/edit.html',context)

def edit_update(request):
    try:
        ob = Car.objects.get(cym=request.POST['cym'])
        ob.cym =request.POST['cym']
        ob.cphm = request.POST['cphm']
        ob.xszzb = request.FILES['xszzb']
        ob.xszfb = request.FILES['xszfb']
        ob.cldjsj = request.POST['cldjsj']
        ob.clgls = request.POST['clgls']
        ob.clzk = request.POST['clzk']
        ob.pcqk = request.POST['pcqk']
        ob.save()
        context={'info':'修改成功!'}
    except:
        context = {'info': '修改失败!'}
    return render(request, 'html/car/edit.html', context)

def search(request):
    ob = Car_anpai.objects.all()
    context={'car_anpai_data':ob}
    return render(request,'html/car/search.html',context)

def find_cym(request):
    ucym = request.POST['find_cym']
    ob = Car_anpai.objects.filter(cym=ucym)
    context={'car_anpai_data':ob}
    return render(request, 'html/car/search.html', context)

def find_jsy(request):
    ujsy = request.POST['find_jsy']
    ob = Car_anpai.objects.filter(jsy=ujsy)
    context={'car_anpai_data':ob}
    return render(request, 'html/car/search.html', context)

def find_date(request):
    udate = request.POST['find_date']

    # filter方法执行,引入Q,感觉逻辑不清晰
    # ob = Car_anpai.objects.filter(~(Q(pcsj__gt=udate) | Q(ghsj__lt=udate)))

    # 利用django执行原生sql语句
    ob =Car_anpai.objects.raw('select * from car_anpai_table where pcsj<%s and ghsj>%s',[udate,udate])

    context = {'car_anpai_data': ob}
    return render(request, 'html/car/search.html', context)

def find_other(request):
    ucym=request.POST['find_cym']
    ujsy=request.POST['find_jsy']
    udate=request.POST['find_date']

    mydata=dict()
    if ucym != '':
        mydata['cym']=ucym
    if ujsy != '':
        mydata['jsy']=ujsy
    if udate == '':
        ob = Car_anpai.objects.filter(**mydata)
    else:
        ob= Car_anpai.objects.filter(**mydata).filter(~(Q(pcsj__gt=udate) | Q(ghsj__lt=udate)))

    context = {'car_anpai_data': ob}
    return render(request, 'html/car/search.html', context)