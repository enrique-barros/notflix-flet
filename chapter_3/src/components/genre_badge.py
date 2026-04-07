import flet as ft
from config.theme import (
    COLOR_TEXT, COLOR_BADGE_BG,
    FONT_SIZE_BADGE, PADDING_BADGE, RADIUS_BADGE
)

def build_genre_badge(texto: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(texto, color=COLOR_TEXT, size=FONT_SIZE_BADGE),
        bgcolor=COLOR_BADGE_BG,
        padding=PADDING_BADGE,
        border_radius=RADIUS_BADGE,
    )

def build_genres_row(generos: list[str]) -> ft.Row:
    return ft.Row(
        controls=[build_genre_badge(g) for g in generos],
        alignment=ft.MainAxisAlignment.CENTER,
        margin=ft.Margin(0, 0, 0, 10),
    )