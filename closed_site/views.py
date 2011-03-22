from closed_site import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from closed_site.forms import AuthenticateForm

def authenticate(request):
	if request.method == "POST":
		form = AuthenticateForm(request.POST)
		if form.is_valid():
			request.session[settings.CLOSED_SITE_SESSION_NAME] = form.cleaned_data["value"]
			return HttpResponseRedirect(request.session.get("next_page","/"))
	else:
		form = AuthenticateForm()

	dic = {
		'form':form, 
		'form_url':request.path,
		'base_template' : settings.CLOSED_SITE_BASE_TEMPLATE,
	}
	return render_to_response(settings.CLOSED_SITE_TEMPLATE,dic,context_instance=RequestContext(request))