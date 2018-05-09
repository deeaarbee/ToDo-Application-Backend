from todo.models import User
from django.contrib.auth import authenticate, login


def createUser(username:str, password:str, email:str, rollnumber:int)->User:
    user = User.objects.create_user(username=username,email=email, password=password, rollnumber=rollnumber)
    return user

def loginUser(request,username:str, password:str )->User:
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
    return user