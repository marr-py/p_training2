# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group3b(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname="Grupa nr 17", grouphead1="naglowek nr 11", groupfooter1="stopka nr 11"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname=" ", grouphead1="", groupfooter1=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



