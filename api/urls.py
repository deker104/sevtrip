from rest_framework import routers

from web.views import SuggestionViewSet, RouteViewSet


router = routers.DefaultRouter()
router.register('suggestion', SuggestionViewSet)
urlpatterns = router.urls
