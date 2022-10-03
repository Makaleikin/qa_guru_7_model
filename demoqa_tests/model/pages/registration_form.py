import os
from typing import Tuple

from selene import have, command, by
from selene.support.shared import browser

from demoqa_tests.model.contols import datepicker, dropdown, modal
from tests.test_data.user_data import Subject


def given_opened():
    browser.open('/automation-practice-form')


def set_first_name(first_name: str):
    browser.element('#firstName').type(first_name)


def set_last_name(last_name: str):
    browser.element('#lastName').type(last_name)


def set_email(email: str):
    browser.element('#userEmail').type(email)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender.value)).first.click()


def set_phone_number(user_number: str):
    browser.element('#userNumber').type(user_number)


def set_date_of_birth(birth_day, birth_month, birth_year):
    datepicker.select_date(birth_day, birth_month, birth_year)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def add_hobbie_sport():
    browser.element('[for="hobbies-checkbox-1"][class="custom-control-label"]').click()


def upload_picture(picture_file: str):
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture_file))


def set_current_address(current_address: str):
    browser.element('#currentAddress').type(current_address)


def set_state(value: str):
    dropdown.select(browser.element('#state'), value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def submit_form():
    browser.element('#submit').click()


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))