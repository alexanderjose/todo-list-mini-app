"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from todo_list.home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # --------------------------------------------------------------------------
    # Home Page App
    # --------------------------------------------------------------------------
    url(
        r'^$',
        home_views.IndexView.as_view(),
        name='todo_index_view'),

    # url(
    #     r'^dashboard/$',
    #     home_views.DashboardView.as_view(),
    #     name='todo_dashboard_view'),

    # url(
    #     r'^tarea/nueva$',
    #     home_views.CrearTareasView.as_view(),
    #     name='new_task_view'),
    #
    # url(
    #     r'^tarea/(?P<pk>[0-9]+)/editar$',
    #     home_views.EditarTareaView.as_view(),
    #     name='update_task_view'),

    # --------------------------------------------------------------------------
    # Home Page App
    # --------------------------------------------------------------------------
    url(r'^admin/', admin.site.urls),

    # --------------------------------------------------------------------------
    # Django All Auth App
    # --------------------------------------------------------------------------
    url(r'^accounts/', include('allauth.urls')),

    # --------------------------------------------------------------------------
    # Django Todo App
    # --------------------------------------------------------------------------
    url(r'^todo/', include('todo_list.task.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
