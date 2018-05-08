from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from todo.views import ListUsers, ListTodo, PostTodo, ChangeStatus, ViewTodo, CreateUser, UserLogin

users_urlpatterns = [
    path('users/list',ListUsers.as_view(), name='listusers'),
    path('users/todos',ListTodo.as_view(), name='listtodos'),
    path('users/post',PostTodo.as_view(), name='posttodo'),
    path('users/status', ChangeStatus.as_view(), name='changestatus'),
    path('users/view/<str:todoid>', ViewTodo.as_view(), name="viewtodo"),
    path('users/create', CreateUser.as_view(), name="createuser"),
    path('users/login', UserLogin.as_view(), name="userlogin" )
]