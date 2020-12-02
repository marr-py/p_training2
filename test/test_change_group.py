# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(groupname="New, changed group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(grouphead1="New, changed header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create()
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(groupfooter1="New, changed footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


