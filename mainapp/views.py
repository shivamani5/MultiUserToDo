from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .forms import SignUpForm, TaskForm
from .models import Task


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            emailuser=form.cleaned_data.get('email')
            if User.objects.filter(email__exact=emailuser).exists():
                messages.error(request,"Email taken, try another email.")
                return redirect('sign_up')
            form.save()
            messages.success(request,'Registration Successfull!')
            return redirect('login')
    else:
        form=SignUpForm()
    context={
        'form':form
    }
    return render(request,'registration/signup.html',context)

def sign_out(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
def display_tasks(request):
    details = Task.objects.filter(user=request.user)
    context={
        'details':details,
    }
    return render(request,'task_list.html',context)

@login_required
def add_task(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task_details=form.save()
            task_details.user=request.user
            task_details.save()
            return redirect('/tasks/')
    else:
        form=TaskForm()

    context={
        'form':form
    }
    return render(request,'create_task.html',context)

@login_required(login_url="/login/")
def edit_task(request,id):
    task=get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST' :
        form =TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form=TaskForm(instance=task)

    context={
        'form':form,
    }
    return render(request,'edit_task.html',context)

@login_required(login_url="/login/")
def  delete_task(request,id):
    task=get_object_or_404(Task ,id=id, user= request.user)
    task.delete()
    # return render(request,'delete_task.html')
    return redirect('/tasks/')
