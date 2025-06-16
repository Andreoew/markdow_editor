import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.title = 'Markdown Editor'
    page.theme_mode = ft.ThemeMode.DARK
    
    def update_view(e):
        view.value = editor.value
        view.update()
        
    def copy_to_clipboard(e):
        page.set_clipboard(editor.value)
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Markdown copiado para a área de transferência!"),
            bgcolor=ft.Colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        text="Copiar Markdown",
        icon=ft.Icons.CONTENT_COPY,
        on_click=copy_to_clipboard,
        
    )
        
    editor = ft.TextField(
        multiline=True,
        min_lines=20,
        content_padding=ft.padding.all(30),
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.BLUE_GREY_700,
        color=ft.Colors.BLACK,
        on_change=update_view,
        
    )

    
    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Text(value='Para criar títulos em diferentes tamanhos', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(value='# H1', color=ft.Colors.GREY_700),
                ft.Text(value='## H2', color=ft.Colors.GREY_700),
                ft.Text(value='### H3', color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),

                ft.Text(value='Para formatar o estilo do texto', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(value='**Texto em negrito**', color=ft.Colors.GREY_700),
                ft.Text(value='*Texto em itálico*', color=ft.Colors.GREY_700),
                ft.Text(value='~~Texto tachado~~', color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),

                ft.Text(value='Para criar listas', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(value='1. Ordenada', color=ft.Colors.GREY_700),
                ft.Text(value='- Desordenada', color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),

                ft.Text(value='Inserir links e imagens', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(value='[Texto do link](https://adss.com.br)', color=ft.Colors.GREY_700),
                ft.Text(value='![Label da imagem](image.jpg)', color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),

                ft.Text(value='Para inserir código', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Text(value='`print("Código em uma linha")`', color=ft.Colors.GREY_700),
                ft.Text(value='```\nprint("Código em mútiplas linhas") \n```', color=ft.Colors.GREY_700),
            ]
        )
    )
    
    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link=lambda e: page.launch_url(e.data),        
    )
    
    layout = ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,                        
                        how_to,
                    ]
                )
            ),
            ft.Container(
                expand=True,
                padding=ft.padding.all(30),
                bgcolor=ft.Colors.BLACK,                
                content=ft.Column(
                    controls=[
                        view,
                    ]
                )
            ),
        ]
    )
    
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target=main)