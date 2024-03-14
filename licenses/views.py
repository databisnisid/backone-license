from django.shortcuts import render
from wagtail.admin.views.generic.preview import JsonResponse


def upload_view(request):
    return render(request, 'licenses/upload.html', locals())


def license_handler(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if request.method == 'POST' and is_ajax:
        files = request.FILES.getlist('files[]')
        if files:
            print(files)
            #do some stuff
        else:
            print("NO FILE AT ALL")
        return JsonResponse({'status': 1})

