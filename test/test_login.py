from openpyxl import load_workbook


def test_login(app):
    app.session.login_from_excel()
    assert app.session.is_logged_in_as("admin")