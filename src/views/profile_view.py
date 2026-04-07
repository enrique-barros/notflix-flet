import flet as ft
from config.theme import COLOR_PRIMARY, COLOR_SUBTEXT, COLOR_TEXT

PROFILES = [
    ("Ana",      "#E50914", ft.Icons.PERSON),
    ("Carlos",   "#0070f3", ft.Icons.PERSON_2),
    ("Marta",    "#7928ca", ft.Icons.PERSON_3),
    ("Invitado", "#444444", ft.Icons.PERSON_OUTLINE),
]


def _avatar(name: str, color: str, icon, on_click) -> ft.Column:
    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        controls=[
            ft.Container(
                width=100,
                height=100,
                border_radius=ft.BorderRadius(8, 8, 8, 8),
                bgcolor=color,
                alignment=ft.Alignment(0, 0),
                on_click=on_click,
                ink=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        ft.Icon(icon, color="white", size=44),
                    ],
                ),
            ),
            ft.Text(name, size=15, color=COLOR_TEXT, weight=ft.FontWeight.W_500),
        ],
    )


def build_profile_view(page: ft.Page) -> ft.Column:
    from router import navigate_to

    def select_profile(e: ft.ControlEvent) -> None:
        navigate_to(page, "/home")

    profile_row = ft.Row(
        wrap=True,
        spacing=28,
        run_spacing=28,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            _avatar(name, color, icon, on_click=select_profile)
            for name, color, icon in PROFILES
        ],
    )

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        spacing=0,
        controls=[
            # Logo
            ft.Text(
                "NOTFLIX",
                size=56,
                weight=ft.FontWeight.BOLD,
                color=COLOR_PRIMARY,
            ),
            ft.Container(height=8),
            ft.Text(
                "¿Quién está viendo?",
                size=24,
                color=COLOR_TEXT,
                weight=ft.FontWeight.W_300,
            ),
            ft.Container(height=48),
            profile_row,
            ft.Container(height=48),
            ft.Text(
                "Selecciona tu perfil para continuar",
                size=13,
                color=COLOR_SUBTEXT,
            ),
        ],
    )
