from rest_framework.routers import DefaultRouter
from .views import InternProfileViewset

router=DefaultRouter()

router.register('profiles',InternProfileViewset)

urlpatterns=router.urls