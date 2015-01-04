from django.shortcuts import render
import logging
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
    dict['recent_links']  = GeneratedURL.objects.all().order_by('-date_generated')[0:10]

    return dict

def index(request):
    context = RequestContext(request)
    defaults = default_values()

    return render_to_response('shorten/index.html', defaults, context)

def generate_alias(url):
    return None

def submit(request):
    """
    View for submitting the URLs.
    :param request:
    :return:
    """
    context = RequestContext(request)
    url = None
    link_form = None
    if request.GET:
        link_form = LinkSubmitForm(request.GET)
    elif request.POST:
        link_form = LinkSubmitForm(request.POST)

    values = default_values()
    if link_form and link_form.is_valid():
        url = link_form.cleaned_data['u']
        link = None
        try:
            link = GeneratedURL.objects.get(url=url)
        except GeneratedURL.DoesNotExist:
            logging.log(logging.INFO, "URL %s doesn't already exist", url)
            pass

        values['status'] = True
        if link is None:
            link = generate_alias(url)
            logging.log(logging.INFO, "Generated link %s", link)
            obj = GeneratedURL(url=url, generated_alias=link)
            obj.save()
            logging.log(logging.INFO, "Saving into database.")

        values['alias'] = link
        return render_to_response('shorten/index.html', values, context)

    values['status'] = False
    return render_to_response('shorten/index.html', values, context)
