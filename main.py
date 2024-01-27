# Modified from: https://github.com/taaaf11/Calculator
import flet as ft


def main(page):
    page.title = "Calculator"

    page.window_width = 310
    page.window_height = 350
    page.window_resizable = False

    page.theme_mode = ft.ThemeMode.DARK

    def textfield_to_eval_able_string(string: str):
        eval_able_str = ""
        for char in string:
            if char == "÷":
                eval_able_str += "/"
                continue
            elif char == "x":
                eval_able_str += "*"
                continue
            eval_able_str += char

        if eval_able_str[0] == "0":
            eval_able_str = eval_able_str[1:]
        return eval_able_str


    def on_click_num(number):
        def handler(e):
            if entry_label.value == "0":
                entry_label.value = ""
            entry_label.value += str(number)
            page.update()
        return handler

    on_click_0 = on_click_num(0)
    on_click_1 = on_click_num(1)
    on_click_2 = on_click_num(2)
    on_click_3 = on_click_num(3)
    on_click_4 = on_click_num(4)
    on_click_5 = on_click_num(5)
    on_click_6 = on_click_num(6)
    on_click_7 = on_click_num(7)
    on_click_8 = on_click_num(8)
    on_click_9 = on_click_num(9)

    def on_click_c_or_ac(e):
        entry_label.value = "0"
        page.update()

    def on_click_add(e):
        entry_label.value += "+"
        page.update()
        
    def on_click_sub(e):
        entry_label.value += "-"
        page.update()

    def on_click_mul(e):
        entry_label.value += "x"
        page.update()

    def on_click_div(e):
        entry_label.value += "÷"
        page.update()

    def on_click_point(e):
        if entry_label.value == "0":
            entry_label.value = ""
        entry_label.value += "."
        page.update()

    def on_click_equals(e):
        result = eval(textfield_to_eval_able_string(entry_label.value))
        entry_label.value = str(result)
        page.update()

    def set_dark_mode():
        page.theme_mode = ft.ThemeMode.DARK
        for button in all_buttons:
            if isinstance(button, ft.IconButton):
                button.icon_color = "#ffffff"
                button.bgcolor = "#191b1e"
                continue
            button.bgcolor = "#121212"
            button.color = "#ffffff"
        button_change_theme.icon = ft.icons.LIGHT_MODE_SHARP
        page.update()

    def set_light_mode():
        page.theme_mode = ft.ThemeMode.LIGHT
        for button in all_buttons:
            if isinstance(button, ft.IconButton):
                button.icon_color = "#ffffff"
                button.bgcolor = "#919699"
                continue
            button.bgcolor = "#919699"
            button.color = "#ffffff"
        button_change_theme.icon = ft.icons.DARK_MODE_SHARP
        page.update()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            set_dark_mode()
        elif page.theme_mode == ft.ThemeMode.DARK:
            set_light_mode()

    def delete_char(e):
        if len(entry_label.value) == 1:  # the only character in the field
            entry_label.value = "0"
        else:
            entry_label_value = list(entry_label.value)
            entry_label.value = "".join(entry_label_value[:-1])
        page.update()

    button_C = ft.ElevatedButton(text="C", on_click=on_click_c_or_ac)
    button_AC = ft.ElevatedButton(text="AC", on_click=on_click_c_or_ac)
    button_delete = ft.IconButton(ft.icons.BACKSPACE, on_click=delete_char)
    button_add = ft.ElevatedButton(text="+", on_click=on_click_add)

    button_7 = ft.ElevatedButton(text="7", on_click=on_click_7)
    button_8 = ft.ElevatedButton(text="8", on_click=on_click_8)
    button_9 = ft.ElevatedButton(text="9", on_click=on_click_9)
    button_sub = ft.ElevatedButton(text="-", on_click=on_click_sub)

    button_4 = ft.ElevatedButton(text="4", on_click=on_click_4)
    button_5 = ft.ElevatedButton(text="5", on_click=on_click_5)
    button_6 = ft.ElevatedButton(text="6", on_click=on_click_6)
    button_mul = ft.ElevatedButton(text="x", on_click=on_click_mul)

    button_1 = ft.ElevatedButton(text="1", on_click=on_click_1)
    button_2 = ft.ElevatedButton(text="2", on_click=on_click_2)
    button_3 = ft.ElevatedButton(text="3", on_click=on_click_3)
    button_div = ft.ElevatedButton(text="÷", on_click=on_click_div)

    button_0 = ft.ElevatedButton(text="0", on_click=on_click_0)
    button_point = ft.ElevatedButton(text=".", on_click=on_click_point)
    button_change_theme = ft.IconButton(
        ft.icons.LIGHT_MODE_SHARP, on_click=change_theme
    )
    button_equals = ft.ElevatedButton(text="=", on_click=on_click_equals)

    all_buttons = [
        button_C,
        button_AC,
        button_delete,
        button_add,
        button_7,
        button_8,
        button_9,
        button_sub,
        button_4,
        button_5,
        button_6,
        button_mul,
        button_1,
        button_2,
        button_3,
        button_div,
        button_0,
        button_point,
        button_change_theme,
        button_equals,
    ]

    entry_label = ft.TextField(value="0", read_only=True)
    row_1 = ft.Row([button_C, button_AC, button_delete, button_add])
    row_2 = ft.Row([button_7, button_8, button_9, button_sub])
    row_3 = ft.Row([button_4, button_5, button_6, button_mul])
    row_4 = ft.Row([button_1, button_2, button_3, button_div])
    row_5 = ft.Row([button_0, button_point, button_change_theme, button_equals])

    view = ft.Column([entry_label, row_1, row_2, row_3, row_4, row_5])

    # initial theme mode of the app
    set_dark_mode()

    page.add(view)


if __name__ == "__main__":
    ft.app(target=main)