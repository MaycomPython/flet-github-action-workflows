import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURAÇÃO DA PÁGINA
    page.title = "App Responsivo Flet"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed="bluegrey")
    page.dark_theme = ft.Theme(color_scheme_seed="bluegrey")
    
    # Removemos QUALQUER configuração de alinhamento ou padding da página
    # A página será apenas um host para nosso container principal.
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
    # Esta é a sua UI, agora dentro de uma Coluna com largura máxima.
    # Isso a torna responsiva: em telas pequenas ela encolhe, em grandes ela não passa de 500px.
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
    # PONTO CHAVE 1: Este container vai preencher toda a tela disponível.
    # PONTO CHAVE 2: Ele vai usar seu alinhamento interno para centralizar o conteúdo.
    main_container = ft.Container(
        content=layout_conteudo,   # Colocamos nosso layout aqui dentro
        expand=True,               # Diz ao container para ocupar todo o espaço
        alignment=ft.alignment.center # Centraliza o 'content' (nosso layout)
    )

    # 6. ADICIONA APENAS O PALCO PRINCIPAL À PÁGINA
    page.add(main_container)
    page.update()

# Inicia o app
ft.app(target=main)
