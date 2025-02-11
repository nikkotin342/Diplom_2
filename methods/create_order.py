import requests
import allure

from helpers.url import *
from methods.crate_user import User

class Order:

    @allure.step('Создание заказа с авторизацией')
    def create_order_authorization(self, ingredients):
        new_user = User().create_user(True)
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f'{BASE_URL}{CREATE_ORDER}',headers={"Authorization": f'{new_user[1]["accessToken"]}'}, data=payload)
        if response.status_code == 500:
            return response.status_code
        else:
            return response.status_code, response.json(), new_user

    @allure.step('Создание заказа без авторизации')
    def create_order_not_authorization(self, ingredients):
        payload = {
            "ingredients": ingredients
        }
        response = requests.post(f'{BASE_URL}{CREATE_ORDER}', data=payload)
        return response.status_code, response.json()

    @allure.step('Получение заказов с авторизацией')
    def order_auth_user(self):
        new_user = User().create_user(True)
        response = requests.get(f'{BASE_URL}{GET_ORDER}',headers={"Authorization": f'{new_user[1]["accessToken"]}'})
        return response.status_code, response.json()

    @allure.step('Получение заказов без авторизации авторизацией')
    def order_not_auth_user(self):
        response = requests.get(f'{BASE_URL}{GET_ORDER}')
        return response.status_code, response.json()


