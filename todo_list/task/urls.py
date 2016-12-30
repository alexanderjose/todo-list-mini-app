from django.conf.urls import url
from . import views as tasks_views

urlpatterns = [

    url(
        r'^tarea/nueva$',
        tasks_views.NewTaskView.as_view(),
        name='new_task_view'),

    url(
        r'^tarea/(?P<pk>[0-9]+)/editar$',
        tasks_views.UpdateTaskView.as_view(),
        name='update_task_view'),

    url(
        r'^tarea/lista$',
        tasks_views.ListTaskView.as_view(),
        name='task_list_view'),

]
