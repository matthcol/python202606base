# module movie

from dataclasses import dataclass
from typing import override

# NB: nom de classe en CamelCase : PEP 8
# https://peps.python.org/pep-0008/

@dataclass # lib standard de Python (alt: pydantic)
class Movie:
    title: str
    year: int
    duration: int | None = None

    @override # Python 3.12+ (marqueur de qualité)
    def __str__(self) -> str:
        return f"{self.title} ({self.year})"