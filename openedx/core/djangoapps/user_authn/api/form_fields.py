"""
Field Descriptions
"""
from django.conf import settings
from django.utils.translation import gettext as _
from django_countries import countries

from common.djangoapps.student.models import UserProfile
from common.djangoapps.edxmako.shortcuts import marketing_link
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangoapps.user_api import accounts
from openedx.core.djangoapps.user_authn.api.constants import SUPPORTED_FIELDS_TYPES
from openedx.core.djangolib.markup import HTML, Text



def _add_field_with_configurable_select_options(field_name, field_label, error_message=''):
    """
    Returns a field description
        If select options are given for this field in EXTRA_FIELD_OPTIONS, it
        will be a select type otherwise it will be a text type.
    """
    field_attributes = {
        'name': field_name,
        'label': field_label,
        'error_message': error_message,
    }
    extra_field_options = configuration_helpers.get_value('EXTRA_FIELD_OPTIONS')
    if extra_field_options is None or extra_field_options.get(field_name) is None:
        field_attributes.update({
            'type': SUPPORTED_FIELDS_TYPES['TEXT'],
        })
    else:
        field_options = extra_field_options.get(field_name)
        options = [(str(option.lower()), option) for option in field_options]
        field_attributes.update({
            'type': SUPPORTED_FIELDS_TYPES['SELECT'],
            'options': options
        })

    return field_attributes


def add_level_of_education_field():
    """
    Returns the level of education field description
    """
    # Translators: This label appears above a dropdown menu used to select
    # the user's highest completed level of education.
    education_level_label = _("Highest level of education completed")

    # pylint: disable=translation-of-non-string
    options = [(name, _(label)) for name, label in UserProfile.LEVEL_OF_EDUCATION_CHOICES]

    if settings.ENABLE_COPPA_COMPLIANCE:
        options = list(filter(lambda op: op[0] != 'el', options))

    return {
        'name': 'level_of_education',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': education_level_label,
        'error_message': accounts.REQUIRED_FIELD_LEVEL_OF_EDUCATION_MSG,
        'options': options,
    }


def add_gender_field():
    """
    Returns the gender field description
    """
    # Translators: This label appears above a dropdown menu used to select
    # the user's gender.
    gender_label = _("Gender")

    # pylint: disable=translation-of-non-string
    options = [(name, _(label)) for name, label in UserProfile.GENDER_CHOICES]
    return {
        'name': 'gender',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': gender_label,
        'error_message': accounts.REQUIRED_FIELD_GENDER_MSG,
        'options': options,
    }


def add_year_of_birth_field():
    """
    Returns the year of birth field description
    """
    # Translators: This label appears above a dropdown menu on the form
    # used to select the user's year of birth.
    year_of_birth_label = _("Year of birth")

    options = [(str(year), str(year)) for year in UserProfile.VALID_YEARS]
    return {
        'name': 'year_of_birth',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': year_of_birth_label,
        'error_message': accounts.REQUIRED_FIELD_YEAR_OF_BIRTH_MSG,
        'options': options,
    }


def add_goals_field():
    """
    Returns the goals field description
    """
    # Translators: This phrase appears above a field meant to hold
    # the user's reasons for registering with edX.
    goals_label = _("Tell us why you're interested in {platform_name}").format(
        platform_name=configuration_helpers.get_value("PLATFORM_NAME", settings.PLATFORM_NAME)
    )

    return {
        'name': 'goals',
        'type': SUPPORTED_FIELDS_TYPES['TEXTAREA'],
        'label': goals_label,
        'error_message': accounts.REQUIRED_FIELD_GOALS_MSG,
    }


def add_profession_field():
    """
    Returns the profession field description
    """
    # Translators: This label appears above a dropdown menu to select
    # the user's profession
    profession_label = _("Profession")
    return _add_field_with_configurable_select_options('profession', profession_label)


def add_specialty_field():
    """
    Returns the user speciality field description
    """
    # Translators: This label appears above a dropdown menu to select
    # the user's specialty
    specialty_label = _("Specialty")
    return _add_field_with_configurable_select_options('specialty', specialty_label)


def add_company_field():
    """
    Returns the company field descriptions
    """
    # Translators: This label appears above a field which allows the
    # user to input the Company
    company_label = _("Company")
    return _add_field_with_configurable_select_options('company', company_label)


def add_title_field():
    """
    Returns the title field description
    """
    # Translators: This label appears above a field which allows the
    # user to input the Title
    title_label = _("Title")
    return _add_field_with_configurable_select_options('title', title_label)


def add_job_title_field():
    """
    Returns the title field description
    """
    # Translators: This label appears above a field which allows the
    # user to input the Job Title
    job_title_label = _("Job Title")
    return _add_field_with_configurable_select_options('job_title', job_title_label)


def add_first_name_field():
    """
    Returns the first name field description
    """
    # Translators: This label appears above a field which allows the
    # user to input the First Name

    first_name_label = _("First Name")

    return {
        'name': 'first_name',
        'type': SUPPORTED_FIELDS_TYPES['TEXT'],
        'label': first_name_label,
        'error_message': accounts.REQUIRED_FIELD_FIRST_NAME_MSG,
    }


def add_last_name_field():
    """
    Returns the last name field description
    """
    # Translators: This label appears above a field which allows the
    # user to input the Last Name

    last_name_label = _("Last Name")

    return {
        'name': 'last_name',
        'type': SUPPORTED_FIELDS_TYPES['TEXT'],
        'label': last_name_label,
        'error_message': accounts.REQUIRED_FIELD_LAST_NAME_MSG,
    }


