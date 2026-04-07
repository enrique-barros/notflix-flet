import flet as ft
from config.theme import COLOR_BG
from views.home_view import build_home_view

def main(page: ft.Page):
    page.title = "Notflix App"
    page.padding = 20
    page.bgcolor = COLOR_BG
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.SafeArea(content=build_home_view())
    )

if __name__ == "__main__":
    ft.run(main)