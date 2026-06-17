from dataclasses import dataclass
from typing import override


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    name: str | None = None

    @override
    def __str__(self) -> str:
        return f"{
            '' if self.name is None else self.name
        }({
            self.x
        }, {
            self.y
        })"