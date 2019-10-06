from rest_framework import routers

from api.views import RouteViewSet


router = routers.DefaultRouter()
router.register('route', RouteViewSet)
urlpatterns = router.urls
