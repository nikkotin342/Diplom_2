import allure

from methods.create_order import Order
from helpers.data import *

@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Тест создать заказ с авторизацией и ингредиентами')
    def test_create_order_with_authorization_and_ingredient(self):
        response = Order().create_order_authorization(INGREDIENTS)
        assert response[0] == 200 and response[1]['order']['owner']['name'] == response[2][2]['name']

    @allure.title('Тест создать заказ без авторизации и ингредиентами')
    def test_create_order_without_authorization_and_ingredient(self):
        response = Order().create_order_not_authorization(INGREDIENTS)
        assert response[0] == 200 and response[1]['success'] is True

    @allure.title('Тест создать заказ с авторизацией без ингредиентами')
    def test_create_order_with_authorization_and_not_ingredient(self):
        response = Order().create_order_authorization(WIRHOUT_INGREDIENTS)
        assert response[0] == 400 and response[1]['success'] is False
        assert response[1]['message'] == "Ingredient ids must be provided"

    @allure.title('Тест создать заказ c авторизацией с неверным хешем ингредиентами')
    def test_create_order_with_authorization_and_incorrect_hash_ingredient(self):
        response = Order().create_order_authorization(INCORRECT_HASH_INGREDIENTS)
        assert response == 500