from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tasks/', views.tasks_page, name="tasks_page"),
    path('employees/', views.employees_page, name="employees_page"),
    path('rules/', views.rules_page, name="rules_page"),
    path('tasks/detail/<int:pk>/', views.task_detail_page, name="task_detail_page"),
    path('category/tasks/', views.tasks_by_category_page, name="tasks_by_category_page"),
    path('category/off/', views.off_tasks, name="off_tasks"),
    path('tasks/complete/<int:pk>/', views.mark_task_completed, name='mark_task_completed'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]