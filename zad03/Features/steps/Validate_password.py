from behave import *

use_step_matcher("re")

@given("there is a password")
def step_impl(context):
    context.password = ""

@given("it has (?P<letters>[0-9]) letters")
def step_impl(context, letters):
    context.password += "a"*int(letters)

@given("it has (?P<uppercase>[0-9]) uppercase letters")
def step_impl(context, uppercase):
    context.password += "A"*int(uppercase)

@given("it has (?P<digits>[0-9]) digits")
def step_impl(context, digits):
    context.password += "1"*int(digits)

@given("it has (?P<chars>[0-9]) special characters")
def step_impl(context, chars):
    context.password += "@"*int(chars)

@when("checking if password is valid")
def step_impl(context):
    context.isvalid = context.validator.validate(context.password)

@then("the password is invalid")
def step_impl(context):
    assert context.isvalid is False

@then("the password is valid")
def step_impl(context):
    assert context.isvalid is True

