from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, SubjectAreaViewSet, AddressViewSet, BuildingViewSet, LocationViewSet, \
    MeetingTimeViewSet, CampusViewSet, SessionViewSet

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'building', BuildingViewSet)
router.register(r'location', LocationViewSet)
router.register(r'subject-area', SubjectAreaViewSet)
router.register(r'course', CourseViewSet)
router.register(r'meeting-time', MeetingTimeViewSet)
router.register(r'campus', CampusViewSet)
router.register(r'session', SessionViewSet)

# app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]
