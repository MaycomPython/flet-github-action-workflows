import flet as ft
import traceback

def main(page: ft.Page):
    try:
        # ===============================================================
        # CÓDIGO SEM OS ÍCONES PARA ISOLAR O PROBLEMA
        # ===============================================================

        # 1. CONFIGURAÇÃO DA PÁGINA
        page.title = "App Responsivo Flet"
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.theme = ft.Theme(color_scheme_seed="bluegrey")
        page.dark_theme = ft.Theme(color_scheme_seed="bluegrey")
        page.padding = 0

        # 2. FUNÇÃO DO EVENTO DO BOTÃO
        def enviar_click(e):
            if user_input_field.value:
                output_text.value = f"Olá, {user_input_field.value}!"
                output_text.opacity = 1
                user_input_field.value = ""
                user_input_field.focus()
                page.update()

        # 3. DEFINIÇÃO DOS CONTROLES (WIDGETS)
        output_text = ft.Text(
            "Digite algo e clique em enviar...",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            opacity=0.5,
            animate_opacity=300
        )

        user_input_field = ft.TextField(
            label="Qual o seu nome?",
            hint_text="Ex: Maria",
            border=ft.InputBorder.OUTLINE,
            border_radius=10,
            # A LINHA DO ÍCONE FOI REMOVIDA DAQUI
            on_submit=enviar_click,
        )

        send_button = ft.ElevatedButton(
            text="Enviar",
            # A LINHA DO ÍCONE FOI REMOVIDA DAQUI
            height=50,
            on_click=enviar_click,
        )
        
        # 4. MONTAGEM DO LAYOUT DO CONTEÚDO
        layout_conteudo = ft.Container(
            width=500,
            bgcolor=ft.colors.with_opacity(0.05, ft.colors.ON_SURFACE),
            border_radius=15,
            padding=30,
            content=ft.Column(
                controls=[
                    output_text,
                    ft.Container(height=20),
                    user_input_field,
                    send_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        )

        # 5. CRIAÇÃO DO "PALCO" PRINCIPAL
        main_container = ft.Container(
            content=layout_conteudo,
            expand=True,
            alignment=ft.alignment.center
        )

        # 6. ADICIONA O PALCO PRINCIPAL À PÁGINA
        page.add(main_container)
        page.update()

    except Exception as e:
        page.clean()
        error_details = traceback.format_exc()
        error_text = ft.Text(
            value=f"Ocorreu um erro fatal:\n\n{error_details}",
            selectable=True,
            font_family="monospace"
        )
        error_view = ft.Column(
            [error_text], 
            scroll=ft.ScrollMode.ADAPTIVE, 
            expand=True
        )
        page.add(error_view)
        page.update()

# Inicia o app
ft.app(target=main)
