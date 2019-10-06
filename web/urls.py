from rest_framework import routers

from web.views import SuggestionViewSet, RouteViewSet

router = routers.DefaultRouter()
router.register('suggestion', SuggestionViewSet)
router.register('', RouteViewSet, basename='route')
urlpatterns = router.urls
