from behave import *
from tests.features.steps.clock.clock_method import Clock


@given(u'I \'{method_name}\' \'{arg}\' is \'{text}\'')
def step_impl(context, method_name, arg, text):
    wrapper_method(Clock, method_name, context.mobile_driver, arg, text)


@when(u'I \'{method_name}\' \'{arg}\'')
def step_impl(context, method_name, arg):
    wrapper_method(Clock, method_name, context.mobile_driver, arg)


@then(u'I \'{method_name}\' is \'{result}\'')
def step_impl(context, method_name, result):
    wrapper_method(Clock, method_name, context.mobile_driver, result)


def wrapper_method(page, method, driver, *args):
    p = page(driver)
    func = getattr(p, method, "No method found")
    func(*args)
