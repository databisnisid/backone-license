from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .models import Licenses


def decode_license_code(lic_code):
    pass


def check_license(lic_json):
    node_id = lic_json["node_id"]
    uuid = lic_json["uuid"]
    token = lic_json["token"]
    name = lic_json["name"]

    try:
        lic = Licenses.objects.get(
            node_id=node_id, organization_uuid=uuid, controller_token=token
        )
    except ObjectDoesNotExist:
        lic = None

    lic_result = {
        "status": 0,
        "node_id": node_id,
        "uuid": uuid,
        "token": token,
        "name": name,
        "is_block_rule": 1,
        "valid_until": "",
    }
    if lic:
        lic_result["status"] = 1
        lic_result["valid_until"] = str(lic.valid_until)
        lic_result["is_block_rule"] = 1 if lic.is_block_rule else 0

    return lic_result


def check_license_expiry(license: Licenses) -> dict:
    license_time = license.valid_until

    license_status = {}

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

        elif delta_time.days < 30:
            license_status = {
                "node_id": license.node_id,
                "uuid": str(license.organization_uuid),
                "name": license.description,
                "msg": _(
                    "License will be expired in " + str(delta_time.days) + " days"
                ),
                "status": 1,
            }

    else:
        license_status = {
            "node_id": license.node_id,
            "uuid": str(license.organization_uuid),
            "name": license.description,
            "msg": _("License is Empty"),
            "status": 0,
        }

    return license_status


def delete_expired_licenses(is_delete: bool = False) -> None:
    licenses = Licenses.objects.all()

    for license in licenses:
        license_status = check_license_expiry(license)

        if license_status["status"] == 2:
            print(
                "Delete Expired License %s with UUID %s",
                license_status["name"],
                license_status["uuid"],
            )
            if is_delete:
                license.delete()
