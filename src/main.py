import flet as ft
from config.theme import COLOR_BG
from router import setup_router


def main(page: ft.Page) -> None:
    page.title = "Notflix"
    page.padding = 0
    page.bgcolor = COLOR_BG
    page.window.icon = "assets/logo.png"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    setup_router(page)


if __name__ == "__main__":
    ft.run(main)