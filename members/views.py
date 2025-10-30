from django.template import loader
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())