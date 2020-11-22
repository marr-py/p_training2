# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_mj(app):
    app.contact.add_contact_no_group(Contact(firstname="Mary", middlename="Jane", nickname="MJ", lastname="Kelly", title="director", company="Huawei", address="Test Ave. 5", phone="1111111111", mobile="55555555", workphone="9999999", fax="+482312312", email="mjkelly@hhhh.com"))


def test_add_contact_jk(app):
    app.contact.add_contact_no_group(Contact(firstname="Jerry", middlename="K.", nickname="JUP", lastname="O'Connell", title="Snowman", company="Nokia", address="Test Ave. 1", phone="777777777", mobile="456456456", workphone="789789987798", fax="+44213111", email="oconnnell@test.com"))
