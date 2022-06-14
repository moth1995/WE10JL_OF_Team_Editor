from .stat import Stat


class EditedFlags:
    def __init__(self, player):
        nameEdited = Stat(player, 3, 0, 1, "");
        callEdited = Stat(player, 3, 2, 1, "");
        shirtEdited = Stat(player, 3, 1, 1, "");
        abilityEdited = Stat(player, 40, 4, 1, "");
        
    def __iter__(self):
        """
        Returns an iterable object with all class attributes

        Returns:
            any: iterable object with all class attributes
        """
        keys = list(self.__dict__.keys())
        values =list(self.__dict__.values())
        return iter([values[i] for i in range(len(keys)) if not keys[i].startswith('__')])
    
    def __call__(self):
        return [appearance() for appearance in self.__iter__()]



