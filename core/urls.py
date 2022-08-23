
from django.contrib import admin
from django.urls import path,include
from author import url as authorUrl
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include(authorUrl))
]