def add_mailing_address_field():
    """
    Returns the mailing address field description
    """
    # Translators: This label appears above a field
    # meant to hold the user's mailing address.
    mailing_address_label = _("Mailing address")

    return {
        'name': 'mailing_address',
        'type': SUPPORTED_FIELDS_TYPES['TEXTAREA'],
        'label': mailing_address_label,
        'error_message': accounts.REQUIRED_FIELD_MAILING_ADDRESS_MSG,
    }


def add_state_field():
    """
    Returns a State/Province/Region field to a description
    """
    # Translators: This label appears above a field
    # which allows the user to input the State/Province/Region in which they live.
    state_label = _("State/Province/Region")

    return {
        'name': 'state',
        'type': SUPPORTED_FIELDS_TYPES['TEXT'],
        'label': state_label,
        'error_message': accounts.REQUIRED_FIELD_STATE_MSG,
    }


def add_city_field():
    """
    Returns a city field to a description
    """
    # Translators: This label appears above a field
    # which allows the user to input the city in which they live.
    city_label = _("City")

    return {
        'name': 'city',
        'type': SUPPORTED_FIELDS_TYPES['TEXT'],
        'label': city_label,
        'error_message': accounts.REQUIRED_FIELD_CITY_MSG,
    }

def add_honor_code_field(separate_honor_and_tos):
        """Add an honor code field to a form description.
        Arguments:
            form_desc: A form description
        Keyword Arguments:
            required (bool): Whether this field is required; defaults to True
        """
        # Separate terms of service and honor code checkboxes
        if separate_honor_and_tos:
            terms_label = _("Honor Code")
            terms_link = marketing_link("HONOR")

        # Combine terms of service and honor code checkboxes
        else:
            # Translators: This is a legal document users must agree to
            # in order to register a new account.
            terms_label = _("Terms of Service and Honor Code")
            terms_link = marketing_link("HONOR")

        # Translators: "Terms of Service" is a legal document users must agree to
        # in order to register a new account.
        label = Text(_(
            "I agree to the {platform_name} {terms_of_service_link_start}{terms_of_service}{terms_of_service_link_end}"
        )).format(
            platform_name=configuration_helpers.get_value("PLATFORM_NAME", settings.PLATFORM_NAME),
            terms_of_service=terms_label,
            terms_of_service_link_start=HTML("<a href='{terms_link}' rel='noopener' target='_blank'>").format(
                terms_link=terms_link
            ),
            terms_of_service_link_end=HTML("</a>"),
        )

        # Translators: "Terms of Service" is a legal document users must agree to
        # in order to register a new account.
        error_msg = _("You must agree to the {platform_name} {terms_of_service}").format(
            platform_name=configuration_helpers.get_value("PLATFORM_NAME", settings.PLATFORM_NAME),
            terms_of_service=terms_label
        )
        field_type = 'CHECKBOX'

        if not separate_honor_and_tos:
            field_type = 'TEXT'

            pp_link = marketing_link("PRIVACY")
            label = Text(_(
                "By creating an account, you agree to the \
                  {terms_of_service_link_start}{terms_of_service}{terms_of_service_link_end} \
                  and you acknowledge that {platform_name} and each Member process your personal data in accordance \
                  with the {privacy_policy_link_start}Privacy Policy{privacy_policy_link_end}."
            )).format(
                platform_name=configuration_helpers.get_value("PLATFORM_NAME", settings.PLATFORM_NAME),
                terms_of_service=terms_label,
                terms_of_service_link_start=HTML("<a href='{terms_url}' rel='noopener' target='_blank'>").format(
                    terms_url=terms_link
                ),
                terms_of_service_link_end=HTML("</a>"),
                privacy_policy_link_start=HTML("<a href='{pp_url}' rel='noopener' target='_blank'>").format(
                    pp_url=pp_link
                ),
                privacy_policy_link_end=HTML("</a>"),
            )

        return {
            'name': 'honor_code',
            'type': SUPPORTED_FIELDS_TYPES[field_type],
            'label': label,
            'error_message': error_msg,
            'default': False
        }

def add_country_field():
    """Add a country field to a form description.
    Arguments:
        form_desc: A form description
    Keyword Arguments:
        required (bool): Whether this field is required; defaults to True
    """
    # Translators: This label appears above a dropdown menu on the registration
    # form used to select the country in which the user lives.

    country_label = _("Country or Region of Residence")

    error_msg = accounts.REQUIRED_FIELD_COUNTRY_MSG

    # If we set a country code, make sure it's uppercase for the sake of the form.
    # pylint: disable=protected-access
    # default_country = form_desc._field_overrides.get('country', {}).get('defaultValue')

    country_instructions = _(
        # Translators: These instructions appear on the registration form, immediately
        # below a field meant to hold the user's country.
        "The country or region where you live."
    )
    # if default_country:
    #     form_desc.override_field_properties(
    #         'country',
    #         default=default_country.upper()
    #     )

    return {
        'name': 'country',
        'type': SUPPORTED_FIELDS_TYPES['SELECT'],
        'label': country_label,
        'error_message': accounts.REQUIRED_FIELD_COUNTRY_MSG,
        'options': list(countries),
        # 'instructions': country_instructions,
        # 'include_default_option':True,
    }
