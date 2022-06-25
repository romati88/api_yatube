

from django.urls import include, path
from rest_framework.authtoken import views
from api.views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
