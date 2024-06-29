
import logging
from django.http import HttpResponseForbidden
from blog.settings.base import ADMIN_WHITELIST

logger = logging.getLogger('admin_restrict_middleware')

class AdminRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        logger.debug(f"Client IP: {ip}")


        if request.path.startswith('/admin/') and ip not in ADMIN_WHITELIST:
            return HttpResponseForbidden()
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
