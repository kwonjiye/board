from django.urls import include, path
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.getPost, name='getPost'),
    path('getPost', views.getPost, name='getPost'),
    path('Post', views.post, name='post'),

    # path('<int:board_id>/', views.detail, name='detail'),
    # path('write/', views.write, name='write'),
    # path('write/write_board', views.write_board, name='write_board'),
    # path('<int:board_id>/create_reply', views.create_reply, name='create_reply'),
    # path('<int:board_id>/post_like', views.post_like, name='post_like'),
    # path('<int:board_id>/post_dislike', views.post_dislike, name='post_dislike'),
]
