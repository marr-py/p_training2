
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_contact()
    app.session.logout()

