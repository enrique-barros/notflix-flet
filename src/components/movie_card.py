import flet as ft

from config.theme import ( COLOR_PRIMARY, COLOR_SUBTEXT,
    COLOR_TEXT, FONT_SIZE_CARD_META, FONT_SIZE_CARD_TITLE, RADIUS_CARD,)
from data.movie_model import Movie

# Paleta de gradientes para simular pósters (asignados por hash del título)
_POSTER_GRADIENTS = [
    ["#0f0c29", "#302b63", "#24243e"],
    ["#1a1a2e", "#16213e", "#0f3460"],
    ["#2d1b69", "#11998e", "#38ef7d"],
    ["#fc4a1a", "#f7b733", "#2c3e50"],
    ["#0f2027", "#203a43", "#2c5364"],
    ["#16222a", "#3a6073", "#16222a"],
    ["#3c1053", "#ad5389", "#3c1053"],
    ["#134e5e", "#71b280", "#134e5e"],
    ["#1f4037", "#99f2c8", "#1f4037"],
    ["#870000", "#190a05", "#870000"],
    ["#005c97", "#363795", "#005c97"],
    ["#4b6cb7", "#182848", "#4b6cb7"],
]


def _poster_gradient(title: str) -> list[str]:
    idx = hash(title) % len(_POSTER_GRADIENTS)
    return _POSTER_GRADIENTS[idx]


def _genre_chip(genre: str) -> ft.Container:
    return ft.Container(
        bgcolor=ft.Colors.with_opacity(0.25, "white"),
        padding=ft.Padding(5, 2, 5, 2),
        border_radius=ft.BorderRadius(3, 3, 3, 3),
        content=ft.Text(genre, size=9, color=COLOR_TEXT),
    )


def build_movie_card(movie: Movie, width: float = 180) -> ft.Container:
    height = width * 1.5          # ratio 2:3 tipo póster
    type_color = COLOR_PRIMARY if movie.type == "Movie" else "#0070f3"
    grad_colors = _poster_gradient(movie.title)

    # ── Póster simulado ───────────────────────────────────────
    poster = ft.Container(
        width=width,
        height=height,
        border_radius=RADIUS_CARD,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=grad_colors,
        ),
        content=ft.Stack(
            controls=[
                # Icono central decorativo
                ft.Container(
                    alignment=ft.Alignment(0, -0.2),
                    content=ft.Icon(
                        ft.Icons.MOVIE_OUTLINED if movie.type == "Movie"
                        else ft.Icons.TV_OUTLINED,
                        color=ft.Colors.with_opacity(0.25, "white"),
                        size=48,
                    ),
                ),
                # Overlay inferior con info
                ft.Container(
                    alignment=ft.Alignment(0, 1),
                    width=width,
                    height=height,
                    content=ft.Container(
                        width=width,
                        padding=ft.Padding(8, 8, 8, 8),
                        gradient=ft.LinearGradient(
                            begin=ft.Alignment(0, -1),
                            end=ft.Alignment(0, 1),
                            colors=[
                                ft.Colors.with_opacity(0, "black"),
                                ft.Colors.with_opacity(0.85, "black"),
                            ],
                        ),
                        content=ft.Column(
                            spacing=3,
                            controls=[
                                # Badge tipo
                                ft.Container(
                                    bgcolor=ft.Colors.with_opacity(0.9, type_color),
                                    padding=ft.Padding(4, 1, 4, 1),
                                    border_radius=ft.BorderRadius(3, 3, 3, 3),
                                    content=ft.Text(
                                        movie.type,
                                        size=9,
                                        color="white",
                                        weight=ft.FontWeight.W_700,
                                    ),
                                ),
                                ft.Text(
                                    movie.title,
                                    size=FONT_SIZE_CARD_TITLE,
                                    color=COLOR_TEXT,
                                    weight=ft.FontWeight.BOLD,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                                ft.Text(
                                    f"{movie.release_year}  ·  {movie.rating}",
                                    size=FONT_SIZE_CARD_META,
                                    color=COLOR_SUBTEXT,
                                ),
                                ft.Row(
                                    spacing=3,
                                    wrap=True,
                                    controls=[_genre_chip(g) for g in movie.genres[:2]],
                                ),
                            ],
                        ),
                    ),
                ),
            ],
        ),
    )

    return poster
