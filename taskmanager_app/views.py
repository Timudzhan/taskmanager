from django.shortcuts import render, get_object_or_404, redirect, redirect
from .models import Category, Tasks, Rules, Employees
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    categories = Category.objects.all()
    #все задачи
    tasks = Tasks.objects.all().order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'tasks': tasks
    }
    return render(request, "./home.html", context)


def tasks_page(request):
    tasks = Tasks.objects.all().order_by('-created_at')
    context = {
        'tasks': tasks
    }
    return render(request, "./tasks.html", context)

def employees_page(request):
    employees = Employees.objects.all().order_by('ranking')
    context = {
        'employees': employees
    }
    return render(request, "./employees.html", context)

def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "./categories.html", context)

def rules_page(request):
    rules = Rules.objects.all()
    context = {
        'rules': rules
    }
    return render(request, "./rules.html", context)

def task_detail_page(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {
        'task': task
    }
    return render(request, "./task-detail.html", context)

def tasks_by_category_page(request):
    # category = get_object_or_404(Category, slug=slug)
    tasks = Tasks.objects.filter(is_active=False)
    context = {
        # 'category': category,
        'tasks': tasks
    }
    return render(request, "./tasks-by-category-done.html", context)

def off_tasks(request):
    # category = get_object_or_404(Category, slug=slug)
    tasks = Tasks.objects.filter(is_active=True)
    context = {
        # 'category': category,
        'tasks': tasks
    }
    return render(request, "./tasks-off-category.html", context)

def mark_task_completed(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.is_active = True
    task.save()
    return redirect('home_page')

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')