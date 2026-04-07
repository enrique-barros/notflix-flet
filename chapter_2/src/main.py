import flet as ft

def main(page: ft.Page):
    # Configuración general de la página
    page.title = "Notflix App"
    page.padding = 20
    page.bgcolor = ft.Colors.BLACK_87

    # Centramos todo el contenido horizontal y verticalmente en la pantalla
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Elemento de logo principal
    logo = ft.Text(
        "NotFlix".upper(),
        size=48,
        weight=ft.FontWeight.BOLD,
        color="#E50914"
    )

    # Envolvemos el logo en un Container para darle "cuerpo"
    contenedor_logo = ft.Container(
    content=logo,
    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    padding=ft.Padding(20, 10, 20, 10),
    border_radius=ft.BorderRadius(10, 10, 10, 10),
    alignment=ft.Alignment.CENTER,
    margin=ft.Margin(0, 0, 0, 20)
    )

    # Subtítulo descriptivo
    subtitulo = ft.Text(
        "Explorador de contenido",
        size=20,
        color="white"
    )

    # Texto de descripción de la app
    descripcion = ft.Text(
        "Aplicación construida con flet",
        size=14,
        italic=True,
        color="bluegrey"
    )

    # Contenedor para agrupar el cuerpo de la app y centrar sus textos internamente
    contenedor_body = ft.Container(
        content=ft.Column(
            controls=[subtitulo, descripcion],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        ),
        alignment=ft.Alignment.CENTER,
        margin=ft.Margin(0, 0, 0, 30)
    )  

    # Indicador de estado del sistema
    estado = ft.Text(
        "Sistema en desarrollo",
        size=16,
        weight=ft.FontWeight.W_500,
        color="red"
    )

    # Contenedor para transformar el texto de estado en una tarjeta visual o badge
    contenedor_estado = ft.Container(
        content=estado,
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.RED),
        padding=ft.Padding(15, 8, 15, 8),
        border_radius=ft.BorderRadius(5, 5, 5, 5),
        border=ft.Border.all(1, ft.Colors.RED_800),
        alignment=ft.Alignment.CENTER,
        width=250

    )

    # Fila con tres badges de género
    fila_generos = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("Acción", color="white", size=12),
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                padding=ft.Padding(10, 5, 10, 5),
                border_radius=ft.BorderRadius(20, 20, 20, 20),
            ),
            ft.Container(
                content=ft.Text("Drama", color="white", size=12),
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                padding=ft.Padding(10, 5, 10, 5),
                border_radius=ft.BorderRadius(20, 20, 20, 20),
            ),
            ft.Container(
                content=ft.Text("Sci-Fi", color="white", size=12),
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
                padding=ft.Padding(10, 5, 10, 5),
                border_radius=ft.BorderRadius(20, 20, 20, 20),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        margin=ft.Margin(0,0,0,10)
    )

    # Añadir todos los elementos a la página
    page.add(
        contenedor_logo,
        contenedor_body,
        fila_generos,
        contenedor_estado
    )

ft.run(main)