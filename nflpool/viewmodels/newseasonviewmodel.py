from nflpool.viewmodels.viewmodelbase import ViewModelBase


class NewSeasonViewModel(ViewModelBase):
    def __init__(self):
        self.new_season_input = None

    def from_dict(self, data_dict):
        self.new_season_input = data_dict.get('new_season_input')

