# Create your views here.
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    
    template_name = "core/base.html"
    