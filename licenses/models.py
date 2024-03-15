from django.core.exceptions import ValidationError
import rsa
from base64 import b64encode, b64decode
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone


class Licenses(models.Model):
    node_id = models.CharField(_('Node ID'), max_length=50)
    organization_uuid = models.UUIDField(_('UUID'), unique=True)
    controller_token = models.CharField(_('Token'), max_length=50)
    valid_until = models.DateTimeField(_('Valid Until'))
    description = models.TextField(_('Description'), blank=True, null=True)
    is_block_rule = models.BooleanField(_('Block Rule at Expired'), default=True)

    license_string = models.TextField(_('License Code'),
                                    help_text=_('Copy this to site, and input in License Code'),
                                    blank=True, null=True)
    license_site = models.TextField(_('Site License'), 
                                    help_text=_('Copy this to site, and input in Lisense Key'),
                                    blank=True, null=True)
    license_server = models.TextField(_('Server License'),
                                    help_text=_('Keep this in License Server'),
                                    blank=True, null=True)


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        db_table = 'licenses'
        verbose_name = _('License')
        verbose_name_plural = _('Licenses')

    def __str__(self):
        return '%s' % self.node_id

    def clean(self):
        current_time = timezone.now()

        if self.valid_until <= current_time:
            raise ValidationError({'valid_until': _('License Validity must be in the future from now')})

        #return super(Licenses, self).clean()

    def save(self):
        if self.license_site is None:
            publicKey, privateKey = rsa.newkeys(settings.RSA_KEY_BIT)
            self.license_site = b64encode(privateKey.save_pkcs1()).decode()
            self.license_server = b64encode(publicKey.save_pkcs1()).decode()

        else:
            publicKey = rsa.PublicKey.load_pkcs1(b64decode(self.license_server))
            privateKey = rsa.PrivateKey.load_pkcs1(b64decode(self.license_site))

        valid_until_str = self.valid_until.strftime('%Y-%m-%d %H:%M:%S%z')
        license_code_json = {
                'node_id': self.node_id,
                'organization_uuid': str(self.organization_uuid),
                'controller_token': self.controller_token,
                'valid_until': valid_until_str
                }
        license_code_str = str(license_code_json)
        license_code_enc = rsa.encrypt(license_code_str.encode(), publicKey) 
        self.license_string = b64encode(license_code_enc).decode()

        return super(Licenses, self).save()
