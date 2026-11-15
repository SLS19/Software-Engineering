from abc import ABC, abstractmethod


class MonsterABC(ABC):
    """Interface for a Monster."""


    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the Monster."""
        pass


    @abstractmethod
    def get_health(self) -> int:
        """Return the current health points; returned value is positive or 0."""
        pass


    @abstractmethod
    def get_max_health(self) -> int:
        """Access the maximum value for health points. Value must be bigger than 0."""
        pass


    @abstractmethod
    def is_alive(self) -> bool:
        """Return true if the number of health points is bigger than 0."""
        pass


    @abstractmethod
    def receive_damage(self, damage: int) -> None:
        """Remove the damage from health points."""
        pass


    @abstractmethod
    def get_base_attack(self) -> int:
        """Access the base attack."""
        pass


    @abstractmethod
    def get_attack(self) -> int:
        """Access the attack value."""
        pass


    @abstractmethod
    def get_weight(self) -> float:
        """Access the weight in kg."""
        pass


    @abstractmethod
    def set_attack_multiplier(self, multiplier: float) -> None:
        """Set the scale factor for the attack value."""
        pass
