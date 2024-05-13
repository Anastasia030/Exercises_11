class AirConditioning:
    """
    Represents an air conditioning unit.
    """
    def __init__(self):
        """
        Initializes an instance of the AirConditioning class.
        """
        self.__status = False
        self.__temperature = None

    @property
    def status(self):
        """
        Gets the status of the air conditioning unit.

        :return: bool, The status of the air conditioning unit (True for on, False for off).
        """
        return self.__status

    @status.setter
    def status(self, condition):
        """
        Sets the status of the air conditioning unit.

        :param condition: bool, The status to set.
        """
        self.__status = self.__status

    @status.getter
    def status(self):
        """
        Gets the status of the air conditioning unit.

        :return: bool, The status of the air conditioning unit.
        """
        return self.__status

    @property
    def temperature(self):
        """
        Gets the temperature set on the air conditioning unit.

        :return: int, The temperature set on the air conditioning unit.
        """
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        """
        Sets the temperature on the air conditioning unit.

        :param value: int, The temperature to set.
        """
        self.__temperature = self.__temperature

    @temperature.getter
    def temperature(self):
        """
        Gets the current temperature if the air conditioning unit is on.

        :return: int, The current temperature of the air conditioning unit if it is on, None otherwise.
        """
        if self.__status:
            return self.__temperature

    def switch_on(self):
        """
        Turns on the air conditioning unit and sets the temperature to 18°C.
        """
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        """
        Turns off the air conditioning unit.
        """
        self.__status = False

    def reset(self):
        """
        Resets the air conditioning unit to its default state (off, temperature set to 18°C).
        """
        self.__status = False
        self.__temperature = 18

    def get_temperature(self):
        """
        Returns the current temperature if the air conditioning unit is on.

        :return: int, The current temperature of the air conditioning unit if it is on, None otherwise.
        """
        if self.__status:
            return self.__temperature

    def raise_temperature(self):
        """
        Increases the temperature by 1 degree if the air conditioning unit is on
        and the temperature is below 43°C.
        """
        if self.__status and self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        """
        Decreases the temperature by 1 degree if the air conditioning unit is on
        and the temperature is above 0°C.
        """
        if self.__status and 0 < self.__temperature:
            self.__temperature -= 1

    def __str__(self):
        """
        Returns a human-readable string representation of the air conditioning unit's status and temperature.

        :return: str, A string representation of the air conditioning unit's status and temperature.
        """
        if not self.__status:
            return 'Кондиционер выключен.'
        else:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов.'

    def __repr__(self):
        """
        Returns a string representation of the air conditioning unit for debugging purposes.

        :return: str, A string representation of the air conditioning unit.
        """
        return self.__str__()
