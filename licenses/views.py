from base64 import b64decode
from django.shortcuts import render
from wagtail.admin.views.generic.preview import JsonResponse

from config.utils import to_json


def upload_view(request):
    return render(request, 'licenses/upload.html', locals())


def license_handler(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    response = JsonResponse({'status': 0})
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
                    response = JsonResponse(lic_json, 
                                            json_dumps_params={'indent': 4})
                    response.status_code = 200

    return response

