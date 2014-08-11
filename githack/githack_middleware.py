from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from githack.models import Subdomain
from django.contrib.sites.models import Site
import settings

class UsersRedirectMiddleware(object):
    def process_request(self, request):
        """
            Redirects users that have not registered a password and requests them to do so.
        """

        paths_login_required=[
            "/accounts/view/",
        ]

        path = request.get_full_path()
        user = request.user

        if path=="/accounts/login/" or path=="/accounts/signup/":
            if user.is_authenticated():
                return redirect('/accounts/view/')
        else:
            if path in paths_login_required:
                if user.is_anonymous():
                    return redirect('/accounts/login/?next=%s' % path)
                else:
                    if not user.has_usable_password():
                        return redirect('/accounts/set_new_password/?next=%s' % path)


#        if path.__contains__("/accounts"):
#            user = request.user
#            if user.is_anonymous():
#                return

#        domain = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME')
#        pieces = domain.split('.')
#        subdomain = ".".join(pieces[:-2]) # join all but primary domain
#        default_domain = Site.objects.get(id=settings.SITE_ID)
#        if domain in {default_domain.domain, "testserver", "localhost", "localhost:8000"}:
#            return None
#        try:
#            route = Subdomain.objects.get(name=subdomain).url
#        except Subdomain.DoesNotExist:
#            route = path

#        print scheme
#
#
#        if route.startswith('http://') or route.startswith('https://'):
#            return HttpResponseRedirect(route)

        print request.get_full_path()
        return None
#        return HttpResponseRedirect(request.get_full_path())


class SubdomainMiddleware(object):
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