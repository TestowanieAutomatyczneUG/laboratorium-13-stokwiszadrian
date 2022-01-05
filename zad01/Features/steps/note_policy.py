from zad01.notes.Note import Note
from behave import *
from assertpy import assert_that

use_step_matcher("re")

@given("you want to create a note with name none")
def step_impl(context):
    context.note_name = None

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with(context.note_name, 4)

@given("you want to create a note with empty name")
def step_impl(context):
    context.note_name = ""

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with(context.note_name, 4)

@given("you want to create a note with name that's not a string")
def step_impl(context):
    context.note_name = 123

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with(context.note_name, 4)

@given("you want to create a note with name that's a string")
def step_impl(context):
    context.note_name = "Maths"

@then("it will work")
def step_impl(context):
    assert_that(Note(context.note_name, 4).get_name()).is_equal_to("Maths")

@given("you want to create a note with note that's not an int or float")
def step_impl(context):
    context.note = "4.5"

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with("Maths", 4.5)

@given("you want to create a note with note less than 2")
def step_impl(context):
    context.note = 1

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with("Maths", context.note)

@given("you want to create a note with note bigger than 6")
def step_impl(context):
    context.note = 7

@then("it won't work")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with(context.note_name, 4)

@given("you want to create a note with note between 2 and 6")
def step_impl(context):
    context.note = 5

@then("it will work")
def step_impl(context):
    assert_that(Note("Maths", context.note).get_note()).is_equal_to(5)

