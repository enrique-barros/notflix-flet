import flet as ft
from config.theme import (
    COLOR_STATUS_BG, COLOR_STATUS_BORDER,
    FONT_SIZE_STATUS, PADDING_STATUS, RADIUS_STATUS
)

def build_status_badge(mensaje: str, color: str = "red") -> ft.Container:
    return ft.Container(
        content=ft.Text(
            mensaje,
            size=FONT_SIZE_STATUS,
            weight=ft.FontWeight.W_500,
            color=color,
        ),
        bgcolor=COLOR_STATUS_BG,
        padding=PADDING_STATUS,
        border_radius=RADIUS_STATUS,
        border=ft.Border.all(1, COLOR_STATUS_BORDER),
        alignment=ft.Alignment.CENTER,
        width=250,
    )