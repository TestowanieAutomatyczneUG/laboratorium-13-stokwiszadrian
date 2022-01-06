from behave import *
from zad02.friendships.Friendships import Friendships


def before_scenario(context, scenario):
    context.friendships = Friendships()


def after_scenario(context, scenario):
    context.friendships = None
