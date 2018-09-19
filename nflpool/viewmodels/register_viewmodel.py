from nflpool.viewmodels.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.confirm_password = None
        self.twitter = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.first_name = data_dict.get('first_name')
        self.last_name = data_dict.get('last_name')
        self.password = data_dict.get('password')
        self.twitter = data_dict.get('twitter')
        self.confirm_password = data_dict.get('confirm_password')

    def validate(self):
        self.error = None

        symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ',', '.', '<', '>'
                  '?', "/"]

        if self.password != self.confirm_password:
            self.error = "The password and confirmation don't match"
            return

        if len(self.password) <= 7:
            self.error = 'You must enter a password with at least eight characters'
            return

        if len(self.password) >= 24:
            self.error = 'Your password must be 24 characters or less'

        if not any(char in symbol for char in self.password):
            self.error = 'Your password should have at least one of the symbol (!, @, #, $, %, ^, &, *, (, ), _, -, '' \
            ''=, +, ,, <, ., >, /, ?)'

        if not any(char.isdigit() for char in self.password):
            self.error = 'Your password have at least one number'

        if not any(char.isupper() for char in self.password):
            self.error = 'Your password should have at least one uppercase letter'

        if not any(char.islower() for char in self.password):
            self.error = 'Your password should have at least one lowercase letter'

        if not self.password:
            self.error = "You must specify a password"
            return

        if not self.email:
            self.error = "You must specify an email address"
            return

