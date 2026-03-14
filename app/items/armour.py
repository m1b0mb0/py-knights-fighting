class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, armour: dict) -> list:
        return [Armour(a["part"], a["protection"]) for a in armour]
