from contract import Contract
from datetime import datetime


class Player(Contract):
    def __init__(self):
        self.contract_expiration = datetime(2019, 5, 20)

    def is_available(self):
        today = datetime.today()
        return self.contract_expiration < today
