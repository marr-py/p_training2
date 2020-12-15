from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_contact_no_group(self, contact):
        # fill contact form
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # add note
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("test notes 1")
        # submit contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion in pop-up
        wd.switch_to_alert().accept()

    '''def change_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # edit first row of contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("YYYYYYYY")
        wd.find_element_by_name("update").click()'''

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        # return to home page
        self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("All e-mail")) > 0:
            wd.find_element_by_link_text("home").click()

    def contact_count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_class_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(lastname=text, id=id))
        return contacts
