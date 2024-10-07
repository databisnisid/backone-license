from django.urls import path
from .views import upload_view, license_handler, license_download
from dpi.views import dpi_license


urlpatterns = [
    # path('upload/', upload_view, name='upload_view'),
    path("handler/", license_handler, name="license_handler"),
    path("download/<int:license_id>/", license_download, name="license_download"),
    path("dpi/<uuid:uuid>/", dpi_license, name="dpi-license"),
]
