import flet as ft
from config.theme import (
    COLOR_PRIMARY, FONT_SIZE_LOGO,
    PADDING_LOGO, RADIUS_CARD
)

def build_logo(texto: str = "NotFlix") -> ft.Container:
    logo = ft.Text(
        texto.upper(),
        size=FONT_SIZE_LOGO,
        weight=ft.FontWeight.BOLD,
        color=COLOR_PRIMARY,
    )
    return ft.Container(
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        padding=PADDING_LOGO,
        border_radius=RADIUS_CARD,
        alignment=ft.Alignment.CENTER,
        margin=ft.Margin(0, 0, 0, 20),
        content=logo,
    )
