from closed_site import settings
from django.http import HttpResponseRedirect
#import django.views.static.serve
from django.views.static import serve
from closed_site.views import authenticate
#import closed_site.views.authenticate

class ClosedSite:
    def __init__(self):
        self.redirect_path = settings.CLOSED_SITE_REDIRECT_PATH
        self.session_name = settings.CLOSED_SITE_SESSION_NAME
        self.session_value = settings.CLOSED_SITE_SESSION_VALUE
        self.ignore_views = (serve,authenticate)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Checks the session for a simple value match or a logged in user, and redirects to an authenticate page otherwise
        """
        if view_func in self.ignore_views:
            return None
        
        session_val = request.session.get(self.session_name,None)
        if session_val != self.session_value:
            request.session["next_page"] = request.path
            return HttpResponseRedirect(self.redirect_path)
        
        return None

