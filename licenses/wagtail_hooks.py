from django.urls import reverse
from wagtail.contrib.modeladmin.helpers.button import ButtonHelper
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, ObjectList, PermissionHelper, modeladmin_register)
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel
from django.utils.translation import gettext_lazy as _
from .models import Licenses
from crum import get_current_user


class LicensesButtonHelper(ButtonHelper):

    current_classnames = ['button button-small button-primary']


    def json_button(self, obj):
        text = _('Download License')
        #obj_id = obj.id
        button_url = reverse('license_download', args=[obj.id])

        return {
                'url': button_url,
                'label': text,
                'classname': self.finalise_classname(self.current_classnames),
                'title': text,
                }

    def get_buttons_for_obj(self, obj, exclude=None, classnames_add=None, classnames_exclude=None):
        buttons = super().get_buttons_for_obj(
            obj, exclude, classnames_add, classnames_exclude
        )
        if 'json_button' not in (exclude or []):
            buttons.append(self.json_button(obj))


        return buttons


class LicensesPermissionHelper(PermissionHelper):
    '''

    def user_can_list(self, user):
        return True
    '''
    
    def user_can_create(self, user):
        if user.is_superuser:
            return True
        else:
            return False

    def user_can_delete_obj(self, user, obj):
        if user.is_superuser:
            return True
        else:
            return False

    '''
    def user_can_edit_obj(self, user, obj):
        return False
    '''


class LicensesAdmin(ModelAdmin):
    model = Licenses
    button_helper_class = LicensesButtonHelper   # Uncomment this to enable button
    #inspect_view_enabled = True
    menu_label = 'License'  # ditch this to use verbose_name_plural from model
    menu_icon = 'key'  # change as required
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('node_id', 'organization_uuid', 'valid_until', 'description')
    list_filter = ('node_id',)
    search_fields = ('node_id', 'organization_uuid', 'description',)
    permission_helper_class = LicensesPermissionHelper

    panels = [
        MultiFieldPanel([
            FieldPanel('node_id'),
            FieldPanel('organization_uuid'),
            FieldPanel('controller_token'),
            ], heading=_('Site Details')),
        MultiFieldPanel([
            FieldPanel('valid_until'),
            FieldPanel('description'),
            ], heading=_('License Validity')),
        MultiFieldPanel([
            FieldPanel('license_site', read_only=True),
            FieldPanel('license_string', read_only=True),
            FieldPanel('license_server', read_only=True),
            ], heading=_('License Keys'), classname="collapsible collapsed")
    ]

    def get_edit_handler(self):
        superuser_panels = [
            MultiFieldPanel([
                FieldPanel('node_id'),
                FieldPanel('organization_uuid'),
                FieldPanel('controller_token'),
                ], heading=_('Site Details')),
            MultiFieldPanel([
                FieldPanel('valid_until'),
                FieldPanel('description'),
                ], heading=_('License Validity')),
            MultiFieldPanel([
                FieldPanel('license_site', read_only=True),
                FieldPanel('license_string', read_only=True),
                FieldPanel('license_server', read_only=True),
                ], heading=_('License Keys'), classname="collapsible collapsed")
        ]

        admin_panels = [
            MultiFieldPanel([
                FieldPanel('valid_until'),
                FieldPanel('description'),
                ], heading=_('License Validity')),
            MultiFieldPanel([
                FieldPanel('node_id', read_only=True),
                FieldPanel('organization_uuid', read_only=True),
                FieldPanel('controller_token', read_only=True),
                ], heading=_('Site Details')),
            MultiFieldPanel([
                FieldPanel('license_string', read_only=True),
                ], heading=_('License Keys'), classname="collapsible collapsed")
        ]

        current_user = get_current_user()

        if current_user.is_superuser:
            return ObjectList(superuser_panels)
        else:
            return ObjectList(admin_panels)


    ''' Working INIT modeladmin '''
    ''' Not Really Working. Need more test '''
    '''
    def __init__(self, *args, **kwargs):
        self.inspect_view_enabled = False
        super(LicensesAdmin, self).__init__(*args, **kwargs)
    '''

modeladmin_register(LicensesAdmin)

