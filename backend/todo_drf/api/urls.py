from django.urls import path 

from .views import (
    apiOverview,
    taskList,
    taskDetail,
    taskDelete,
    taskCreate,
    taskUpdate
)

urlpatterns = [
    path('api-overview/', apiOverview, name='api-overview'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<pk>/', taskDetail, name='task-detail'),
    path('task-delete/<str:pk>/', taskDelete, name='task-delete' ),
    path('task-update/<str:pk>/', taskUpdate, name='task-update'),
    path('task-create/', taskCreate, name='task-create')
]

# from .views import TaskViewSets
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', TaskViewSets, basename='tasks')
# urlpatterns = router.urls
