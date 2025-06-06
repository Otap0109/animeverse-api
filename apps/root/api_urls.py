from rest_framework.routers import DefaultRouter
from django.urls import path, include
from char.views import CharViewSet
from franchise.views import FranchiseViewSet

router = DefaultRouter()

router.register(r'characters', CharViewSet, basename='characters')
router.register(r'franchise', FranchiseViewSet, basename='franchise')

urlpatterns = [path('', include(router.urls))]