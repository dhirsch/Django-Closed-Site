from closed_site import settings

def closed_site(request):
	return {'closed_site_closed' : settings.CLOSED_SITE_CLOSED }