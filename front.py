import flet as ft
import requests

# Функция для получения слова из API
def get_word():
    response = requests.get("http://127.0.0.1:8000/word")
    if response.status_code == 200:
        data = response.json()
        return data["word"]
    return None

# Функция для отправки ответа на API
def submit_answer(answer: str):
    response = requests.get(f"http://127.0.0.1:8000/task?answer={answer}")
    if response.status_code == 200:
        data = response.json()
        return data["message"]
    return "Ошибка при отправке ответа"

# Главная функция для создания интерфейса
def main(page: ft.Page):
    page.title = "Тренировка ЕГЭ по русскому"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Метки для отображения информации
    word_label = ft.Text("Слово появится здесь", size=24, color=ft.colors.BLUE_GREY)
    result_label = ft.Text("", size=20, color=ft.colors.BLUE_GREY)  # Изначально пустая

    # Функция для обновления слова
    def update_word(e):
        # Очищаем предыдущий результат
        result_label.value = ""
        word_label.value = "Загрузка слова..."
        page.update()
        word = get_word()
        if word:
            word_label.value = f"Слово: {word}"
        else:
            word_label.value = "Ошибка при получении слова"
        page.update()

    # Функция для обработки нажатия кнопки "Слитно"
    def on_slitno_click(e):
        result_label.value = "Отправка ответа..."
        page.update()
        result = submit_answer("Слитно")
        result_label.value = result
        page.update()

    # Функция для обработки нажатия кнопки "Раздельно"
    def on_razdelno_click(e):
        result_label.value = "Отправка ответа..."
        page.update()
        result = submit_answer("Раздельно")
        result_label.value = result
        page.update()

    # Кнопка для получения слова (сдержанный синий-серый)
    word_button = ft.ElevatedButton(
        "Получить слово",
        on_click=update_word,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#607D8B"
        )
    )
    # Кнопка "Слитно" (мягкий зелёный)
    slitno_button = ft.ElevatedButton(
        "Слитно",
        on_click=on_slitno_click,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#8BC34A"
        )
    )
    # Кнопка "Раздельно" (мягкий красный)
    razdelno_button = ft.ElevatedButton(
        "Раздельно",
        on_click=on_razdelno_click,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=ft.colors.WHITE,
            bgcolor="#E57373"
        )
    )

    # Группируем кнопки "Слитно" и "Раздельно" в одну строку и центрируем их
    answer_buttons_row = ft.Row(
        controls=[slitno_button, razdelno_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Выравниваем элементы по центру
    page.add(
        ft.Column(
            controls=[
                word_button,
                word_label,
                answer_buttons_row,
                result_label
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# Запуск приложения
ft.app(target=main, view=ft.WEB_BROWSER)
