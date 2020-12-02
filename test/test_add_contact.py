# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_mj(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact_no_group(Contact(firstname="Mary", middlename="Jane", nickname="MJ", lastname="Kelly",
                                             title="director", company="Huawei", address="Test Ave. 5",
                                             phone="1111111111", mobile="55555555", workphone="9999999",
                                             fax="+482312312", email="mjkelly@hhhh.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_contact_jk(app):
    app.contact.add_contact_no_group(Contact(firstname="Jerry", middlename="K.", nickname="JUP", lastname="O'Connell",
                                             title="Snowman", company="Nokia", address="Test Ave. 1",
                                             phone="777777777", mobile="456456456", workphone="789789987798",
                                             fax="+44213111", email="oconnnell@test.com"))
