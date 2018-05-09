from rest_framework.request import Request
from typing import Union, Any, Dict
import todo.functions.core as core
from .models import User
Chainable = Any


class RequestInterface:
    def __init__(self):
        self.query_params: Dict = {}
        self.data: Dict = {}


class RequestManager():

    def __init__(
            self
    ) -> Chainable:
        self.type_of_return: str = None
        self.filters: Dict = None
        self.limit: int = None
        self.skip: int = None
        self.request: Union[Request, RequestInterface] = None
        self.query_params = None
        self.post_data = None
        self.id = None
        self.source_url = None

    def set_request(
            self,
            request: Union[Request, RequestInterface]
    ) -> Chainable:
        self.request = request
        self.query_params = self.request.query_params
        self.post_data = self.request.data
        self.source_url = request.META.get('HTTP_REFERER', None)
        return self


    def register(self)->User:
        username = self.post_data.get("username",None)
        email = self.post_data.get("email",None)
        password = self.post_data.get("password",None)
        rollnumber = self.post_data.get("rollnumber",None)

        user = core.createUser(username=username, email=email, password=password, rollnumber=rollnumber)

        return user

    def userlogin(self)->User:
        username = self.post_data.get("username",None)
        password = self.post_data.get("password",None)

        user = core.loginUser(self.request,username,password)
        return user

