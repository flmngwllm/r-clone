from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('post', views.Post)
router.register('comments', views.CommentsView)


urlpatterns = [
    path('', include(router.urls))
]