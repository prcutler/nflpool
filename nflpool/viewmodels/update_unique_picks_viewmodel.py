from nflpool.viewmodels.viewmodelbase import ViewModelBase


class UniquePicksViewModel(ViewModelBase):
    def __init__(self):
        self.picks = None

    def from_dict(self, data_dict):
        self.picks = data_dict.get('picks')
