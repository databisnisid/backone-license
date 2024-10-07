import ast
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from .models import DpiLicenses


def dpi_license(request, uuid):
    try:
        license = DpiLicenses.objects.get(uuid=uuid)
        license_json = ast.literal_eval(license.license)

    except ObjectDoesNotExist:
        license_json = {}

    return JsonResponse(license_json, safe=False)
