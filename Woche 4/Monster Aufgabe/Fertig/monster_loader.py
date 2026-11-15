# import necessary modules if needed

from typing import List
from monster import Monster


class MonsterLoader:
    @staticmethod
    def load_monster_file(file_path: str) -> List[Monster]:
        """Load the monsters from the given file. If something is wrong with a monster, it is not loaded."""
        """ The loading process continues with the next monster. """
        monsters: List[Monster] = []
        keys = ["name", "maxHP", "attack", "weight", "multi"]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = [raw.strip() for raw in f if raw.strip()]
        except Exception:
            return monsters

        i = 0
        while i < len(lines):
            if lines[i] != "Monster":
                i += 1
                continue
            i += 1
            block = lines[i:i + 5]
            try:
                if len(block) != 5:
                    continue
                values = []
                for key, line in zip(keys, block):
                    parts = line.split(" ", 1)
                    if parts[0] != key or len(parts) < 2 or not parts[1].strip():
                        raise ValueError
                    values.append(parts[1].strip())
                monsters.append(
                    Monster(values[0], int(values[1]), float(values[3]),
                            int(values[2]), float(values[4]))
                )
                i += 5
            except Exception:
                pass
        return monsters


if __name__ == "__main__":
    for fn in ("monster_ok.txt", "monster_fail.txt"):
        res = MonsterLoader.load_monster_file(fn)
        print(fn, [m.get_name() for m in res])
