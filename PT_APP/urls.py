from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('post-detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
]

