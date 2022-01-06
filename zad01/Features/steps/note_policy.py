from zad01.notes.Note import Note
from behave import *
from assertpy import assert_that

use_step_matcher("re")

@when("you want to create a note with name none")
def step_impl(context):
    context.note_name = None

@then("Note with a None value for a name won't be created")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with(context.note_name, 4)

@when("you want to create a note with empty name")
def step_impl(context):
    context.note_name = ""

@then("Note with an empty name won't be created")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with(context.note_name, 4)

@when("you want to create a note with a name that's not a string")
def step_impl(context):
    context.note_name = 123

@then("Note with a name that's not a string won't be created")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with(context.note_name, 4)

@when("you want to create a note with a name that's a string")
def step_impl(context):
    context.note_name = "Maths"

@then("Note with given string will be created")
def step_impl(context):
    assert_that(Note(context.note_name, 4).get_name()).is_equal_to("Maths")

@When("you want to create a note with note that's not an int or float")
def step_impl(context):
    context.note = "4.5"

@then("Note with NaN note won't be created")
def step_impl(context):
    assert_that(Note).raises(TypeError).when_called_with("Maths", context.note)

@when("you want to create a note with note smaller than 2")
def step_impl(context):
    context.note = 1

@then("Note with a note smaller than 2 won't be created")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with("Maths", context.note)

@when("you want to create a note with note bigger than 6")
def step_impl(context):
    context.note = 7

@then("Note with a note bigger than 6 won't be created")
def step_impl(context):
    assert_that(Note).raises(ValueError).when_called_with("Maths", context.note)

@when("you want to create a note with note between 2 and 6")
def step_impl(context):
    context.note = 5

@then("Note with given note will be created")
def step_impl(context):
    assert_that(Note("Maths", context.note).get_note()).is_equal_to(5)

