from nflpool.viewmodels.viewmodelbase import ViewModelBase


class NewSeasonViewModel(ViewModelBase):
    def __init__(self):
        self.current_season = None

    def from_dict(self, data_dict):
        self.current_season = data_dict.get('new_season')

