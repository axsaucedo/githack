from django.http import HttpResponseRedirect
from githack.models import Subdomain
from django.contrib.sites.models import Site
import settings


class RedirectMiddleware(object):
    """Middleware class that redirects non "www" subdomain requests to a
    specified URL or business.
    """
    def process_request(self, request):
        """Returns an HTTP redirect response for requests including non-"www"
        subdomains.
        """
        scheme = "http" if not request.is_secure() else "https"
        path = request.get_full_path()
        domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
        pieces = domain.split('.')
        subdomain = ".".join(pieces[:-2]) # join all but primary domain
        default_domain = Site.objects.get(id=settings.SITE_ID)
        if domain in {default_domain.domain, "testserver", "localhost", "localhost:8000"}:
            return None
        try:
            route = Subdomain.objects.get(name=subdomain).url
        except Subdomain.DoesNotExist:
            route = path

        if route.startswith('http://') or route.startswith('https://'):
            return HttpResponseRedirect(route)

        return HttpResponseRedirect("{0}://{1}{2}".format(scheme, default_domain.domain, route))