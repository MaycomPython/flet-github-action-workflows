import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURAÇÃO DA PÁGINA
    page.title = "App Responsivo Flet"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed="bluegrey")
    page.dark_theme = ft.Theme(color_scheme_seed="bluegrey")

    # Centraliza todo o conteúdo da página de forma robusta
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.padding = 20

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
        # Em telas pequenas, é melhor deixar a largura se adaptar.
        # width=300, 
        expand=True, # Faz o TextField ocupar o espaço disponível na coluna
        border=ft.InputBorder.OUTLINE,
        border_radius=10,
        prefix_icon=ft.icons.PERSON_ROUNDED,
        on_submit=enviar_click,
    )

    send_button = ft.ElevatedButton(
        text="Enviar",
        icon=ft.icons.SEND_ROUNDED,
        height=50,
        # width=300,
        expand=True, # Faz o botão ocupar o espaço disponível na coluna
        on_click=enviar_click,
    )
    
    # 4. MONTAGEM DO LAYOUT RESPONSIVO
    # Ao invés de um Container com largura fixa, usamos uma Coluna que
    # será centralizada pela própria página.
    layout_responsivo = ft.Column(
            # Limita a largura máxima dos controles para não ficarem gigantes em telas grandes
            width=500, 
            controls=[
                output_text,
                ft.Container(height=20),
                user_input_field,
                send_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
    )

    # 5. ADICIONA O LAYOUT FINAL À PÁGINA
    page.add(layout_responsivo)
    page.update()

# Inicia o app
ft.app(target=main)
