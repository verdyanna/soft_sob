from selenium import webdriver
import pytest
from openpyxl import load_workbook
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture()
def app(request):
    wd = webdriver.Chrome()
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
        app.find_element_by_id('login').send_keys(row[1].value)
        app.find_element_by_id('password').send_keys(row[1].value)
        app.find_element_by_id('loginSubmit').click()
        wb.save(filename="C:\\Reposit\\soft_sob\\data_result.xlsx")
        row_number += 1

def ensure_logout(self):
    if len(app.find_elements_by_link_text("logout"))>0:
        self.logout()
    else:
        self.registr()

def logout(self):
    app.find_element_by_id(".//*[@id='logoutlink").click()

def registr():
    app.get('http://www.addressbook.net/cgi-bin/WebObjects/AddressBook.woa/wa/UserAction/registerUser')

def ensure_login(self,username,password):
    if self.is_log_in:
        if self.is_log_in_as(username):
            return
        else:
            self.logout()
    self.login(username, password)



def is_log_in(self):
    pass

def login(self):
    pass


def is_log_in_as(self, username):
    wd = self.app.wd
    return wd.find_element_by_xpath(".//*[@id='logoutlink']").text









