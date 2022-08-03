# STANDARD IMPORTS
from django.shortcuts import render

# PROJECT IMPORTS
from .models import Member
from .utilities import get_tenant


def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)

    render_response = render(
        request,
        'tenant/our_team.html',
        {
            'tenant': tenant,
            'members': members
        }
    )

    return render_response
