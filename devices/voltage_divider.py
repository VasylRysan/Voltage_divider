from devices.resistor import Resistor


class VoltageDivider:
    def __init__(
            self,
            input_voltage: float,
            output_voltage: float,
            max_current: float,
    ) -> None:
        self.input_voltage = input_voltage
        self.output_voltage = output_voltage
        self.max_current = max_current

    def get_standard_resistors(self) -> None:

        """ This function calculates the values of resistances
            R1 and R2 according to input values,
            input voltage and output voltage:
            .........................
            .                       .
            .                       R1
              +                     .
            V input                 .................  +
              -                     .
            .                       R2              V output
            .                       .
            .........................................  -

        """

        r2 = round(self.output_voltage / self.max_current, 2)
        r2 = Resistor(r2)
        r1 = (r2.resistance * self.input_voltage / self.output_voltage) - r2.resistance
        r1 = Resistor(r1)
        print(
            f"Standard R1 E24 resistor value: {r1.resistance} \n"
            f"Standard R2 E24 resistor value: {r2.resistance}"
        )
