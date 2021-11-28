from rest_framework.routers import DefaultRouter

from customer_club.api.views.category_view import CategoryViewset
from customer_club.api.views.question_view import QuestionViewset

router = DefaultRouter()
router.register(r'customer-club/category', CategoryViewset, basename='customer-club-category')
router.register(r'customer-club/question', QuestionViewset, basename='customer-club-question')

urlpatterns = router.urls
