from nflpool.viewmodels.viewmodelbase import ViewModelBase


class AdminViewModel(ViewModelBase):
    def __init__(self):
        self.first_game_date = None
        self.first_game_time = None
        self.teams = None

    def from_dict(self, data_dict):
        self.first_game_date = data_dict.get("first_game_date")
        self.first_game_time = data_dict.get("first_game_time")
        self.teams = data_dict.get("teams")
