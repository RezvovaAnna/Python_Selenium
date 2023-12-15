from testpage import OperationsHelper
import logging
import yaml
import random
import string

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('Test 2 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['name'])
    testpage.enter_pass(testdata['passwd'])
    testpage.click_login_button()
    assert testpage.get_result_auth() == "Blog"


def test_step3(browser):
    logging.info('Test 3 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_create_post_button()
    tittle = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    testpage.create_tittle_post(tittle)
    testpage.create_description_post(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
    testpage.create_content_post(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
    testpage.click_button_save_post()
    assert testpage.get_result_public_post() == tittle


def test_step4(browser):
    logging.info('Test 4 starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact()
    testpage.enter_name_to_contact_us('Test')
    testpage.enter_email_to_contact_us('sdff@mail.ru')
    testpage.enter_content_to_contact_us('Проверка')
    testpage.click_contact_us_btn()
    assert testpage.checkout_alert() == 'Form successfully submitted'


def test_step5(browser):
    logging.info('Test 5 starting')
    testpage = OperationsHelper(browser)
    testpage.log_out()
    assert testpage.get_result_login_out() == 'LOGIN'
