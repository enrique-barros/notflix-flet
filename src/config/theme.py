import flet as ft

# ── Paleta ────────────────────────────────────────────────────
COLOR_PRIMARY    = "#E50914"          # rojo Netflix
COLOR_BG         = "#141414"          # negro Netflix (no BLACK_87 que es gris)
COLOR_SURFACE    = "#1F1F1F"          # superficie de cards
COLOR_SURFACE2   = "#2A2A2A"          # superficie elevada
COLOR_TEXT       = "#FFFFFF"
COLOR_SUBTEXT    = "#A3A3A3"
COLOR_ACCENT     = "#E50914"

COLOR_BADGE_BG   = ft.Colors.with_opacity(0.18, ft.Colors.WHITE)
COLOR_CARD_BG    = "#1F1F1F"
COLOR_STATUS_BG     = ft.Colors.with_opacity(0.1, ft.Colors.RED)
COLOR_STATUS_BORDER = ft.Colors.RED_800

# ── Tipografía ────────────────────────────────────────────────
FONT_SIZE_LOGO       = 48
FONT_SIZE_SUBTITLE   = 18
FONT_SIZE_BODY       = 14
FONT_SIZE_STATUS     = 16
FONT_SIZE_BADGE      = 11
FONT_SIZE_CARD_TITLE = 13
FONT_SIZE_CARD_META  = 11

# ── Espaciado ────────────────────────────────────────────────
PADDING_LOGO   = ft.Padding(20, 10, 20, 10)
PADDING_BADGE  = ft.Padding(10, 5, 10, 5)
PADDING_STATUS = ft.Padding(15, 8, 15, 8)
PADDING_CARD   = ft.Padding(10, 10, 10, 10)

# ── Radios ────────────────────────────────────────────────────
RADIUS_CARD   = ft.BorderRadius(6, 6, 6, 6)
RADIUS_BADGE  = ft.BorderRadius(4, 4, 4, 4)
RADIUS_STATUS = ft.BorderRadius(5, 5, 5, 5)
