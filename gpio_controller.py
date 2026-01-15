#!/usr/bin/env python3
import time
from gpiozero import Button
from pynput.keyboard import Key, Controller

# Инициализация виртуальной клавиатуры
keyboard = Controller()

# Настройка кнопок (GPIO номера могут отличаться в зависимости от схемы)
btn_up    = Button(5,  pull_up=True, bounce_time=0.05)
btn_down  = Button(6,  pull_up=True, bounce_time=0.05)
btn_left  = Button(13, pull_up=True, bounce_time=0.05)
btn_right = Button(19, pull_up=True, bounce_time=0.05)

print("Система управления запущена. Нажмите кнопки для управления.")

try:
    while True:
        if btn_up.is_pressed:
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        if btn_down.is_pressed:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        if btn_left.is_pressed:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        if btn_right.is_pressed:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        time.sleep(0.05)  # небольшая задержка для снижения нагрузки
except KeyboardInterrupt:
    print("\nВыход.")