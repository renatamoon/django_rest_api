# PROJECT IMPORTS
from .models import Tenant


def get_hostname(request):
    response = request.get_host().split(':')[0].lower()

    return response


def get_tenant(request):
    hostname = get_hostname(request)
    subdomain = hostname.split('.')[0]

    tenant_response = Tenant.objects.filter(subdomain=subdomain).first()

    return tenant_response
