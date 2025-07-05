from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...


class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")


class LightCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.commands: list[ICommand] = []

    def set_command(self, command: ICommand):
        self.commands.append(command)

    def press_button(self, index: int):
        if 0 <= index < len(self.commands):
            self.commands[index].execute()
        else:
            print("Invalid command index")

    def press_undo(self, index: int):
        if 0 <= index < len(self.commands):
            self.commands[index].undo()
        else:
            print("Invalid command index")


if __name__ == "__main__":
    light = Light()
    light_command = LightCommand(light)

    remote = RemoteControl()
    remote.set_command(light_command)

    remote.press_button(0)
    remote.press_undo(0)
