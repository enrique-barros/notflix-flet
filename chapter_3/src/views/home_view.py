import flet as ft
from config.theme import COLOR_TEXT, COLOR_SUBTEXT, FONT_SIZE_SUBTITLE, FONT_SIZE_BODY
from components.logo import build_logo
from components.genre_badge import build_genres_row
from components.status_badge import build_status_badge

GENEROS = ["Acción", "Drama", "Sci-Fi", "Terror"]

def build_body() -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Explorador de contenido", size=FONT_SIZE_SUBTITLE, color=COLOR_TEXT),
                ft.Text("Aplicación construida con flet", size=FONT_SIZE_BODY, italic=True, color=COLOR_SUBTEXT),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
        ),
        alignment=ft.Alignment.CENTER,
        margin=ft.Margin(0, 0, 0, 30),
    )

def build_home_view() -> ft.Column:
    return ft.Column(
        controls=[
            build_logo(),
            build_body(),
            build_genres_row(GENEROS),
            build_status_badge("Sistema en desarrollo"),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
