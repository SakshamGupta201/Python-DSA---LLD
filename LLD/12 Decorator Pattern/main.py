from abc import abstractmethod, ABC


class ICharacter(ABC):
    @abstractmethod
    def get_ability(self) -> str:
        ...


class IDecorator(ICharacter):
    def __init__(self, character: ICharacter):
        self.character = character


class Mario(ICharacter):
    def get_ability(self) -> str:
        return "Mario"


class HeightUpDecorator(IDecorator):
    def __init__(self, character: ICharacter):
        super().__init__(character)

    def get_ability(self):
        return self.character.get_ability() + " with height Up"


class GunPowerDecorator(IDecorator):
    def __init__(self, character: ICharacter):
        super().__init__(character)

    def get_ability(self):
        return self.character.get_ability() + " with gun power"


class StarPower(IDecorator):
    def __init__(self, character: ICharacter):
        super().__init__(character)

    def get_ability(self):
        return self.character.get_ability() + " with star power (Limited time)"


ch = StarPower(HeightUpDecorator(Mario()))
print(ch.get_ability())
