from django.shortcuts import render, redirect
from .models import Category,Meal
from .forms import Ctgform
# Create your views here.

def index(request):
    ctgs = Category.objects.all()

    ctx = {
        'ctgs':ctgs
    }
    return render(request,'index.html',ctx)

def add_food(request):
    ctx = {

    }
    return render(request,'add_food.html',ctx)

def add_category(request):
    if request.POST:
        form = Ctgform(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            request.session['session'] = "Yangi Categoriya Qo'shildi"
        else:
            request.session['error'] = f"Xatolik: {request.errors}"
        return redirect('add-category')

    ctx = {
        "ctgs":Category,
    }
    success = request.session.get('success', None)
    error = request.session.get('error', None)
    ctx['success'] = success
    ctx['error'] = error
    try: del request.session['success']
    except: ...
    try: del request.session['error']
    except: ...
    return render(request,'add_category.html',ctx)
