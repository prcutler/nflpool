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

        if self.password != self.confirm_password:
            self.error = "The password and confirmation don't match"
            return

        if not self.password:
            self.error = "You must specify a password"
            return

        if not self.email:
            self.error = "You must specify an email address"
            return
