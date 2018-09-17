import unittest
import unittest.mock
import pyramid.testing


class AccountControllerTests(unittest.TestCase):

    def test_register_validation_no_email(self):
        # Arrange
        from nflpool.viewmodels.register_viewmodel import RegisterViewModel
        request = pyramid.testing.DummyRequest()
        request.POST = {
            'first_name': 'Paul',
            'last_name': 'Cutler',
            'email': 'paul.r.cutler@gmail.com',
            'password': '',
            'confirm_password': ''
        }
        # noinspection PyTypeChecker
        vm = RegisterViewModel(request)

        # Act
        vm.validate()

        # Assert:
        self.assertIsNotNone(vm.error)
        self.assertTrue('password' in vm.error)
