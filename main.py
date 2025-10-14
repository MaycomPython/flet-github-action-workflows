import flet as ft
import time

def main(page: ft.Page):
    # --- Configurações da Página (Janela/App) ---
    page.title = "Login e Cadastro"
    
    # Remove as definições de tamanho fixo para se adaptar a qualquer tela
    # page.window_width = 400
    # page.window_height = 800
    # page.window_resizable = False
    
    # Alinhamento para simular um app de celular
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Tema do App com a cor Verde
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")
    
    # IMPORTANTE: Ajuste para renderização correta no mobile
    page.padding = 0

    # --- Funções de Lógica ---
    def show_register_view(e):
        login_view.visible = False
        register_view.visible = True
        page.update()

    def show_login_view(e):
        login_view.visible = True
        register_view.visible = False
        page.update()

    def login_clicked(e):
        if not email_login.value or not senha_login.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos!"),
                bgcolor=ft.colors.RED_ACCENT_700
            )
            page.snack_bar.open = True
            page.update()
            return
        print(f"Tentativa de login com Email: {email_login.value} e Senha: {senha_login.value}")
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Bem-vindo, {email_login.value}!"),
            bgcolor=ft.colors.GREEN_800
        )
        page.snack_bar.open = True
        page.update()

    def register_clicked(e):
        if not nome_register.value or not email_register.value or not senha_register.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos!"),
                bgcolor=ft.colors.RED_ACCENT_700
            )
            page.snack_bar.open = True
            page.update()
            return
        print(f"Usuário cadastrado com sucesso: Nome: {nome_register.value}, Email: {email_register.value}")
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Cadastro realizado com sucesso! Faça o login."),
            bgcolor=ft.colors.GREEN_800
        )
        page.snack_bar.open = True
        nome_register.value = ""
        email_register.value = ""
        senha_register.value = ""
        page.update()
        time.sleep(1)
        show_login_view(None)

    # --- Componentes da UI (Widgets) ---

    # --- Tela de Login ---
    email_login = ft.TextField(label="Email", hint_text="Digite seu email", prefix_icon="email", border_radius=10)
    senha_login = ft.TextField(label="Senha", hint_text="Digite sua senha", prefix_icon="lock", password=True, can_reveal_password=True, border_radius=10)
    
    login_view = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(name="lock_person", size=80),
            ft.Text("Bem-vindo de Volta!", size=32, weight=ft.FontWeight.BOLD),
            email_login,
            senha_login,
            ft.ElevatedButton(text="Login", on_click=login_clicked, width=300, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text("Não tem uma conta?"), ft.TextButton(text="Cadastre-se", on_click=show_register_view)])
        ]
    )

    # --- Tela de Cadastro ---
    nome_register = ft.TextField(label="Nome Completo", hint_text="Digite seu nome", prefix_icon="person", border_radius=10)
    email_register = ft.TextField(label="Email", hint_text="Digite um email válido", prefix_icon="email", border_radius=10)
    senha_register = ft.TextField(label="Crie uma Senha", hint_text="Digite sua nova senha", prefix_icon="lock", password=True, can_reveal_password=True, border_radius=10)

    register_view = ft.Column(
        visible=False,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(name="person_add", size=80),
            ft.Text("Crie sua Conta", size=32, weight=ft.FontWeight.BOLD),
            nome_register,
            email_register,
            senha_register,
            ft.ElevatedButton(text="Cadastrar", on_click=register_clicked, width=300, height=50, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Text("Já tem uma conta?"), ft.TextButton(text="Faça Login", on_click=show_login_view)])
        ]
    )

    # --- Estrutura Principal da Página ---
    # Envolvemos tudo em um SafeArea para evitar sobreposição com a barra de status/notches
    # O Container principal agora tem expand=True para ocupar toda a tela
    page.add(
        ft.SafeArea(
            expand=True, # Garante que o SafeArea também se expanda
            content=ft.Container(
                # expand=True, # O expand no SafeArea já resolve isso para o content
                alignment=ft.alignment.center, # Centraliza o conteúdo dentro do Container
                padding=30,
                content=ft.Column(
                    # A coluna agora não precisa de alinhamento horizontal, pois o container já centraliza
                    controls=[
                        login_view,
                        register_view
                    ]
                )
            )
        )
    )

    page.update()

# Inicia o aplicativo
if __name__ == "__main__":
    ft.app(target=main)
