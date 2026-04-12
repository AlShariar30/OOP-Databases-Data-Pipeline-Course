from device import IoTDevice, TemperatureSensor, HumiditySensor, MotionSensor


def encrypt_text(text: str) -> str:
    return "".join(chr(ord(char) + 1) for char in text)


def decrypt_text(text: str) -> str:
    return "".join(chr(ord(char) - 1) for char in text)


devices = []
filename = "iot_data.csv"
encrypted_filename = "iot_data_encrypted.txt"

while True:
    print("\nMenu:")
    print("1 - Add IoT Device")
    print("2 - Serialize Data")
    print("3 - Deserialize Data")
    print("4 - Encrypt Data")
    print("5 - Decrypt Data")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Choose device type:")
        print("1 - TemperatureSensor")
        print("2 - HumiditySensor")
        print("3 - MotionSensor")

        device_choice = input("Device type: ")
        deviceId = input("Enter device ID: ")
        location = input("Enter location: ")
        data = float(input("Enter data value: "))

        if device_choice == "1":
            device = TemperatureSensor(deviceId, location, data)
        elif device_choice == "2":
            device = HumiditySensor(deviceId, location, data)
        elif device_choice == "3":
            device = MotionSensor(deviceId, location, data)
        else:
            print("Invalid device choice")
            continue

        devices.append(device)
        print("Device added successfully.")

    elif choice == "2":
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for device in devices:
                    file.write(device.serialize() + "\n")
            print("Data serialized to file successfully.")
        except Exception as e:
            print(f"Error while serializing: {e}")

    elif choice == "3":
        try:
            devices.clear()
            with open(filename, "r", encoding="utf-8") as file:
                for row in file:
                    device = IoTDevice.deserialize(row)
                    devices.append(device)
            print("Data deserialized successfully.")
            for device in devices:
                print(device.serialize())
        except Exception as e:
            print(f"Error while deserializing: {e}")

    elif choice == "4":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
            encrypted_content = encrypt_text(content)
            with open(encrypted_filename, "w", encoding="utf-8") as file:
                file.write(encrypted_content)
            print("Data encrypted successfully.")
        except Exception as e:
            print(f"Error while encrypting: {e}")

    elif choice == "5":
        try:
            with open(encrypted_filename, "r", encoding="utf-8") as file:
                encrypted_content = file.read()
            decrypted_content = decrypt_text(encrypted_content)
            print("Decrypted data:")
            print(decrypted_content)
        except Exception as e:
            print(f"Error while decrypting: {e}")

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid menu choice.")