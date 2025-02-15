import allure

from methods.crate_user import User

@allure.story('Логин пользователя')
class TestCreateUser:

    @allure.title('Тест логин существующего пользователя')
    def test_login_user(self):
        response = User().login_user()
        assert response[0] == 200 and response[1]['success'] is True
        assert response[1]['user'] == {'email': response[2]['email'],
                                       'name': response[2]['name']}

    @allure.title('Негативный тест логина пользователя с неверным логином')
    def test_login_without_email(self):
        response = User().login_user_without_login()
        assert response[0] == 401 and response[1]['success'] is False and response[1]['message'] == 'email or password are incorrect'

    @allure.title('Негативный тест логина пользователя с неверным паролем')
    def test_login_without_password(self):
        response = User().login_user_without_password()
        assert response[0] == 401 and response[1]['success'] is False and response[1]['message'] == 'email or password are incorrect'