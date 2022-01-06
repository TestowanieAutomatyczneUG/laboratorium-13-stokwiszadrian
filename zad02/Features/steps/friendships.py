from zad02.friendships.Friendships import Friendships
from behave import *
from assertpy import assert_that

use_step_matcher("re")

@when("adding friendship to an empty dictionary")
def step_impl(context):
    context.friendships.addFriend("Kowal", "Kwiatkowski")

@then("person 2 will be a friend of person 1")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kowal")).contains("Kwiatkowski")

@step("not the other way around")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kwiatkowski")).is_empty()

@given("person 1 and 2 have some friends")
def step_impl(context):
    context.friendships.friendships = {"Kowal": {"Nowicka", "Bobrowski"}, "Kwiatkowski": {"Bobrowski"}}

@when("making person 2 a friend of person 1")
def step_impl(context):
    context.friendships.addFriend("Kowal", "Kwiatkowski")

@then("person 2 will be added to person 1 friendlist")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kowal")).contains("Kwiatkowski")

@then("person 1 friendlist will stay the same")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kwiatkowski")).does_not_contain("Kowal")

@when("making friends in an empty dictionary")
def step_impl(context):
    context.friendships.makeFriends("Kowalski", "Kwiatkowski")

@then("person 1 will be a friend of person 2 and vice versa")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kowalski")).contains_only("Kwiatkowski")
    assert_that(context.friendships.getFriendsList("Kwiatkowski")).contains_only("Kowalski")

@given("person 1 is a friend of person 2")
def step_impl(context):
    context.friendships.friendships = {"Kowalski": {"Kwiatkowski"}, "Kwiatkowski": set()}
    context.person2 = context.friendships.getFriendsList("Kowalski")

@when("making friends of person 1 and person 2")
def step_impl(context):
    context.friendships.makeFriends("Kowalski", "Kwiatkowski")

@then("person 2 will be a friend of person 1 but person 2 friendlist won't change")
def step_impl(context):
    assert_that(context.friendships.getFriendsList("Kwiatkowski")).contains_only("Kowalski")
    assert_that(context.friendships.getFriendsList("Kowalski")).is_equal_to(context.person2)

@when("trying to get a friendslist from an empty dict")
def step_impl(context):
    context.friendlist = context.friendships.getFriendsList("Kowalski")

@then("this person's friendlist will be an empty set")
def step_impl(context):
    assert_that(context.friendlist).is_type_of(set).is_empty()

@given("person 1 has some friends")
def step_impl(context):
    context.friendships.friendships = {"Kowalski": {"Kwiatkowska", "Nowak"}}

@when("trying to get his friendlist")
def step_impl(context):
    context.friendlist = context.friendships.getFriendsList("Kowalski")

@then("you'll get a set containing his friends")
def step_impl(context):
    assert_that(context.friendlist).is_type_of(set).contains("Kwiatkowska", "Nowak")

@given("person 2 has some friends, but not person 1")
def step_impl(context):
    context.friendships.friendships = {"Kowalski": {"Michalak", "Król"}}

@when("checking if person 1 is a friend of person 2")
def step_impl(context):
    context.check = context.friendships.areFriends("Kwiatkowski", "Kowalski")

@then("it returns false")
def step_impl(context):
    assert_that(context.check).is_false()

@given("person 2 has some friends, including person 1")
def step_impl(context):
    context.friendships.friendships = {"Kowalski": {"Michalak", "Król", "Kwiatkowski"}}

@when("checking if person 1 is a friend of person2")
def step_impl(context):
    context.check = context.friendships.areFriends("Kwiatkowski", "Kowalski")

@then("it returns true")
def step_impl(context):
    assert_that(context.check).is_true()

