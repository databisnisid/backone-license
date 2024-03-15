import json
from base64 import b64decode, b64encode
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wagtail.admin.views.generic.preview import JsonResponse
from django.views.decorators.csrf import requires_csrf_token
from config.utils import to_json
from .models import Licenses
from .utils import check_license


def upload_view(request):
    return render(request, 'licenses/upload.html', locals())


@requires_csrf_token
def license_handler(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    response = JsonResponse({'error': 'Uknown Error'})
    response.status_code = 500
    if request.method == 'POST' and is_ajax:
        if request.body:
            #print(request.body)
            lic_enc = request.body

            try:
                lic_json_str = b64decode(lic_enc).decode()

            except:
                lic_json_str = None

            if lic_json_str:
                #print(lic_json_str)
                lic_json = to_json(lic_json_str)
                if lic_json:
                    print(lic_json)
                    lic_json_check = check_license(lic_json)
                    response = JsonResponse(lic_json_check, 
                                            json_dumps_params={'indent': 4})
                    response.status_code = 200
                else:
                    response = JsonResponse({'error': 'License Code Error'})
                    response.status_code = 500

            else:
                response = JsonResponse({'error': 'License Decode Error'})
                response.status_code = 500
        else:
            response = JsonResponse({'error': 'License is empty'})
            response.status_code = 500

    return response


@login_required
def license_download(request, license_id):
    try:
        lic = Licenses.objects.get(id=license_id)
        is_block_rule = 1 if lic.is_block_rule else 0
        lic_json = {
                'name': str(lic.description),
                'node_id': str(lic.node_id),
                'uuid': str(lic.organization_uuid),
                'token': str(lic.controller_token),
                'is_block_rule': is_block_rule,
                'license_code': str(lic.license_string)
                }
    except ObjectDoesNotExist:
        lic_json = {}

    try:
        filename = lic_json['token'] + '.lic'
    except:
        filename = 'license.lic'

    lic_json_str = json.dumps(lic_json)
    lic_json_enc = b64encode(lic_json_str.encode()).decode()

    response = HttpResponse(lic_json_enc, content_type='application/text')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response


