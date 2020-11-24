# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create()
    app.group.modify_first_group(Group(groupname="New, changed group name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create()
    app.group.modify_first_group(Group(grouphead1="New, changed header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create()
    app.group.modify_first_group(Group(groupfooter1="New, changed footer"))


