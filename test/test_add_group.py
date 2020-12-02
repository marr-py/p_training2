# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize

def test_add_group3b(app):
    old_groups = app.group.get_group_list()
    group = Group(groupname="Grupa nr 19", grouphead1="naglowek nr 19", groupfooter1="stopka nr 19")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(old_groups)
    old_groups.append(group)
        def id_or_max(gr):
            if gr.id:
                return gr.id
            else:
                return maxsize
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname=" ", grouphead1="", groupfooter1=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



