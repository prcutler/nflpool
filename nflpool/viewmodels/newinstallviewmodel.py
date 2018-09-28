from nflpool.viewmodels.viewmodelbase import ViewModelBase


class NewInstallViewModel(ViewModelBase):
    def __init__(self):
        self.team_id = None
        self.name = None
        self.city = None
        self.team_abbr = None
        self.conference = None
        self.division = None
        self.division_abbr = None
        self.division_id = None

    def from_dict(self, data_dict):
        self.team_id = data_dict.get("team_id")
        self.name = data_dict.get("name")
        self.city = data_dict.get("city")
        self.team_abbr = data_dict.get("team_abbr")
        self.conference = data_dict.get("conference")
        self.division = data_dict.get("division")
        self.division_abbr = data_dict.get("division_abbr")
        self.division_id = data_dict.get("division_id")
