from nflpool.viewmodels.viewmodelbase import ViewModelBase


class AdminViewModel(ViewModelBase):
    def __init__(self):
        self.user_id = None
        self.is_super_user = None

    def from_dict(self, data_dict):
        self.user_id = data_dict.get("user_id")
        self.is_super_user = data_dict.get("is_super_user")
