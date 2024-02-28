import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value='Hello, world!'))

    user_name = ft.TextField(label="Enter your name")

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([user_name], tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=user_name)],
        actions_alignment="end",
    )

ft.app(target=main)