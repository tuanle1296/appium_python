from behave import *
from tests.features.steps.clock.clock_method import Clock


@given(u'I {method_name} \'{arg}\' is \'{text}\'')
def step_impl(context, method_name, arg, text):
    method = wrapper_method(Clock, method_name, context.mobile_driver)
    method(arg, text)


@when(u'I {method_name} \'{arg}\'')
def step_impl(context, method_name, arg):
    method = wrapper_method(Clock, method_name, context.mobile_driver)
    method(arg)


@then(u'I {method_name} is \'{result}\'')
def step_impl(context, method_name, result):
    method = wrapper_method(Clock, method_name, context.mobile_driver)
    method(result)


def wrapper_method(page, method, driver):
    p = page(driver)
    return getattr(p, method, "No method found")
