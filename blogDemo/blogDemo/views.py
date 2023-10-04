from typing import Any, Dict
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["heading"] = "Home"
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["heading"] = "About"
        return context
