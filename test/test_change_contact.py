from model.contact import Contact
from fixture.contact import Contact


def test_change_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add_contact_no_group((Contact(firstname="Mary", middlename="Jane", nickname="MJ", lastname="Kelly",
                                                  title="director", company="Huawei", address="Test Ave. 5",
                                                  phone="1111111111", mobile="55555555", workphone="9999999",
                                                  fax="+482312312", email="mjkelly@hhhh.com")))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Last name modified"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


