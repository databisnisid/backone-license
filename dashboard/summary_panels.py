from django.core.exceptions import ObjectDoesNotExist
from wagtail.admin.ui.components import Component
from django.conf import settings
from crum import get_current_user
from django.utils.translation import gettext as _
from django.utils import timezone
from django.db.models import Count
from django.contrib.auth.models import Group
from licenses.models import Licenses
from licenses.utils import check_license_expiry


class LicenseSummaryPanel(Component):
    order = 5
    template_name = "dashboard/license_summary.html"

    def get_context_data(self, parent_context):
        # request = parent_context["request"]
        context = super().get_context_data(parent_context)

        licenses = Licenses.objects.all()

        license_status_list = []

        for license in licenses:

            license_status = check_license_expiry(license)

            license_status_list.append(license_status)

            """
            license_time = license.valid_until
            if license_time:

                delta_time = license_time - timezone.now()

                print("License day", delta_time.days)

                if delta_time.days < 0:
                    license_status = {
                        "node_id": license.node_id,
                        "uuid": str(license.organization_uuid),
                        "name": license.description,
                        "msg": _("License Expired"),
                        "status": 2,
                    }
                    license_status_list.append(license_status)

                elif delta_time.days < 30:
                    license_status = {
                        "node_id": license.node_id,
                        "uuid": str(license.organization_uuid),
                        "name": license.description,
                        "msg": _(
                            "License will expired in " + str(delta_time.days) + " days"
                        ),
                        "status": 1,
                    }
                    license_status_list.append(license_status)

            else:
                license_status = {
                    "node_id": license.node_id,
                    "uuid": str(license.organization_uuid),
                    "name": license.description,
                    "msg": _("License is Empty"),
                    "status": 0,
                }
                license_status_list.append(license_status)
            """

        # print(license_status_list)
        context["license_status"] = license_status_list
        return context


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
            "EC1100": "License Key and Code are empty",
            "EC1101": "Node ID is NOT match",
            "EC1102": "UUID is NOT match",
            "EC1103": "Token is NOT match",
            "EC1104": "License is expired",
            "EC1105": "License Code Decode Error",
            "EC1106": "JSON Error",
            "EC1107": "License Key Decode Error",
            "EC1108": "License Key Load Error",
            "EC1109": "License Key Decryption Error",
            "EC1110": "Unknown Error",
            "EC1111": "Node ID is not exist",
            "EC1112": "UUID is not exist",
            "EC1113": "Token is not exist",
            "EC1114": "Validity Error",
        }

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context["error_codes"] = self.error_codes

        return context


class LicenseDecoderPanel(Component):
    order = 20
    template_name = "dashboard/license_decoder.html"

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        return context
