from nflpool.viewmodels.viewmodelbase import ViewModelBase


class NewSeasonViewModel(ViewModelBase):
    def __init__(self):
        self.new_season_input = None
        self.season_start_date_input = None

    def from_dict(self, data_dict):
        self.new_season_input = data_dict.get('new_season_input')
        self.season_start_date_input = data_dict.get('season_start_date_input')

