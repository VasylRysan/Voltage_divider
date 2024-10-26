from devices.srs_e24 import e24


class Resistor:
    def __init__(self, resistance: float) -> None:
        self.resistance = resistance

        if self.resistance not in e24:
            self.resistance = min(
                e24, key=lambda res: abs(self.resistance - res)
            )
