import flet as ft
import requests

def get_word():
    response = requests.get("http://127.0.0.1:8000/word")
    if response.status_code == 200:
        return response.json()["word"]
    return None

def submit_answer(answer: str):
    response = requests.get(f"http://127.0.0.1:8000/task?answer={answer}")
    if response.status_code == 200:
        return response.json()["message"]
    return "Ошибка при отправке ответа"

def main(page: ft.Page):
    page.title = "Тренировка ЕГЭ по русскому"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    word_label = ft.Text("Слово появится здесь", size=24, color=ft.colors.BLUE_GREY)
    result_label = ft.Text("", size=20, color=ft.colors.BLUE_GREY)

    def update_word():
        word = get_word()
        if word:
            word_label.value = f"Слово: {word}"
        else:
            word_label.value = "Ошибка при получении слова"
        page.update()

    def on_answer_click(answer):
        result = submit_answer(answer)
        if result == "Верно!":
            result_label.value = "Верно!"
            update_word()  # Обновляем слово
        else:
            result_label.value = result  # Сообщаем о неправильном ответе
        page.update()

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "ArrowLeft":  # Стрелка влево
            on_answer_click("Слитно")
        elif e.key == "ArrowRight":  # Стрелка вправо
            on_answer_click("Раздельно")

    word_button = ft.ElevatedButton(
        "Получить слово",
        on_click=lambda e: update_word(),
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#607D8B"
        )
    )

    slitno_button = ft.ElevatedButton(
        "Слитно",
        on_click=lambda e: on_answer_click("Слитно"),
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#8BC34A"
        )
    )

    razdelno_button = ft.ElevatedButton(
        "Раздельно",
        on_click=lambda e: on_answer_click("Раздельно"),
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#E57373"
        )
    )

    answer_buttons_row = ft.Row(
        controls=[slitno_button, razdelno_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    main_content = ft.Column(
        controls=[word_button, word_label, answer_buttons_row, result_label],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Добавляем обработчик событий клавиатуры к странице:
    page.on_keyboard_event = on_keyboard

    page.add(main_content)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
