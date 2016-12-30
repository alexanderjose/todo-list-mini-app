# from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import (
    ListView, FormView
)
from .forms import (
    CrearTareaForm
)
from django.core.urlresolvers import (
    reverse_lazy, reverse
)
from .models import Todo
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)
# from django.conf import settings


class NewTaskView(FormView):
    raise_exception = True
    redirect_unauthenticated_users = True
    form_class = CrearTareaForm
    template_name = 'task/crear_tarea.html'
    success_url = reverse_lazy('task_list_view')

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(
                NewTaskView, self).dispatch(request, *args, **kwargs)
        return super(NewTaskView, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        task = Todo()

        task.descripcion = form.cleaned_data['descripcion']
        # task.status = form.cleaned_data['status']
        task.status = Todo.POR_INICIAR
        task.user = user
        task.save()

        messages.success(
            self.request,
            _('Task created successfuly. Add new.')
        )

        return super(NewTaskView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewTaskView, self).get_context_data(**kwargs)
        # user = self.request.user
        return context


class UpdateTaskView(FormView):
    raise_exception = True
    redirect_unauthenticated_users = True
    form_class = CrearTareaForm
    template_name = 'task/editar_tarea.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(UpdateTaskView, self).dispatch(
                request, *args, **kwargs)

        self._tarea = Todo.objects.get(pk=kwargs['pk'])

        return super(UpdateTaskView, self).dispatch(
            request, *args, **kwargs)

    def get_initial(self):
        return {
            'descripcion': self._tarea.descripcion,
            'status': self._tarea.status,
        }

    def form_valid(self, form):
        descripcion_nueva = form.cleaned_data.get('descripcion')
        tarea = self._tarea
        tarea.status = form.cleaned_data.get('status')
        tarea.descripcion = descripcion_nueva
        tarea.save()
        # messages.success(
        #     self.request,
        #     _('Task updated successfuly.')
        # )
        return super(UpdateTaskView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request,
            _('Task modified successfuly.')
        )
        return reverse('task_list_view')


class ListTaskView(ListView):
    template_name = 'task/tasks_list.html'
    model = Todo
    paginate_by = 5

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(ListTaskView, self).dispatch(*args, **kwargs)
        # else:
        #     return redirect('todo_index_view')
        return super(ListTaskView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListTaskView, self).get_context_data(**kwargs)
        # Se obtiene el id del usuario
        user = self.request.user
        # Se obtienen la lista de las tareas creadas, si se quiere sólo las del
        # usuario que está logueado se habilita la condición: user=user
        tareas = Todo.objects.all().filter(
            user=user
        ).order_by('status')
        # Configuración por defecto de la paginación del template
        paginator = Paginator(tareas, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            tareas = paginator.page(page)
        except PageNotAnInteger:
            tareas = paginator.page(1)
        except EmptyPage:
            tareas = paginator.page(paginator.num_pages)
        # Contexto. Objeto a recorrer en el template.
        context['tareas'] = tareas
        # context['BASE_DIR'] = settings.BASE_DIR
        # context['ROOT_DIR'] = settings.ROOT_DIR
        # context['APPS_DIR'] = settings.APPS_DIR
        return context
