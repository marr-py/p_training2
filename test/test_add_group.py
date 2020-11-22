# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group3b(app):
    app.group.create(Group(groupname="Grupa nr 11", grouphead1="naglowek nr 11", groupfooter1="stopka nr 11"))
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(groupname=" ", grouphead1="", groupfooter1=""))



