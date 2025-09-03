import flet as ft
from flet import colors

def main(page: ft.Page):
    # 1. CONFIGURAÇÃO DA PÁGINA
    page.title = "App Responsivo Flet"
    page.theme_mode = ft.ThemeMode.SYSTEM  # Adapta ao tema do OS (Claro/Escuro)
    
    # Gera um tema Material 3 a partir de uma cor semente
    page.theme = ft.Theme(color_scheme_seed="bluegrey")
    page.dark_theme = ft.Theme(color_scheme_seed="bluegrey")

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # 2. FUNÇÃO DO EVENTO DO BOTÃO
    def enviar_click(e):
        if user_input_field.value:  # Verifica se o campo não está vazio
            output_text.value = f"Olá, {user_input_field.value}!"
            output_text.opacity = 1  # Torna o texto totalmente visível
            user_input_field.value = "" # Limpa o campo de texto
            page.update()
            user_input_field.focus() # Coloca o foco de volta no campo de texto

    # 3. DEFINIÇÃO DOS CONTROLES (WIDGETS)
    output_text = ft.Text(
        "Digite algo e clique em enviar...",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        opacity=0.5, # Começa um pouco transparente
        animate_opacity=300 # Animação de fade-in/out
    )

    user_input_field = ft.TextField(
        label="Qual o seu nome?",
        hint_text="Ex: Maria",
        width=300,
        border=ft.InputBorder.OUTLINE,
        border_radius=10,
        prefix_icon=ft.icons.PERSON_ROUNDED,
        on_submit=enviar_click, # Permite enviar com a tecla Enter
    )

    send_button = ft.ElevatedButton(
        text="Enviar",
        icon=ft.icons.SEND_ROUNDED,
        height=50,
        width=300,
        on_click=enviar_click,
    )
    
    # 4. MONTAGEM DO LAYOUT RESPONSIVO
    # Usamos um Container para limitar a largura em telas grandes (desktops)
    # e permitir que ele encolha em telas pequenas (celulares).
    layout_responsivo = ft.Container(
        width=500, # Largura máxima
        bgcolor=colors.with_opacity(0.05, colors.ON_SURFACE), # Cor de fundo sutil
        border_radius=15,
        padding=30,
        content=ft.Column(
            controls=[
                output_text,
                ft.Container(height=20), # Espaçamento
                user_input_field,
                send_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

    # 5. ADICIONA O LAYOUT FINAL À PÁGINA
    page.add(layout_responsivo)
    page.update()

# Inicia o app
ft.app(target=main)
