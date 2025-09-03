import flet as ft
import traceback # Biblioteca para formatar detalhes do erro

def main(page: ft.Page):
    try:
        # ===============================================================
        # SEU CÓDIGO ORIGINAL COMEÇA AQUI
        # A lógica do seu app está toda dentro deste bloco 'try'.
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
            prefix_icon=ft.icons.PERSON_ROUNDED,
            on_submit=enviar_click,
        )

        send_button = ft.ElevatedButton(
            text="Enviar",
            icon=ft.icons.SEND_ROUNDED,
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

        # 5. CRIAÇÃO DO "PALCO" PRINCIPAL QUE OCUPA A TELA INTEIRA
        main_container = ft.Container(
            content=layout_conteudo,
            expand=True,
            alignment=ft.alignment.center
        )

        # 6. ADICIONA O PALCO PRINCIPAL À PÁGINA
        page.add(main_container)
        page.update()

    except Exception as e:
        # ===============================================================
        # BLOCO DE CAPTURA DE ERRO
        # Se qualquer coisa acima falhar, este código será executado.
        # Ele vai limpar a tela e mostrar o erro que aconteceu.
        # ===============================================================
        
        page.clean()
        
        # Formata o erro completo com todos os detalhes técnicos
        error_details = traceback.format_exc()
        
        # Cria um texto rolável para exibir o erro na tela do celular
        error_text = ft.Text(
            value=f"Ocorreu um erro fatal:\n\n{error_details}",
            selectable=True, # Permite copiar o texto do erro
            font_family="monospace" # Fonte monoespaçada para facilitar a leitura
        )
        
        # Coloca o texto de erro dentro de uma Coluna que pode ser rolada
        error_view = ft.Column(
            [error_text], 
            scroll=ft.ScrollMode.ADAPTIVE, 
            expand=True
        )

        # Adiciona a visualização de erro à página
        page.add(error_view)
        page.update()

# Inicia o app
ft.app(target=main)
