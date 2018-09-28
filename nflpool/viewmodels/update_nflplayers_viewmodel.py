from nflpool.viewmodels.viewmodelbase import ViewModelBase


class UpdateNFLPlayersViewModel(ViewModelBase):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.player_id = None
        self.team_id = None
        self.position = None
        self.season = None

    def from_dict(self, data_dict):
        self.firstname = data_dict.get("firstname")
        self.lastname = data_dict.get("lastname")
        self.player_id = data_dict.get("player_id")
        self.team_id = data_dict.get("team_id")
        self.position = data_dict.get("position")
        self.season = data_dict.get("season")
