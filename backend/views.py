from django.views import generic

# Create your views here.
class MainView(generic.TemplateView):
    template_name = 'backend/main.html'