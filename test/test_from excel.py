from selenium import webdriver
import pytest
from openpyxl import *


@pytest.fixture(scope="session")
def app(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(0)
    def destroy():
        wd.quit()
    request.addfinalizer(destroy)
    return wd


def test_email_login(app):

    wb = load_workbook(filename="C:\\Reposit\\soft_sob\\user_pass.xlsx")
    ws = wb['Лист1']
    row_number = 1
    for row in ws.rows:
        app.get('https://www.addressbook.net/cgi-bin/WebObjects/AddressBook.woa/wa/UserAction/login')


        app.find_element_by_name("user").send_keys(row[1].value)

        app.find_element_by_name("pass").send_keys(row[2].value)
        app.find_element_by_css_selector('input[type="submit"]').click()
        # applic.find_element_by_id('login').send_keys(row[0].value)
        # applic.find_element_by_id('password').send_keys(row[1].value)
        # applic.find_element_by_id('loginSubmit').click()
        ws['C' + str(row_number)] = "okay"


        wb.save(filename="C:\\Reposit\\soft_sob\\data_resssult.xlsx")
        row_number += 1