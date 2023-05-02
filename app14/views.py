from django.shortcuts import render,redirect
from django.contrib import messages
from  app14.models import ProductModel
from app14.models import UserRegistation
from django.core.paginator import Paginator


def ShowIndex(request):
    result =ProductModel.objects.all()
    r = request.COOKIES
    l = dict(r)
    le =len(l)
    if le == 1:
        le=0
        return render(request,"Index.html",{"data":result,"length":le})
    else:
        le-=1
        return render(request,"index.html",{"data":result,"length":le})


def admin_login(request):
    return render(request,"admin_login.html")


def view_admin_login(request):
    un =request.POST.get("a1")
    pa =request.POST.get("a2")
    if un == "Biswal" and pa == "Biswal" :
        return render(request,"view_admin.html")
    else:
        messages.error(request,"Invalid User")
        return redirect("admin_login")


def view_product(request):
     # res=ProductModel.objects.all()
    #return render(request,"view_product.html",{"data":res})

     res = ProductModel.objects.all()
     pa  = Paginator(res,2)
     page_no = request.GET.get("page_no",1)
     page = pa.page(page_no)
     return render(request, "view_product.html", {"page": page})



def save_product(request):
    na =request.POST.get("z1")
    pr =request.POST.get("z2")
    qt =request.POST.get("z3")
    img =request.FILES["z4"]
    status = "acative"
    ProductModel(name=na,price=pr,quantity=qt,photo=img,status=status).save()
    return redirect("view_product")


def user_register(request):
    return render(request,"user_register.html")


def new_register(request):
    nm =request.POST.get("y1")
    cn =request.POST.get("y2")
    ml =request.POST.get("y3")
    ps =request.POST.get("y4")
    status = "Pending"
    UserRegistation(name=nm,cno=cn,email=ml,password=ps,status=status).save()
    return redirect("user_register")


def user_login(request):
    return render(request,"user_login.html")


def save_login(request):
    ne=request.POST.get("l1")
    pw=request.POST.get("l2")
    print(ne,pw)
    try:
        UserRegistation.objects.get(name=ne,password=pw)
        return render(request,"main_menu.html")
    except:
        return render(request,"user_login.html",{'error':'Invalid Credentials'})


def show_user(request):
    resu =UserRegistation.objects.all()
    return render(request,"show_user.html",{"data":resu})


def forgot_user(request):
    return render(request,"forgot_user.html")


def Save_details(request):
    un = request.POST.get("un")
    # pw = request.POST.get("pw")
    confirm_pass = request.POST.get("confirm","new")
    try:
        user = UserRegistation.objects.get(name=un)
        user.password = confirm_pass
        user.save()
        return render(request,"user_login.html")
    except:
        return render(request,"forgot_user.html",{'error':"Invalid Credentials"})


def add_to_cart(request):
     k=request.GET.get("c1")
     v=request.GET.get("c2")
     response=redirect('main')
     response.set_cookie(k,v)
     return response






def change_password(request):
    return render(request,"change_password.html")


def new_password(request):
    old =request.POST.get("x1")
   # new =request.POST.get("x2")
    con =request.POST.get("x3","x2")
    try:
        user=UserRegistation.objects.get(password=old)
        user.password = con
        user.save()
        return render(request,"change_password.html")
    except:
        return render(request,"change_password.html",{"error":"Invalid old password"})


def update_product(request):
    up=request.GET.get("no")
    data=ProductModel.objects.get(no=up)
    return render(request,"update_product.html",{"data":data})


def delete(request):
    dl=request.GET.get("no")
    ProductModel.objects.filter(no=dl).delete()
    return redirect("view_product")


def update(request):
    na=request.POST.get("u1")
    nn=request.POST.get("u2")
    pr=request.POST.get("u3")
    qt=request.POST.get("u4")
    ProductModel.objects.filter(no=na).update(name=nn,price=pr,quantity=qt)
    return redirect("view_product")


def in_cart(request):
    return render(request,"in_cart.html",{"data":request.COOKIES})


def iteams_cart(request):
    r = request.COOKIES
    l = dict(r)
    le = len(l)
    if le == 2:
        le = 1
        return render(request, "cart_items.html", {"length": le, "data": request.COOKIES})
    else:
        le -= 1
        return render(request, "cart_items.html", {"length": le, "data": request.COOKIES})


def del_cart(request):
    k = request.GET.get("key")
    response = redirect('iteams_cart')
    response.delete_cookie(k)
    return response