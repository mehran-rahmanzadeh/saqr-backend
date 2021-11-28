from rest_framework.routers import DefaultRouter

from users.api.views.user_view import UserViewset

router = DefaultRouter()
router.register(r'profile', UserViewset, basename='profile')

urlpatterns = router.urls
