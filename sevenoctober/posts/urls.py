
from django.urls import path
from posts.views import (PostsList, PostDetails, PostUpdate,
                         PostCreate, PostDelete)
urlpatterns = [

    path('',PostsList.as_view(), name='posts.list'),
    path('<int:pk>', PostDetails.as_view(), name='posts.details'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='posts.edit'),
    path('create', PostCreate.as_view(), name='posts.create'),
    path('<int:pk>/delete', PostDelete.as_view(), name='posts.delete'),

]