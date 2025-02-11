import allure

from methods.crate_user import User

@allure.story('Создание пользователя')
class TestCreateUser:

    @allure.title('Тест создать уникального пользователя')
    def test_create_unique_user(self):
        response = User().create_user(True)
        assert response[0] == 200 and response[1]['success'] is True

    @allure.title('Негативный тест создания существующего пользователя')
    def test_create_existing_user(self):
        response = User().create_user(False)
        assert response[0] == 403 and response[1]['success'] is False and response[1]['message'] == 'User already exists'

    @allure.title('Негативный тест создания пользователя без данных')
    def test_create_user_without_data(self):
        response = User().create_user_without_data()
        assert response[0] == 403 and response[1]['success'] is False and response[1][
            'message'] == 'Email, password and name are required fields'