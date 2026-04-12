from device import SmartLight, SmartThermostat, SmartLock


def operate_devices(devices):
    print("\nOperating all smart devices...")
    for device in devices:
        device.operate()


devices = []

while True:
    print("\nMenu:")
    print("1 - Add Smart Device")
    print("2 - Operate Devices")
    print("0 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Choose device type:")
        print("1 - SmartLight")
        print("2 - SmartThermostat")
        print("3 - SmartLock")

        device_choice = input("Device type: ")
        name = input("Enter device name: ")
        status = input("Enter status (on/off or active/inactive): ")

        if device_choice == "1":
            brightness = int(input("Enter brightness: "))
            device = SmartLight(name, status, brightness)
        elif device_choice == "2":
            temperature = float(input("Enter temperature: "))
            device = SmartThermostat(name, status, temperature)
        elif device_choice == "3":
            locked_input = input("Is it locked? (yes/no): ").lower()
            locked = locked_input == "yes"
            device = SmartLock(name, status, locked)
        else:
            print("Invalid device choice.")
            continue

        devices.append(device)
        print("Smart device added successfully.")

    elif choice == "2":
        if len(devices) == 0:
            print("No smart devices added yet.")
        else:
            operate_devices(devices)

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid menu choice.")