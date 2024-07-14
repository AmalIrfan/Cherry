from django.conf.urls import handler404
from pprint import pp

def DenyNonAdmins(get_response):
    def middleware(request):
        if request.path.startswith('/admin'):
            if not request.user.is_superuser:
                return handler404(request, Exception())
        return get_response(request)
    return middleware
