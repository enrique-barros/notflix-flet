import flet as ft

from config.theme import COLOR_PRIMARY, COLOR_SUBTEXT, COLOR_TEXT
from data.movie_model import Movie

_HERO_GRADIENTS = [
    ["#0d0d0d", "#1a0533", "#2d1b69"],
    ["#0d0d0d", "#0f2027", "#2c5364"],
    ["#0d0d0d", "#1f1c2c", "#928dab"],
    ["#0d0d0d", "#1a1a2e", "#16213e"],
    ["#0d0d0d", "#16222a", "#3a6073"],
    ["#0d0d0d", "#134e5e", "#71b280"],
]


def _hero_gradient(title: str) -> list[str]:
    return _HERO_GRADIENTS[hash(title) % len(_HERO_GRADIENTS)]


def _pill(text: str) -> ft.Container:
    return ft.Container(
        bgcolor=ft.Colors.with_opacity(0.2, "white"),
        border_radius=ft.BorderRadius(4, 4, 4, 4),
        padding=ft.Padding(8, 3, 8, 3),
        content=ft.Text(text, size=11, color=COLOR_TEXT, weight=ft.FontWeight.W_500),
    )


def build_hero_banner(movie: Movie, on_ver_detalle) -> ft.Container:
    desc = movie.description[:160] + "…" if len(movie.description) > 160 else movie.description

    # Metadatos en pills
    meta_pills = ft.Row(
        spacing=6,
        wrap=True,
        controls=[
            _pill(str(movie.release_year)),
            _pill(movie.rating or "NR"),
            _pill(movie.duration or "—"),
        ],
    )

    # Géneros en texto sutil
    genres_text = ft.Text(
        "  ·  ".join(movie.genres[:3]),
        size=12,
        color=COLOR_SUBTEXT,
    )

    # Botones — ft.Button es la API actual en 0.80+
    btn_play = ft.Container(
        bgcolor=COLOR_TEXT,
        border_radius=ft.BorderRadius(4, 4, 4, 4),
        padding=ft.Padding(20, 10, 20, 10),
        on_click=on_ver_detalle,
        ink=True,
        content=ft.Row(
            spacing=6,
            tight=True,
            controls=[
                ft.Icon(ft.Icons.PLAY_ARROW_ROUNDED, color="black", size=20),
                ft.Text("Reproducir", color="black", weight=ft.FontWeight.BOLD, size=14),
            ],
        ),
    )

    btn_info = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.3, "white"),
        border_radius=ft.BorderRadius(4, 4, 4, 4),
        padding=ft.Padding(20, 10, 20, 10),
        on_click=on_ver_detalle,
        ink=True,
        content=ft.Row(
            spacing=6,
            tight=True,
            controls=[
                ft.Icon(ft.Icons.INFO_OUTLINE_ROUNDED, color="white", size=20),
                ft.Text("Más info", color="white", weight=ft.FontWeight.W_500, size=14),
            ],
        ),
    )

    content_layer = ft.Column(
        spacing=14,
        controls=[
            # Badge tipo
            ft.Container(
                bgcolor=ft.Colors.with_opacity(0.85, COLOR_PRIMARY),
                border_radius=ft.BorderRadius(3, 3, 3, 3),
                padding=ft.Padding(8, 3, 8, 3),
                content=ft.Text(
                    movie.type.upper(),
                    size=10,
                    color="white",
                    weight=ft.FontWeight.W_700,
                ),
            ),
            # Título grande
            ft.Text(
                movie.title,
                size=32,
                color=COLOR_TEXT,
                weight=ft.FontWeight.BOLD,
                max_lines=2,
                overflow=ft.TextOverflow.ELLIPSIS,
            ),
            meta_pills,
            genres_text,
            ft.Text(
                desc,
                size=13,
                color=ft.Colors.with_opacity(0.8, "white"),
                max_lines=3,
                overflow=ft.TextOverflow.ELLIPSIS,
            ),
            ft.Row(spacing=10, wrap=True, controls=[btn_play, btn_info]),
        ],
    )

    return ft.Container(
        expand=True,
        height=320,
        border_radius=ft.BorderRadius(8, 8, 8, 8),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=_hero_gradient(movie.title),
        ),
        content=ft.Stack(
            controls=[
                # Icono decorativo de fondo
                ft.Container(
                    alignment=ft.Alignment(0.85, 0),
                    content=ft.Icon(
                        ft.Icons.MOVIE_ROUNDED if movie.type == "Movie"
                        else ft.Icons.TV_ROUNDED,
                        color=ft.Colors.with_opacity(0.06, "white"),
                        size=260,
                    ),
                ),
                # Contenido
                ft.Container(
                    padding=ft.Padding(28, 28, 28, 28),
                    content=content_layer,
                ),
            ],
        ),
    )
