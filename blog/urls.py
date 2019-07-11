from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:category>/<slug:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('<slug:category>/', PostCategory.as_view()),
    path('', PostList.as_view(), name='post_list_url'),


]