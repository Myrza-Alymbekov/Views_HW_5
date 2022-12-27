from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from courses import views

router = routers.DefaultRouter()

router.register('mentor', views.MentorAPIViewSet)
router.register('course', views.CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/student/', views.StudentListCreateAPIView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
]