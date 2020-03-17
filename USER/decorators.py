from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def visitor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='homepage'):

    actual_decorator = user_passes_test(
       lambda u: u.is_active and u.is_visitor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def contributor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='homepage'):

    actual_decorator = user_passes_test(
       lambda u: u.is_active and u.is_contributor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='homepage'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
