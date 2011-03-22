from django.conf import settings

CLOSED_SITE_REDIRECT_PATH = getattr(settings,"CLOSED_SITE_REDIRECT_PATH","/login")
CLOSED_SITE_SESSION_NAME = getattr(settings,"CLOSED_SITE_SESSION_NAME","closed_site")
CLOSED_SITE_SESSION_VALUE = getattr(settings,"CLOSED_SITE_SESSION_VALUE","x86n023")
CLOSED_SITE_TEMPLATE = getattr(settings,"CLOSED_SITE_TEMPLATE","closed_site/authenticate.django.html")
CLOSED_SITE_CLOSED = getattr(settings,"CLOSED_SITE_CLOSED",False)