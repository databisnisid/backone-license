from django.core.exceptions import ObjectDoesNotExist
from .models import Licenses


def decode_license_code(lic_code):
    pass

def check_license(lic_json):
    node_id = lic_json['node_id']
    uuid = lic_json['uuid']
    token = lic_json['token']
    name = lic_json['name']

    try:
        lic = Licenses.objects.get(node_id=node_id,
                                   organization_uuid=uuid,
                                   controller_token=token)
    except ObjectDoesNotExist:
        lic = None

    lic_result = {
            'status': 0,
            'node_id': node_id,
            'uuid': uuid,
            'token': token,
            'name': name,
            'valid_until': ''
            }
    if lic:
        lic_result['status'] = 1
        lic_result['valid_until'] = str(lic.valid_until)

    return lic_result

