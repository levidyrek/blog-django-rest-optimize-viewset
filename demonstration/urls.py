from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'demonstration'

router = DefaultRouter()
router.register(r'blog-posts', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
