from django.shortcuts import render, redirect
from .auth_models import User
from django.contrib.auth import login as dj_login, logout as dj_logout, authenticate


def login(request):
    ctx = {

    }
    if request.POST:
        phone = request.POST.get('phone',None)
        password = request.POST.get('password',None)
        if None in[phone,password]:
            ctx['error'] = "Ma'lumotlar to'liq emas"
            return render(request,'auth/login.html',ctx)

        user = User.objects.filter(phone=phone).first()
        if not user:
            ctx['error'] = "Bunaqa User topilmadi"
            return render(request,"auth/login.html",ctx)

        if not user.check_password(str(password)):
            ctx['error'] = "'Parol noto'g'ri"
            return render(request, "auth/login.html", ctx)


        dj_login(request, user)
        return redirect('home')



    return render(request,'auth/login.html',ctx)

def regis(request):
    if request.POST:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        pass_conf = request.POST.get('pass_conf')

        if phone is None or password is None or pass_conf is None:
            return render(request,'auth/register.html',{'error':"ma'lumot to'liq emas"})

        if pass_conf != password:
            return render(request,'auth/register',{"error":"Parollar bir xil emas"})

        if 6 > len(password) or len(password) > 15:
            return render(request, 'auth/register', {"error": "Parollar uzunligi xato"})
        user = User.objects.filter(phone=phone).first()
        if user:
            return render(request,'auth/register.html',{"error":"Bunaqa user mavjud"})

        user = User.objects.create_user(
            phone = phone,
            password = password,
            fio = request.POST.get('fio'),
            yosh = request.POST.get('yosh'),
        )
        dj_login(request, user)
        authenticate(request)
        return redirect("home")
    return render(request,'auth/register.html')







def logout(request):
    dj_logout(request)
    return redirect('login')