from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import GeneratedURL, LinkSubmitForm
from django.conf import settings

# Create your views here.

def default_values():
    link_form = LinkSubmitForm()
    dict = {}
    dict['link_form'] = link_form
    dict['site_base_url'] = settings.SITE_BASE_URL

    return dict

def index(request):
    context = RequestContext(request)
    defaults = default_values()
    defaults['recent_links'] = GeneratedURL.objects.all().order_by('-date_generated')[0:10]

    return render_to_response('shorten/index.html', defaults, context)

def submit(request):
    context = RequestContext(request)
    return "hello"
