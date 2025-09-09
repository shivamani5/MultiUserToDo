from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index,name='index'),
    path('sign_up/',views.sign_up,name='signup'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',views.sign_out,name='logout'),
    path('tasks/',views.display_tasks,name='tasks'),
    path('add_task/',views.add_task,name='add_task'),
    path('edit_task/<int:id>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:id>/',views.delete_task,name='delete_task'),
]
