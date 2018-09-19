import unittest
import unittest.mock
import pyramid.testing


class AccountControllerTests(unittest.TestCase):

    def test_register_validation_valid(self):
        # 3 A's of test: Arrange, Act, then Assert

        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        data = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': 'Aa123456@',
            'confirm_password': 'Aa123456@'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel()
        vm.from_dict(data)

        # Act
        target = 'nflpool.services.account_service.AccountService.find_account_by_email'
        with unittest.mock.patch(target, return_value=None):
            vm.validate()

        # Assert:
        self.assertIsNone(vm.error)

    def test_register_validation_existing_user(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        from nflpool.data.account import Account
        data = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': 'Aa123456@',
            'confirm_password': 'Aa123456@'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel()
        vm.from_dict(data)

        # Act
        target = 'nflpool.services.account_service.AccountService.find_account_by_email'
        with unittest.mock.patch(target, return_value=Account()):
            vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('exist' in vm.error)

    def test_register_validation_no_password(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel

        data = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': '',
            'confirm_password': ''
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel()
        vm.from_dict(data)

        # Act
        vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('password' in vm.error)

    def test_register_validation_no_email(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel

        data = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': '',
            'password': 'Aa123456@',
            'confirm_password': 'Aa123456@'
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel()
        vm.from_dict(data)

        # Act
        vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('email' in vm.error)