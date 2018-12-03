from django.urls import path
from . import views

# アプリのルート(/list2/)にアクセスが有った場合、views.pyのindexが実行される。
app_name = 'list2'

urlpatterns = [
    path('', views.index, name='index'), 
]