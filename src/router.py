import flet as ft
from config.theme import COLOR_BG
from data.movie_model import Movie, load_movies
from views.detail_view import build_detail_view
from views.home_view import build_home_view
from views.profile_view import build_profile_view

_MOVIE_INDEX: dict[str, Movie] = {m.show_id: m for m in load_movies()}


def _view_profiles(page: ft.Page) -> ft.View:
    return ft.View(
        route="/",
        bgcolor=COLOR_BG,
        controls=[ft.SafeArea(expand=True, content=build_profile_view(page))],
    )


def _view_home(page: ft.Page) -> ft.View:
    return ft.View(
        route="/home",
        bgcolor=COLOR_BG,
        appbar=ft.AppBar(
            title=ft.Text("NOTFLIX", color="#E50914", weight=ft.FontWeight.BOLD, size=22),
            bgcolor="#0a0a0a",
            automatically_imply_leading=False,
            actions=[
                ft.Container(width=16),
            ],
        ),
        controls=[
            ft.Container(
                expand=True,
                padding=ft.Padding(16, 0, 16, 16),
                content=ft.SafeArea(expand=True, content=build_home_view(page)),
            )
        ],
    )


def _view_detail(page: ft.Page, show_id: str) -> ft.View:
    movie = _MOVIE_INDEX.get(show_id)
    content = (
        build_detail_view(movie, page)
        if movie
        else ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Título no encontrado", size=20, color="white"),
                ft.TextButton("<- Volver", on_click=lambda _: navigate_to(page, "/home")),
            ],
        )
    )
    return ft.View(
        route=f"/detail/{show_id}",
        bgcolor=COLOR_BG,
        controls=[
            ft.Container(
                expand=True,
                padding=ft.Padding(16, 16, 16, 16),
                content=ft.SafeArea(expand=True, content=content),
            )
        ],
    )


def navigate_to(page: ft.Page, route: str) -> None:
    page.views.clear()
    page.views.append(_view_profiles(page))
    if route == "/home":
        page.views.append(_view_home(page))
    elif route.startswith("/detail/"):
        show_id = route.split("/detail/", 1)[-1]
        page.views.append(_view_home(page))
        page.views.append(_view_detail(page, show_id))
    page.update()


def setup_router(page: ft.Page) -> None:
    def view_pop(e: ft.ViewPopEvent) -> None:
        if len(page.views) > 1:
            page.views.pop()
            page.update()
    page.on_view_pop = view_pop
    navigate_to(page, "/")
