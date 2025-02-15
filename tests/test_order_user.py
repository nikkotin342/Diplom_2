import allure

from methods.create_order import Order
from helpers.data import *

@allure.story('Получение заказов конкретного пользователя')
class TestCreateOrder:

    @allure.title('Тест заказы авторизованного пользователя')
    def test_order_auth_user(self):
        response = Order().order_auth_user()
        assert response[0] == 200 and response[1]['success'] is True

    @allure.title('Тест заказы не авторизованного пользователя')
    def test_order_not_auth_user(self):
        response = Order().order_not_auth_user()
        assert response[0] == 401 and response[1]['success'] is False
        assert response[1]['message'] == "You should be authorised"