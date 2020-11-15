# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact


def test_add_group3b(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="Grupa nr 11", grouphead1="naglowek nr 11", groupfooter1="stopka nr 11"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname=" ", grouphead1="", groupfooter1=""))
    app.session.logout()


def test_add_contact_mj(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact_no_group(Contact(firstname="Mary", middlename="Jane", nickname="MJ", lastname="Kelly", title="director", company="Huawei", address="Test Ave. 5", phone="1111111111", mobile="55555555", workphone="9999999", fax="+482312312", email="mjkelly@hhhh.com"))
    app.session.logout()


def test_add_contact_jk(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact_no_group(Contact(firstname="Jerry", middlename="K.", nickname="JUP", lastname="O'Connell", title="Snowman", company="Nokia", address="Test Ave. 1", phone="777777777", mobile="456456456", workphone="789789987798", fax="+44213111", email="oconnnell@test.com"))
    app.session.logout()
