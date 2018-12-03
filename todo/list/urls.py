from django.urls import path
from . import views

# アプリのルート(/list/)にアクセスが有った場合、views.pyのindexが実行される。
app_name = 'list'

urlpatterns = [
    path('', views.index, name='index'),
    path('item1', views.item1, name='item1'),
]