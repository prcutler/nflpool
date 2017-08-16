from nflpool.viewmodels.viewmodelbase import ViewModelBase


class UpdateNFLScheduleViewModel(ViewModelBase):
    def __init__(self):
        self.game_id = None
        self.game_date = None
        self.away_team = None
        self.home_team = None
        self.week = None
        self.season = None

    def from_dict(self, data_dict):
        self.game_id = data_dict.get('game_id')
        self.game_date = data_dict.get('game_date')
        self.away_team = data_dict.get('away_team')
        self.home_team = data_dict.get('home_team')
        self.week = data_dict.get('week')
        self.season = data_dict.get('season')
