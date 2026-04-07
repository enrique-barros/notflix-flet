"""
Capítulo 4 — Modelo de datos.

Definimos un dataclass `Movie` que representa una fila del CSV,
y una función `load_movies()` que lee el archivo y devuelve
una lista de instancias `Movie`.

Conceptos clave:
- `dataclass`: estructura limpia para representar datos.
- `csv.DictReader`: leer CSV como diccionarios fila por fila.
- Función de carga separada del resto de la app (principio de responsabilidad única).
"""

import csv
from dataclasses import dataclass, field
from pathlib import Path

# Ruta al CSV, relativa a este módulo
DATA_PATH = Path(__file__).parent.parent / "data" / "netflix_titles.csv"


@dataclass
class Movie:
    """Representa un título de Netflix extraído del CSV."""

    show_id: str
    type: str          # "Movie" | "TV Show"
    title: str
    director: str
    cast: str
    country: str
    date_added: str
    release_year: str
    rating: str
    duration: str
    listed_in: str     # géneros separados por coma
    description: str

    @property
    def genres(self) -> list[str]:
        """Devuelve la lista de géneros como strings limpios."""
        return [g.strip() for g in self.listed_in.split(",") if g.strip()]


def load_movies(path: Path = DATA_PATH) -> list[Movie]:
    """
    Lee el CSV y devuelve una lista de objetos Movie.

    Omite filas con campos esenciales vacíos (title, type).
    """
    movies: list[Movie] = []

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row.get("title", "").strip()
            type_ = row.get("type", "").strip()

            # Saltamos filas sin título ni tipo
            if not title or not type_:
                continue

            movies.append(
                Movie(
                    show_id=row.get("show_id", ""),
                    type=type_,
                    title=title,
                    director=row.get("director", ""),
                    cast=row.get("cast", ""),
                    country=row.get("country", ""),
                    date_added=row.get("date_added", ""),
                    release_year=row.get("release_year", ""),
                    rating=row.get("rating", ""),
                    duration=row.get("duration", ""),
                    listed_in=row.get("listed_in", ""),
                    description=row.get("description", ""),
                )
            )

    return movies
