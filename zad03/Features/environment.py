from behave import *
from zad03.ValidatePassword.ValidatePassword import ValidatePassword


def before_scenario(context, scenario):
    context.validator = ValidatePassword()


def after_scenario(context, scenario):
    context.validator = None
