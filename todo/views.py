from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, permission_classes


from rest_framework.parsers import JSONParser, FormParser
from rest_framework.renderers import JSONRenderer

# from ToDoApp.todo.models import User
from django.contrib.auth import authenticate, login
from .models import TodoBoard, User

import uuid, datetime


class SessionAuthNoCSRF(authentication.SessionAuthentication):

    def enforce_csrf(self, request):
        pass


class CreateUser(APIView):

    def post(self,request, *args, **kwargs):
        print(request.data)
        # try:
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        roll = data['rollnumber']
        user = User.objects.create_user(username, email, password, rollnumber=roll)
        user.save()
        return Response({"message": "User Added Successfully", "status":200}, status=200)
        # except:
        #     return Response({"message": "User cannot be Added ", "status":201}, status=200)


class UserLogin(APIView):

    def post(self,request ,*args, **kwargs):
        print(request.data)
        # try:
        data = request.data
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)
        try:
            if user is not None:
                login(request,user)
                request.session['username'] = username
                return Response({"message": "Login success ", "status":200 }, status=200)
            else:
                return Response({"message": "Login Failed ", "status":200 }, status=200)
        except:
            return Response({"message": "Login Failed ", "status": 200}, status=200)



class ListUsers(APIView):

    # authentication_classes = (authentication.SessionAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class ListTodo(APIView):

    renderer_classes = (JSONRenderer,)
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a list of Todos by the users.
        """
        try:
            todo = TodoBoard.objects.filter(username=request.user.username)
            todolist = []
            for each in todo:
                foo = {}

                foo['status'] = each.status
                foo['description'] = each.description
                foo['dateadded'] = each.date_created
                todolist.append(foo)
            resp = {"message":"Retrieved successfully"}
            resp['data'] = todolist
            resp['status'] = 200
            return Response(resp, status=200)
        except:
            return Response({"message":"List cannot be retrieved","status":201})

class PostTodo(APIView):

    renderer_classes = (JSONRenderer,)
    authentication_classes = (SessionAuthNoCSRF,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        try:
            data = request.data
            user = request.session['username']
            description = data['description']
            todoid  = uuid.uuid1()
            status = data['status']
            if  description == '' or status == '' :
                return Response({"message": "Fields empty", "status": 201}, status=200)
            date_added = datetime.datetime.now().date()
            todo = TodoBoard(todoid=todoid, username=user, description=description, date_created=date_added, status= status)
            todo.save()
            status  = {"message" : "Added successfully", "status": 200}
            return Response(status, status=200)
        except:
            foo = {"message": "Failed to add todo"}
            return Response(foo, status=200)




class ChangeStatus(APIView):

    renderer_classes = (JSONRenderer, )
    authentication_classes = (SessionAuthNoCSRF,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        try:
            username = request.user.username
            description = data['description']
            status = data['status']
            if username == '' or description == '' or status == '' :
                return Response({"message": "Fields empty", "status": 201}, status=200)
            todo = TodoBoard.objects.get(username=username, description=description)
            todo.status = status
            todo.save()
            status  = {"message" : "Changed successfully", "status": 200}
            return Response(status, status=200)
        except:
            foo = {"message": "Failed to change status"}
            return Response(foo, status=200)


class ViewTodo(APIView):

    renderer_classes = (JSONRenderer, )
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, todoid):
        print(todoid)
        todo = TodoBoard.objects.get(todoid=todoid)
        data = {
            "username":todo.username,
            "description":todo.description,
            "status" : todo.status,
            "date_created" : todo.date_created
        }
        status = {"data":data, "message": "Retrieved successfully", "status": 200}
        return Response(status, status=200)
