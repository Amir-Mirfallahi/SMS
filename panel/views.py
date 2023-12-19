from django.shortcuts import redirect
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = []
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return redirect('/admin')  # Redirect to the admin page
        return super().dispatch(request, *args, **kwargs)
