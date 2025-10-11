import flet as ft
import time

def main(page: ft.Page):
    # --- Configurações da Página (Janela/App) ---
    page.title = "Login e Cadastro"
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    
    # Alinhamento para simular um app de celular
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Tema do App com a cor Verde
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="green")

    # --- Funções de Lógica ---
    def show_register_view(e):
        """Alterna a visibilidade para a tela de cadastro."""
        login_view.visible = False
        register_view.visible = True
        page.update()

    def show_login_view(e):
        """Alterna a visibilidade para a tela de login."""
        login_view.visible = True
        register_view.visible = False
        page.update()

    def login_clicked(e):
        """Função chamada ao clicar no botão de Login."""
        # Lógica de validação (exemplo simples)
        if not email_login.value or not senha_login.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos!"),
                bgcolor=ft.colors.RED_ACCENT_700
            )
            page.snack_bar.open = True
            page.update()
            return

        # Simula uma verificação
        print(f"Tentativa de login com Email: {email_login.value} e Senha: {senha_login.value}")
        
        # Feedback para o usuário
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Bem-vindo, {email_login.value}!"),
            bgcolor=ft.colors.GREEN_800
        )
        page.snack_bar.open = True
        page.update()

    def register_clicked(e):
        """Função chamada ao clicar no botão de Cadastro."""
        # Lógica de validação (exemplo simples)
        if not nome_register.value or not email_register.value or not senha_register.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos!"),
                bgcolor=ft.colors.RED_ACCENT_700
            )
            page.snack_bar.open = True
            page.update()
            return

        # Simula o cadastro
        print(f"Usuário cadastrado com sucesso: Nome: {nome_register.value}, Email: {email_register.value}")

        # Feedback e volta para a tela de login
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Cadastro realizado com sucesso! Faça o login."),
            bgcolor=ft.colors.GREEN_800
        )
        page.snack_bar.open = True
        # Limpa os campos após o cadastro
        nome_register.value = ""
        email_register.value = ""
        senha_register.value = ""
        
        page.update()
        time.sleep(1) # Pequeno delay para o usuário ver o snackbar
        show_login_view(None) # Leva para a tela de login

    # --- Componentes da UI (Widgets) ---

    # --- Tela de Login ---
    email_login = ft.TextField(
        label="Email", 
        hint_text="Digite seu email",
        prefix_icon=ft.icons.EMAIL,
        border_radius=10
    )
    senha_login = ft.TextField(
        label="Senha", 
        hint_text="Digite sua senha",
        prefix_icon=ft.icons.LOCK,
        password=True, 
        can_reveal_password=True,
        border_radius=10
    )
    
    login_view = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(name=ft.icons.LOCK_PERSON, size=80),
            ft.Text("Bem-vindo de Volta!", size=32, weight=ft.FontWeight.BOLD),
            email_login,
            senha_login,
            ft.ElevatedButton(
                text="Login", 
                on_click=login_clicked, 
                width=300, 
                height=50,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Não tem uma conta?"),
                    ft.TextButton(text="Cadastre-se", on_click=show_register_view)
                ]
            )
        ]
    )

    # --- Tela de Cadastro ---
    nome_register = ft.TextField(
        label="Nome Completo", 
        hint_text="Digite seu nome",
        prefix_icon=ft.icons.PERSON,
        border_radius=10
    )
    email_register = ft.TextField(
        label="Email",
        hint_text="Digite um email válido",
        prefix_icon=ft.icons.EMAIL,
        border_radius=10
    )
    senha_register = ft.TextField(
        label="Crie uma Senha",
        hint_text="Digite sua nova senha",
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=10
    )

    register_view = ft.Column(
        visible=False,  # Começa invisível
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(name=ft.icons.PERSON_ADD, size=80),
            ft.Text("Crie sua Conta", size=32, weight=ft.FontWeight.BOLD),
            nome_register,
            email_register,
            senha_register,
            ft.ElevatedButton(
                text="Cadastrar",
                on_click=register_clicked,
                width=300,
                height=50,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Já tem uma conta?"),
                    ft.TextButton(text="Faça Login", on_click=show_login_view)
                ]
            )
        ]
    )

    # Adiciona as duas "telas" à página principal
    page.add(
        ft.Container(
            padding=30,
            border_radius=15,
            content=ft.Column(
                controls=[
                    login_view,
                    register_view
                ]
            )
        )
    )

    page.update()

# Inicia o aplicativo
if __name__ == "__main__":
    ft.app(target=main)
