import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURAÇÃO DA PÁGINA E TEMA MATERIAL DESIGN
    page.title = "App de Boas-Vindas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Centraliza o conteúdo verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Centraliza horizontalmente

    # Aplicando um tema Material 3 bonito com base na cor Indigo
    page.theme = ft.Theme(color_scheme_seed="indigo")
    page.dark_theme = ft.Theme(color_scheme_seed="indigo")
    page.theme_mode = ft.ThemeMode.SYSTEM # Respeita o tema claro/escuro do celular

    # 2. FUNÇÃO DO BOTÃO (LÓGICA DO APP)
    def btn_click(e):
        # Validação: verifica se o campo de texto não está vazio
        if not txt_name.value:
            txt_name.error_text = "Por favor, digite seu nome"
            txt_name.focus() # Coloca o foco de volta no campo
        else:
            # Lógica de sucesso
            name = txt_name.value
            page.clean() # Limpa a tela
            
            # Cria a nova tela de boas-vindas
            page.add(
                ft.Column(
                    [
                        ft.Icon(ft.Icons.CELEBRATION, color=ft.colors.AMBER, size=80),
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
        # Usando a forma mais segura de chamar ícones
        prefix_icon=ft.Icons.PERSON_OUTLINE, 
        border=ft.InputBorder.OUTLINE,
        border_radius=8
    )

    btn_hello = ft.ElevatedButton(
        text="Dizer Olá!",
        # Usando a forma mais segura de chamar ícones
        icon=ft.Icons.WAVING_HAND,
        height=50,
        on_click=btn_click,
    )

    # 4. MONTAGEM DO LAYOUT RESPONSIVO
    # Usamos uma Coluna com largura máxima para o conteúdo não esticar demais em telas grandes
    layout = ft.Column(
        width=400, # Largura máxima do conteúdo
        controls=[
            ft.Text("Vamos começar", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Este é um app de exemplo construído de forma robusta para rodar no Android.", text_align=ft.TextAlign.CENTER),
            ft.Container(height=20), # Espaçamento
            txt_name,
            btn_hello
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # Adiciona o layout à página
    page.add(layout)
    page.update()

# Inicia o app
ft.app(target=main)
