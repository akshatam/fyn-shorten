from django.shortcuts import render
import logging
from random import randint
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import GeneratedURL, LinkSubmitForm, WordBank
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.

def default_values(request):
    link_form = LinkSubmitForm()
    dict = {}
    dict['link_form'] = link_form
    dict['site_base_url'] = request.META['HTTP_HOST']
    dict['recent_links']  = GeneratedURL.objects.all().order_by('-date_generated')[0:10]
    dict['state'] = 'default'

    return dict

def index(request):
    context = RequestContext(request)
    defaults = default_values(request)

    return render_to_response('shorten/index.html', defaults, context)

def generate_alias(url):
    url_comps = reversed(url.split('/'))
    wordbankobj = None
    for comp in url_comps:
        if wordbankobj is not None:
            break
        words = comp.split('-')
        for word in words:
            try:
                obj = WordBank.objects.get(word=word)
                if hasattr(obj, 'generatedurl'):
                    continue
                else:
                    wordbankobj = obj
                    break
            except WordBank.DoesNotExist:
                continue

    if wordbankobj is None:
        virgins = WordBank.objects.filter(taken=False)
        random = randint(0, len(virgins)-1)
        wordbankobj = virgins[random]

    print "Alias is " + str(wordbankobj.word)
    return wordbankobj

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

    values = default_values(request)
    values['state'] = "submitted"
    if link_form and link_form.is_valid():
        url = link_form.cleaned_data['u']
        link = None
        wobj = None
        try:
            obj = GeneratedURL.objects.get(url=url)
            wobj = obj.generated_alias
        except GeneratedURL.DoesNotExist:
            logging.log(logging.INFO, "URL %s doesn't already exist", url)
            pass

        if wobj is None:
            wobj = generate_alias(url)
            logging.log(logging.INFO, "Generated link %s", wobj.word)
            obj = GeneratedURL(url=url, generated_alias=wobj,)
            obj.save()
            logging.log(logging.INFO, "Saving into database.")

        values['status'] = True
        values['alias'] = wobj.word
        values['fullurl'] = wobj.generatedurl.url
        return render_to_response('shorten/index.html', values, context)

    values['status'] = False
    return render_to_response('shorten/index.html', values, context)

def redirect(request):
    print request
    alias = request.path
    alias = alias.replace('/', '')
    try:
        obj = WordBank.objects.get(word=alias)
        if hasattr(obj, 'generatedurl'):
            genurl = obj.generatedurl
            return HttpResponseRedirect(genurl.url)
        else:
            values = default_values(request)
            values['messages'] = ["Alias '%s' is Unused" % alias,]
            return render_to_response('shorten/index.html', values, RequestContext(request))
    except WordBank.DoesNotExist:
        logging.log(logging.ERROR, "Can't redirect %s", alias)
        values = default_values(request)
        values['status'] = False
        values ['state'] = 'redirecterror'
        values['messages'] = ["No Alias '%s' found" % alias,]
        return render_to_response('shorten/index.html', values, RequestContext(request))