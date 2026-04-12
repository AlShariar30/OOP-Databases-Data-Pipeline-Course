class IoTDevice:
    def __init__(self, deviceId: str, location: str, data: float):
        self.deviceId = deviceId
        self.location = location
        self.data = data

    def serialize(self) -> str:
        return f"{self.__class__.__name__},{self.deviceId},{self.location},{self.data}"

    @staticmethod
    def deserialize(row: str):
        parts = row.strip().split(",")
        if len(parts) != 4:
            raise ValueError("Invalid row format")

        device_type, deviceId, location, data = parts
        data = float(data)

        if device_type == "TemperatureSensor":
            return TemperatureSensor(deviceId, location, data)
        elif device_type == "HumiditySensor":
            return HumiditySensor(deviceId, location, data)
        elif device_type == "MotionSensor":
            return MotionSensor(deviceId, location, data)
        else:
            raise ValueError("Unknown device type")


class TemperatureSensor(IoTDevice):
    pass


class HumiditySensor(IoTDevice):
    pass


class MotionSensor(IoTDevice):
    pass