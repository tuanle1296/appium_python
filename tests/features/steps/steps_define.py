from behave import *

from tests.features.steps.clock.clock_method import Clock


@given(u'I \'{method_name}\' on \'{page}\'')
def given_step_impl(context, method_name, page):
    wrapper_method(page, method_name, context.mobile_driver)


@when(u'I \'{method_name}\' \'{arg}\' on \'{page}\'')
def when_step_impl(context, method_name, arg, page):
    wrapper_method(page, method_name, context.mobile_driver, arg)


@then(u'I \'{method_name}\' is \'{result}\' on \'{page}\'')
def then_step_impl(context, method_name, result, page):
    wrapper_method(page, method_name, context.mobile_driver, result)


def wrapper_method(page, method, driver, *args):
    global value
    mapping = {"clock_page": Clock, }
    if page in mapping:
        value = mapping[page]
    else:
        raise AssertionError("Key does not exist in the dictionary")

    my_instance = value(driver)

    # Specify the method name as a string
    getattr(my_instance, method, "No method found")(*args)
