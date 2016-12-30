# from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import (
    TemplateView
)


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if user.is_anonymous():
            return super(IndexView, self).dispatch(*args, **kwargs)
        else:
            return redirect('new_task_view')


# class DashboardView(TemplateView):
#     def dispatch(self, *args, **kwargs):
#         user = self.request.user
#         if user.is_anonymous():
#             return super(DashboardView, self).dispatch(
#                 self.request, *args, **kwargs)
#
#         return super(DashboardView, self).dispatch(*args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(DashboardView, self).get_context_data(**kwargs)
#         return context
#
#     def get_template_names(self):
#         template_name = 'task/dashboard.html'
#         return [template_name]
