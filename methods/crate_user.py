import requests
import allure

from helpers.url import *
from helpers.facker import *

class User:

    @allure.step('Создать пользователя')
    def create_user(self, uniq):
        payload = {"email": new_email(),
                   "password": new_name_password(),
                   "name": new_name_password()}
        response = requests.post(f'{BASE_URL}{CREATE_USER}', data=payload)
        if uniq == True:
            return response.status_code,response.json(), payload
        else:
            response = requests.post(f'{BASE_URL}{CREATE_USER}', data=payload)
            return response.status_code,response.json(), payload

    @allure.step('Создать пользователя без данных')
    def create_user_without_data(self):
        payload = {"email": new_email(),
                   "password": '',
                   "name": new_name_password()}
        response = requests.post(f'{BASE_URL}{CREATE_USER}', data=payload)
        return response.status_code, response.json()

    @allure.step('Логин сущесвующего пользователя')
    def login_user(self):
        new_user = self.create_user(True) # создаем нового пользователя через метод create_user
        payload = {"email": new_user[2]["email"],
                   "password": new_user[2]["password"],
                   }
        response = requests.post(f'{BASE_URL}{LOGIN_USER}', data=payload)
        return response.status_code, response.json(), new_user[2]

    @allure.step('Логин сущесвующего пользователя c неверынм логином')
    def login_user_without_login(self):
        new_user = self.create_user(True)
        payload = {"email": '',
                "password": new_user[2]['password']
                }
        response = requests.post(f'{BASE_URL}{LOGIN_USER}', data=payload)
        return response.status_code, response.json()

    @allure.step('Логин сущесвующего пользователя c неверынм паролем')
    def login_user_without_password(self):
        new_user = self.create_user(True)
        payload = {"email": new_user[2]['email'],
                "password": ''
                }
        response = requests.post(f'{BASE_URL}{LOGIN_USER}', data=payload)
        return response.status_code, response.json()

    @allure.step('Изменение авторизованного пользователя')
    def changing_authorization_user(self):
        new_user = self.create_user(True)
        payload = {"email": new_email(),
                   "password": new_name_password(),
                   "name": new_name_password()}
        response = requests.patch(f"{BASE_URL}{CHANGE_USER}",
                                  headers={"Authorization": f'{new_user[1]["accessToken"]}'}, data=payload)
        return response.status_code, response.json(), payload

    @allure.step('Изменение не авторизованного пользователя')
    def changing_not_authorization_user(self):
        payload = {"email": new_email(),
                   "password": new_name_password(),
                   "name": new_name_password()}
        response = requests.patch(f"{BASE_URL}{CHANGE_USER}", data=payload)
        return response.status_code, response.json(), payload