import allure

from methods.crate_user import User

@allure.story('Логин пользователя')
class TestCreateUser:

    @allure.title('Тест изменение данных пользователя с авторизацией')
    def test_changing_authorization_user(self):
        response = User().changing_authorization_user()
        assert response[0] == 200 and response[1]['success'] is True
        assert response[1]['user'] == {
                                'email': response[2]['email'],
                                'name': response[2]['name']
                                }

    @allure.title('Тест изменение данных пользователя без авторизацией')
    def test_changing_not_authorization_user(self):
        response = User().changing_not_authorization_user()
        assert response[0] == 401 and response[1]['success'] is False and response[1]['message'] == "You should be authorised"
