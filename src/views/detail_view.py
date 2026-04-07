import flet as ft
from config.theme import (
    COLOR_BG, COLOR_PRIMARY, COLOR_SUBTEXT, COLOR_TEXT,
    RADIUS_BADGE, RADIUS_CARD,
)
from data.movie_model import Movie

_POSTER_GRADIENTS = [
    ["#0f0c29", "#302b63", "#24243e"],
    ["#1a1a2e", "#16213e", "#0f3460"],
    ["#2d1b69", "#11998e", "#38ef7d"],
    ["#fc4a1a", "#f7b733", "#2c3e50"],
    ["#0f2027", "#203a43", "#2c5364"],
    ["#16222a", "#3a6073", "#16222a"],
    ["#3c1053", "#ad5389", "#3c1053"],
    ["#134e5e", "#71b280", "#134e5e"],
]


def _grad(title: str) -> list[str]:
    return _POSTER_GRADIENTS[hash(title) % len(_POSTER_GRADIENTS)]


def _info_row(label: str, value: str) -> ft.Row:
    return ft.Row(
        spacing=10,
        controls=[
            ft.Text(label, size=13, color=COLOR_SUBTEXT, width=90),
            ft.Text(value or "—", size=13, color=COLOR_TEXT, expand=True,
                    max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
        ],
    )


def _genre_chip(genre: str) -> ft.Container:
    return ft.Container(
        bgcolor=ft.Colors.with_opacity(0.15, "white"),
        padding=ft.Padding(10, 4, 10, 4),
        border_radius=RADIUS_BADGE,
        content=ft.Text(genre, size=12, color=COLOR_TEXT),
    )


def build_detail_view(movie: Movie, page: ft.Page) -> ft.Column:
    from router import navigate_to
    type_color = COLOR_PRIMARY if movie.type == "Movie" else "#0070f3"

    # ── Póster simulado ───────────────────────────────────────
    poster = ft.Container(
        width=130,
        height=195,
        border_radius=RADIUS_CARD,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=_grad(movie.title),
        ),
        content=ft.Icon(
            ft.Icons.MOVIE_ROUNDED if movie.type == "Movie" else ft.Icons.TV_ROUNDED,
            color=ft.Colors.with_opacity(0.2, "white"),
            size=60,
        ),
    )

    # ── Botón play grande ─────────────────────────────────────
    btn_play = ft.Container(
        bgcolor=COLOR_TEXT,
        border_radius=ft.BorderRadius(4, 4, 4, 4),
        padding=ft.Padding(20, 10, 20, 10),
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

    header = ft.Row(
        spacing=20,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[
            poster,
            ft.Column(
                expand=True,
                spacing=10,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.with_opacity(0.9, type_color),
                        padding=ft.Padding(8, 3, 8, 3),
                        border_radius=RADIUS_BADGE,
                        content=ft.Text(movie.type, size=11, color="white",
                                        weight=ft.FontWeight.W_700),
                    ),
                    ft.Text(movie.title, size=24, color=COLOR_TEXT,
                            weight=ft.FontWeight.BOLD, max_lines=3,
                            overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Row(
                        spacing=6,
                        wrap=True,
                        controls=[
                            ft.Text(str(movie.release_year), size=13, color=COLOR_SUBTEXT),
                            ft.Text("·", size=13, color=COLOR_SUBTEXT),
                            ft.Text(movie.rating or "NR", size=13, color=COLOR_SUBTEXT),
                            ft.Text("·", size=13, color=COLOR_SUBTEXT),
                            ft.Text(movie.duration or "—", size=13, color=COLOR_SUBTEXT),
                        ],
                    ),
                    ft.Row(wrap=True, spacing=6,
                           controls=[_genre_chip(g) for g in movie.genres]),
                    btn_play,
                ],
            ),
        ],
    )

    synopsis = ft.Column(spacing=8, controls=[
        ft.Text("Sinopsis", size=16, color=COLOR_TEXT, weight=ft.FontWeight.BOLD),
        ft.Text(movie.description or "Sin descripción.",
                size=14, color=ft.Colors.with_opacity(0.85, "white")),
    ])

    metadata = ft.Column(spacing=6, controls=[
        ft.Text("Información", size=16, color=COLOR_TEXT, weight=ft.FontWeight.BOLD),
        _info_row("Año",      str(movie.release_year)),
        _info_row("Rating",   movie.rating),
        _info_row("Duración", movie.duration),
        _info_row("País",     movie.country),
        _info_row("Añadido",  movie.date_added),
        _info_row("Director", movie.director),
    ])

    cast_col = ft.Column(spacing=6, controls=[
        ft.Text("Reparto", size=16, color=COLOR_TEXT, weight=ft.FontWeight.BOLD),
    ])
    if movie.cast:
        for name in [c.strip() for c in movie.cast.split(",")][:8]:
            cast_col.controls.append(ft.Row(spacing=8, controls=[
                ft.Icon(ft.Icons.PERSON_OUTLINE, color=COLOR_SUBTEXT, size=14),
                ft.Text(name, size=13, color=COLOR_TEXT),
            ]))

    divider = ft.Divider(color=ft.Colors.with_opacity(0.1, "white"), height=1)

    back_btn = ft.Container(
        on_click=lambda _: navigate_to(page, "/home"),
        ink=True,
        border_radius=ft.BorderRadius(4, 4, 4, 4),
        padding=ft.Padding(0, 4, 8, 4),
        content=ft.Row(
            spacing=4,
            tight=True,
            controls=[
                ft.Icon(ft.Icons.ARROW_BACK_IOS_NEW_ROUNDED, color=COLOR_PRIMARY, size=14),
                ft.Text("Volver al catálogo", color=COLOR_PRIMARY, size=14),
            ],
        ),
    )

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=22,
        controls=[back_btn, header, divider, synopsis, divider, metadata, divider, cast_col],
    )
