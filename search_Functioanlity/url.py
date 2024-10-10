
from django.urls import path
from home.views import home, dynamic_path, index,search_page

urlpatterns = [
    path('', home),
    path('dynamic_path/<int:num>/', dynamic_path),
    path('index/', index),
    path('search_page/', search_page)
]
