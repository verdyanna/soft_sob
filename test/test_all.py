from selenium import webdriver
import pytest
from openpyxl import load_workbook
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def app(request):
    wd = webdriver.Chrome()
    #wd.get('https://www.addressbook.net/cgi-bin/WebObjects/AddressBook.woa/wa/UserAction/login')
    def destroy():
        wd.close()
    request.addfinalizer(destroy)
    return wd


def test_mail_in(app):
    wb = load_workbook(filename='C:\\Reposit\\soft_sob\\book1.xlsx')
    ws = wb['Sheet1']
    row_number = 1
    for row in ws.rows:

        app.get('https://www.addressbook.net/cgi-bin/WebObjects/AddressBook.woa/wa/UserAction/login')
        app.find_element_by_id('login').send_keys(row[0].value)
        app.find_element_by_id('password').send_keys(row[1].value)
        app.find_element_by_id('loginSubmit').click()

        wb.save(filename="C:\\Reposit\\soft_sob\\data_result.xlsx")
        row_number += 1





