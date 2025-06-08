"""JiangNa URL Configuration
"""
from django.contrib import admin
from django.urls import path
from JN import views as jNView #从应用导入视图
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getpapercontent/', jNView .makePaperConent),
    path('getpaperindex/', jNView .getPaperIndex),
    path('getpaper/', jNView .getPaper),
    path('getdoc/', jNView.getDoc),
]
