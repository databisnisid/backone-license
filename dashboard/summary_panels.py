from django.core.exceptions import ObjectDoesNotExist
from wagtail.admin.ui.components import Component
from django.conf import settings
from crum import get_current_user
from django.utils.translation import gettext as _
from django.db.models import Count
from django.contrib.auth.models import Group


class ErrorCodes:
    def __init__(self, error_code, error_desc):
        self.error_code = error_code
        self.error_desc = error_desc


class ErrorMessagesPanel(Component):
    order = 10
    template_name = "dashboard/errormessages_component.html"
    error_codes = []

    def __init__(self):
        self.error_codes = {
                'EC1100': 'License Key and Code are empty',
                'EC1101': 'Node ID is NOT match',
                'EC1102': 'UUID is NOT match',
                'EC1103': 'Token is NOT match',
                'EC1104': 'License is expired',
                'EC1105': 'License Code Decode Error',
                'EC1106': 'JSON Error',
                'EC1107': 'License Key Decode Error',
                'EC1108': 'License Key Load Error',
                'EC1109': 'License Key Decryption Error',
                'EC1110': 'Unknown Error',
                'EC1111': 'Node ID is not exist',
                'EC1112': 'UUID is not exist',
                'EC1113': 'Token is not exist',
                'EC1114': 'Validity Error',
              }

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['error_codes'] = self.error_codes

        return context


class LicenseDecoderPanel(Component):
    order = 20
    template_name = "dashboard/license_decoder.html"

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        return context
