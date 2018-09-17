import unittest
import unittest.mock
import pyramid.testing


class AccountControllerTests(unittest.TestCase):

    def test_register_validation_valid(self):
        # 3 A's of test: Arrange, Act, then Assert

        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': 'a',
            'confirm_password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        target = 'nflpool.services.account_service.find_account_by_email'
        with unittest.mock.patch(target, return_value=None):
            vm.validate()

        # Assert:
        self.assertIsNone(vm.error)

    def test_register_validation_existing_user(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        from nflpool.data.account import Account
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        target = 'nflpool.services.account_service.find_user_by_email'
        with unittest.mock.patch(target, return_value=Account()):
            vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('exist' in vm.error)

    def test_register_validation_no_email(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': '',
            'password': 'a',
            'confirm_password': 'a'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('email' in vm.error)
