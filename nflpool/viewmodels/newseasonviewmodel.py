from nflpool.viewmodels.viewmodelbase import ViewModelBase


class NewSeasonViewModel(ViewModelBase):
    def __init__(self):
        self.new_season_input = None
        self.season_start_date_input = None
        self.season_start_time = None
        self.home_team = None
        self.away_team = None

    def from_dict(self, data_dict):
        self.new_season_input = data_dict.get('new_season_input')
        self.season_start_date_input = data_dict.get('season_start_date_input')
        self.season_start_time = data_dict.get('season_start_time')
        self.home_team = data_dict.get('home_team')
        self.away_team = data_dict.get('away_team')

