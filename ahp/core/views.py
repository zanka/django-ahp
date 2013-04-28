# Create your views here.
from django.views.generic.base import TemplateView
from ahp.algorithm.ahp_algorithm import test

class HomeView(TemplateView):
    
    template_name = "core/home.html"
    
    
class AlgorytmView(TemplateView):
    
    template_name = "core/algorithm.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(TemplateView, self).get_context_data(**kwargs)
        
        ctx.update({'test': 'test12'
                    })
        
        test()
        
        return ctx
    