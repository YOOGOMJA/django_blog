from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:post_id>', views.detail, name="detail"),
    path('api/comment/new/<int:post_id>' , views.comment_create , name="comment_create"),
    path('api/comment/update/<int:comment_id>' , views.comment_update , name="comment_update"),
    path('api/comment/delete/<int:comment_id>' , views.comment_delete , name="comment_delete"),
    path('api/comment/get/<int:post_id>' , views.get_comment , name="comment_get"),
    
]
