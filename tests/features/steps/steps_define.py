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


# define wrapper_method to call method from class by string input
# this will map the page param with dict and return class name
# then will create instance for class and call method
# With this approach we can call method directly from gherkin step then can minimise duplicate code implemented under
def wrapper_method(page, method, driver, *args):
    mapping = {"clock_page": Clock, }
    if page in mapping:
        value = mapping[page]
    else:
        raise AssertionError("Key does not exist in the dictionary")

    # create instance of class
    my_instance = value(driver)

    # call method from instance by name and args
    getattr(my_instance, method, "No method found")(*args)
