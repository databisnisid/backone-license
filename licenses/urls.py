from django.urls import path
from .views import upload_view, license_handler, license_download


urlpatterns = [
        #path('upload/', upload_view, name='upload_view'),
        path('handler/', license_handler, name='license_handler'),
        path('download/<int:license_id>/', license_download, name='license_download'),
        ]
