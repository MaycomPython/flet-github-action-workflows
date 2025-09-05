import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURAÇÃO DA PÁGINA E TEMA MATERIAL DESIGN
    page.title = "App de Boas-Vindas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(color_scheme_seed="indigo")
    page.dark_theme = ft.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.SYSTEM

    # 2. FUNÇÃO DO BOTÃO (LÓGICA DO APP)
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor, digite seu nome"
            txt_name.focus()
        else:
            name = txt_name.value
            page.clean()
            
            page.add(
                ft.Column(
                    [
                        # CORREÇÃO APLICADA AQUI:
                        # Trocamos ft.colors.AMBER pela string "amber", que é mais segura.
                        ft.Icon(ft.Icons.CELEBRATION, color="amber", size=80),
                        
                        ft.Text(f"Olá, {name}!", size=32, weight=ft.FontWeight.BOLD),
                        ft.Text("Seja bem-vindo(a) ao Flet!", size=16, italic=True)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            )
        
        page.update()

    # 3. CRIAÇÃO DOS WIDGETS (COMPONENTES VISUAIS)
    txt_name = ft.TextField(
        label="Seu nome",
        hint_text="Como podemos te chamar?",
        prefix_icon=ft.Icons.PERSON_OUTLINE, 
        border=ft.InputBorder.OUTLINE,
        border_radius=8
    )

    btn_hello = ft.ElevatedButton(
        text="Dizer Olá!",
        icon=ft.Icons.WAVING_HAND,
        height=50,
        on_click=btn_click,
    )

    # 4. MONTAGEM DO LAYOUT RESPONSIVO
    layout = ft.Column(
        width=400,
        controls=[
            ft.Text("Vamos começar", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Este é um app de exemplo construído de forma robusta para rodar no Android.", text_align=ft.TextAlign.CENTER),
            ft.Container(height=20),
            txt_name,
            btn_hello
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(layout)
    page.update()

# Inicia o app
ft.app(target=main)
