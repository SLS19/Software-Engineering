# class Monster
# author: Thomas Wilde
# This file is for private use only.
from monster_abc import MonsterABC


class Monster(MonsterABC):
    def __init__(
        self,
        name: str,
        max_health: int,
        weight: float,
        base_atk: int,
        multiplier: float,
    ):
        # Initialize final members (in Python, we use naming conventions)
        self.name = name
        self.max_health = max(1, max_health)
        self.weight = max(0.1, weight)

        # Initialize other members
        self.health = self.max_health
        self.base_atk = base_atk
        self.atk_multiplier = multiplier
        self._cap_multiplier()

    def _cap_multiplier(self) -> None:
        if self.atk_multiplier < -2.0:
            self.atk_multiplier = -2.0
        if self.atk_multiplier > 5.0:
            self.atk_multiplier = 5.0

    def _clip_health(self) -> None:
        if self.health < 0:
            self.health = 0
        if self.health > self.max_health:
            self.health = self.max_health

    def get_name(self) -> str:
        return self.name

    def get_health(self) -> int:
        return self.health

    def get_max_health(self) -> int:
        return self.max_health

    def is_alive(self) -> bool:
        return self.health > 0

    def receive_damage(self, damage: int) -> None:
        if self.weight > 13.37:
            reduction = int(damage * 0.2)
            damage -= reduction
        self.health -= damage
        self._clip_health()

    def get_base_attack(self) -> int:
        return self.base_atk

    def get_attack(self) -> int:
        return int(self.base_atk * self.atk_multiplier)

    def get_weight(self) -> float:
        return self.weight

    def set_attack_multiplier(self, multiplier: float) -> None:
        self.atk_multiplier = multiplier
        self._cap_multiplier()

    def __str__(self) -> str:
        return f"""Name:   {self.name}
maxHP:  {self.max_health}
HP:     {self.health}
attack: {self.base_atk}
weight: {self.weight}
multi:  {self.atk_multiplier}"""
