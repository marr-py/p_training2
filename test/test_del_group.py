# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="test", grouphead1="test", groupfooter1="test"))
    app.group.delete_first_group()
