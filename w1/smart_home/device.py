class SmartDevice:
    def __init__(self, deviceName: str, status: str):
        self.deviceName = deviceName
        self.status = status

    def operate(self):
        print(f"{self.deviceName} is operating.")


class SmartLight(SmartDevice):
    def __init__(self, deviceName: str, status: str, brightness: int):
        super().__init__(deviceName, status)
        self.brightness = brightness

    def operate(self):
        print(f"{self.deviceName} light is {self.status} with brightness {self.brightness}%.")


class SmartThermostat(SmartDevice):
    def __init__(self, deviceName: str, status: str, temperature: float):
        super().__init__(deviceName, status)
        self.temperature = temperature

    def operate(self):
        print(f"{self.deviceName} thermostat is {self.status} at {self.temperature}C.")


class SmartLock(SmartDevice):
    def __init__(self, deviceName: str, status: str, locked: bool):
        super().__init__(deviceName, status)
        self.locked = locked

    def operate(self):
        lock_status = "locked" if self.locked else "unlocked"
        print(f"{self.deviceName} lock is {self.status} and currently {lock_status}.")