from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.api_overview, name="api-overview"),
    path("task-list/", views.task_list, name="task-list"),
    path("task-detail/<slug:slug>/", views.task_detail, name="task-detail"),
    path("task-update/<slug:slug>/", views.task_update, name="task-update"),
    path("task-delete/<slug:slug>/", views.task_delete, name="task-delete"),
    path("create-task/", views.task_create, name="task-create"),
    path("complete-task/<slug:slug>/", views.task_complete, name="task-complete"),
]
