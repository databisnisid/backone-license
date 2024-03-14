from wagtail.wagtailforms.models import AbstractFormField, FORM_FIELD_CHOICES
from wagtail.wagtailforms.forms import FormBuilder
from base64 import b64decode
from config.utils import to_json


def license_handler(f):
    lic_json_enc = f.read()

    try:
        lic_json_str = b64decode(lic_json_enc)

    except:
        pass
        
    lic_json = to_json(lic_json_str)

    return lic_json


