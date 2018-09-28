from nflpool.viewmodels.viewmodelbase import ViewModelBase


class UpdateWeeklyStats(ViewModelBase):
    def __init__(self):
        self.player_id = None
        self.passyds = None
        self.rushyds = None
        self.recyds = None
        self.sacks = None
        self.interceptions = None
        self.week = None
        self.season = None

    def from_dict(self, data_dict):
        self.player_id = data_dict.get("player_id")
        self.passyds = data_dict.get("passyds")
        self.rushyds = data_dict.get("rushyds")
        self.recyds = data_dict.get("recyds")
        self.sacks = data_dict.get("sacks")
        self.interceptions = data_dict.get("interceptions")
        self.week = data_dict.get("week")
        self.season = data_dict.get("season")
