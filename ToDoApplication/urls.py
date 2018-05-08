
from django.contrib import admin
from django.urls import path,include

from todo.urls import users_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += users_urlpatterns