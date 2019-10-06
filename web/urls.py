from rest_framework import routers

from web.views import SuggestionViewSet, AnketaViewSet

router = routers.DefaultRouter()
router.register('suggestion', SuggestionViewSet)
router.register('', AnketaViewSet, basename='anketa')
urlpatterns = router.urls
