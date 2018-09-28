from nflpool.viewmodels.viewmodelbase import ViewModelBase


class UniquePicksViewModel(ViewModelBase):
    def __init__(self):
        self.season = None

    def from_dict(self, data_dict):
        self.season = data_dict.get("season")
