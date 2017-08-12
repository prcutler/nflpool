from nflpool.viewmodels.viewmodelbase import ViewModelBase


class PlayerPicksViewModel(ViewModelBase):
    def __init__(self):
        self.pick_name = None
        self.pick_id = None

    def from_dict(self, data_dict):
        self.pick_name = data_dict.get('pick_name')
        self.pick_id = data_dict.get('pick_id')


