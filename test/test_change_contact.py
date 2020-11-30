from model.contact import Contact


def test_change_first_group(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact_no_group((Contact(firstname="Mary", middlename="Jane", nickname="MJ", lastname="Kelly",
                                                  title="director", company="Huawei", address="Test Ave. 5",
                                                  phone="1111111111", mobile="55555555", workphone="9999999",
                                                  fax="+482312312", email="mjkelly@hhhh.com")))
    app.contact.change_contact()


