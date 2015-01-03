from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('shorten/base.html', context)

def submit(request):
    context = RequestContext(request)
    return "hello"
