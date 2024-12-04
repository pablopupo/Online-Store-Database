from django.urls import path
from . import views

app_name = "store"
urlpatterns = [
    # ex: /store/
    path("", views.menu, name="menu"),
    # ex: /store/performance/
    path("performance/", views.performance, name="performance"),
    path("search/", views.search, name="search"),
    path("insert/", views.insert, name="insert"),
    path("delete/", views.delete, name="delete"),
    path("sort/", views.sort, name="sort"),
    path('managedata/', views.manage_data, name='managedata')

]