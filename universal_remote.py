from abc import ABC, abstractmethod


class UniversalRemote(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass


class BaseDevice(UniversalRemote):
    def __init__(self):
        self._is_on = False  # Track the state of the device

    def volume_up(self):
        return 'Volume increase by 10%'

    def volume_down(self):
        return 'Volume decrease by 10%'

    def is_on(self):
        return self._is_on


class TV(BaseDevice):
    def on(self):
        if not self._is_on:
            self._is_on = True
            return 'Turning on TV'
        else:
            return 'TV is already on'

    def off(self):
        if self._is_on:
            self._is_on = False
            return 'Turning off TV'
        else:
            return 'TV is already off'


class DVD(BaseDevice):
    def on(self):
        if not self._is_on:
            self._is_on = True
            return 'Turning on DVD'
        else:
            return 'DVD is already on'

    def off(self):
        if self._is_on:
            self._is_on = False
            return 'Turning off DVD'
        else:
            return 'DVD is already off'


class AC(UniversalRemote):
    def __init__(self):
        self._is_on = False  # Track the state of the AC

    def on(self):
        if not self._is_on:
            self._is_on = True
            return 'Turning on AC'
        else:
            return 'AC is already on'

    def off(self):
        if self._is_on:
            self._is_on = False
            return 'Turning off AC'
        else:
            return 'AC is already off'

    def volume_up(self):
        pass  # do nothing

    def volume_down(self):
        pass  # do nothing


def operate(device: UniversalRemote, operation: str):
    operations = {
        'on': device.on,
        'off': device.off,
        'volume_up': device.volume_up,
        'volume_down': device.volume_down
    }

    action = operations.get(operation)
    if action:
        return action()
    else:
        return "Invalid operation"


# Testing the functionality
ac = AC()
print(operate(ac, 'on'))  # Output: Turning on AC
print(operate(ac, 'on'))  # Output: AC is already on
print(operate(ac, 'off'))  # Output: Turning off AC
print(operate(ac, 'off'))  # Output: AC is already off

# dvd = DVD()
# print(operate(dvd, 'on'))  # Output: Turning on DVD
# print(operate(dvd, 'on'))  # Output: DVD is already on
# print(operate(dvd, 'volume_down'))  # Output: Volume decrease by 10%
# print(operate(dvd, 'off'))  # Output: Turning off DVD
# print(operate(dvd, 'off'))  # Output: DVD is already off
#
# tv = TV()
# print(operate(tv, 'off'))  # Output: Turning off TV
# print(operate(tv, 'on'))  # Output: Turning on TV
# print(operate(tv, 'volume_up'))  # Output: Volume increase by 10%
# print(operate(tv, 'off'))  # Output: Turning off TV
# print(operate(tv, 'off'))  # Output: TV is already off
