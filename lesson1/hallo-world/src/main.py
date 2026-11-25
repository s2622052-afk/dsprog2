import flet as ft


def main(page: ft.Page):

    hallo_world = ft.Text("Hallo World", size=50)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    def decrement_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data -= 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, key="increment", on_click=increment_click)

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=ft.Column(controls=[hallo_world, counter], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
            ),
        ),
        ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decrement", on_click=decrement_click),
    )


if __name__ == "__main__":
    ft.run(main)
