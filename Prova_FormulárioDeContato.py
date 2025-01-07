import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    def enviar(e):
        nome_contato = nome.value
        email_contato = email.value
        mensagem_contato = mensagem.value

        if nome_contato and email_contato and mensagem_contato:
            MensagemConfirmação.visible = True
            page.update()
            print(f"Nome: {nome_contato}, E-mail: {email_contato}, Mensagem: {mensagem_contato}")
    page.update()
    
    nome = ft.TextField(label="Nome", width=200)
    email = ft.TextField(label="E-mail", width=200)
    mensagem = ft.TextField(label="Mensagem", width=200, height=100, multiline=True)
    MensagemConfirmação = ft.Text("Formulario Enviado com Sucesso", color="green", visible=False)
    
    page.add(
        ft.Text("Formulário de Contato", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD, size="20px"),
        nome,
        email,
        mensagem,
        ft.ElevatedButton("Enviar", bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, width=200, height=50, on_click=enviar,),
        MensagemConfirmação
    )    
ft.app(target=main)