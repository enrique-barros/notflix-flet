import random
import flet as ft

from components.hero_banner import build_hero_banner
from components.movie_card import build_movie_card
from config.theme import COLOR_BG, COLOR_SUBTEXT, COLOR_TEXT, FONT_SIZE_SUBTITLE
from data.movie_model import Movie, load_movies


def _clickable_card(movie: Movie, page: ft.Page) -> ft.GestureDetector:
    from router import navigate_to
    return ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.CLICK,
        on_tap=lambda _: navigate_to(page, f"/detail/{movie.show_id}"),
        content=build_movie_card(movie, width=160),
    )


def _section(title: str, movies: list[Movie], page: ft.Page) -> ft.Column:
    return ft.Column(
        spacing=10,
        controls=[
            ft.Text(title, size=FONT_SIZE_SUBTITLE, color=COLOR_TEXT, weight=ft.FontWeight.BOLD),
            ft.Row(
                scroll=ft.ScrollMode.AUTO,
                spacing=10,
                controls=[_clickable_card(m, page) for m in movies],
            ),
        ],
    )


def build_home_view(page: ft.Page) -> ft.Column:
    from router import navigate_to

    all_movies  = load_movies()
    movies_only = [m for m in all_movies if m.type == "Movie"]
    shows_only  = [m for m in all_movies if m.type == "TV Show"]
    featured    = random.choice(movies_only[:50])

    # ── Buscador ─────────────────────────────────────────────
    results_grid = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=180,
        spacing=10,
        run_spacing=10,
        controls=[],
    )
    no_results     = ft.Text("Sin resultados.", color=COLOR_SUBTEXT, italic=True, visible=False)
    search_section = ft.Column(
        visible=False,
        spacing=10,
        controls=[
            ft.Text("Resultados de búsqueda", size=FONT_SIZE_SUBTITLE,
                    color=COLOR_TEXT, weight=ft.FontWeight.BOLD),
            no_results,
            results_grid,
        ],
    )
    catalog_section = ft.Column(
        spacing=28,
        controls=[
            _section("🎬 Películas destacadas", movies_only[:16], page),
            _section("📺 Series populares",      shows_only[:16],  page),
            _section("🔥 Estrenos recientes",    movies_only[16:32], page),
        ],
    )

    def on_search(e: ft.ControlEvent) -> None:
        query = e.control.value.strip().lower()
        if not query:
            catalog_section.visible = True
            search_section.visible  = False
            results_grid.controls.clear()
            page.update()
            return
        found = [
            m for m in all_movies
            if query in m.title.lower()
            or query in m.listed_in.lower()
            or query in m.director.lower()
        ][:40]
        results_grid.controls   = [_clickable_card(m, page) for m in found]
        no_results.visible      = len(found) == 0
        catalog_section.visible = False
        search_section.visible  = True
        page.update()

    search_bar = ft.TextField(
        hint_text="Buscar títulos, géneros, directores…",
        hint_style=ft.TextStyle(color=COLOR_SUBTEXT),
        border_color=ft.Colors.with_opacity(0.2, "white"),
        focused_border_color="#E50914",
        color=COLOR_TEXT,
        bgcolor=ft.Colors.with_opacity(0.08, "white"),
        border_radius=ft.BorderRadius(6, 6, 6, 6),
        prefix_icon=ft.Icons.SEARCH,
        on_change=on_search,
    )

    def ver_detalle(e: ft.ControlEvent) -> None:
        navigate_to(page, f"/detail/{featured.show_id}")

    return ft.Column(
        expand=True,
        spacing=24,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            build_hero_banner(featured, on_ver_detalle=ver_detalle),
            search_bar,
            search_section,
            catalog_section,
        ],
    )
