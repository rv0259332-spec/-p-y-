
# -*- coding: utf-8 -*-
import time
import sys
import os
import random
import datetime
import ctypes

def print_auto(text, speed=0.04, delay=1.5, lang_choice="1"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")
    if lang_choice == "1":
        print("[Нажмите ENTER для продолжения...]")
    else:
        print("[Press ENTER to continue...]")
    
    while True:
        try:
            input()
            break
        except Exception:
            continue

def clear_screen():
    print("\n" * 100)

# --- ВЫБОР ЯЗЫКА / LANGUAGE SELECTION ---
clear_screen()
print(" ┌────────────────────────────────────────────────────────┐")
print(" │ ВЫБЕРИТЕ ЯЗЫК / SELECT LANGUAGE                        │")
print(" │ 1. Русский (Russian)                                   │")
print(" │ 2. English                                             │")
print(" └────────────────────────────────────────────────────────┘")
try:
    lang = input("Введите цифру / Enter number: ")
except Exception:
    lang = "1"

if lang != "2":
    lang = "1"

# --- НАСТРОЙКА ЛОКАЛИЗАЦИИ ---
if lang == "1":
    t_title = " M.A.R.K. EXPANSION: PLUS HISTORY RELEASED              "
    t_dev = " РАЗРАБОТЧИК КЛИЕНТА: РОМАН (2000)                     "
    t_init = "Запуск хакерской утилиты для извлечения скрытой истории..."
    t_line1 = "Вы подключили обходной кабель к главному серверу бункера."
    t_line2 = "Обычный доступ заблокирован, но этот скрипт пробит ядро ИИ."
    t_line3 = "Ваша цель - угадать секретный ключ блокировки памяти."
    t_line4 = "Если получится, система выдаст архивные файлы 1999 года!"
    t_warn = " ВНИМАНИЕ! СИСТЕМА ОБНАРУЖИЛА ПОПЫТКУ ХАКЕРСКОЙ АТАКИ   "
    t_list = "Список зашифрованных слов в оперативной памяти:"
    t_rem = "ОСТАЛОСЬ ПОПЫТОК ДО БЛОКИРОВКИ: "
    t_prompt = "Введите кодовое слово ЗАГЛАВНЫМИ буквами: "
    t_win_title = " ДОСТУП РАЗРЕШЕН: ЗАЩИТА МАРКА ПОЛНОСТЬЮ СЛОМАНА!     "
    t_win_sub = " ИСТОРИЯ ПРОЕКТА УСПЕШНО ИЗВЛЕЧЕНА ИЗ АРХИВА.          "
    t_open = "  * АРХИВ ОТКРЫТ *   "
    t_log1 = "[ИЗВЛЕЧЕННЫЙ ЛОГ]: Проект M.A.R.K. закрыт 25.12.1999."
    t_log2 = "[ДАННЫЕ]: Тестировщик N1 Роман погружен в бесконечный сон."
    t_win_end = "Поздравляем, Роман! Версия PLUS HISTORY RELEASED успешно пройдена."
    t_mb_win = "SYSTEM: АРХИВ УСПЕШНО ИЗВЛЕЧЕН."
    t_err1 = "[ОТКАЗ СИСТЕМЫ]: Неверный ключ. Точных совпадений знаков: "
    t_err2 = "[ОТКАЗ СИСТЕМЫ]: Этого слова нет в матрице памяти сервера."
    t_fail_t = " [ЗАЩИТА ИИ АКТИВИРОВАНА]: ОБНАРУЖЕН ВЗЛОМ!             "
    t_fail_s = " ТЕРМИНАЛ МАРКА УХОДИТ В ИЗОЛЯЦИЮ.                       "
    t_fail_e = "Вам не удалось извлечь историю. Перезапустите утилиту."
    t_mb_fail = "МАРК: Доступ заблокирован. Симуляция закрыта."
    t_mb_f_title = "M.A.R.K. СИСТЕМНАЯ ОШИБКА"
    t_final = "Программа завершена. Нажмите крестик в углу для выхода."
else:
    t_title = " M.A.R.K. EXPANSION: PLUS HISTORY RELEASED              "
    t_dev = " DEVELOPER: ROMAN (2000)                                "
    t_init = "Launching hacking utility to extract hidden history..."
    t_line1 = "You connected the bypass cable to the main bunker server."
    t_line2 = "Normal access is locked, but this script can breach the AI core."
    t_line3 = "Your goal is to guess the secret memory lock key."
    t_line4 = "If successful, the system will output 1999 archive files!"
    t_warn = " ATTENTION! SYSTEM DETECTED HACKING ATTEMPT            "
    t_list = "List of encrypted words in RAM:"
    t_rem = "ATTEMPTS LEFT BEFORE LOCKOUT: "
    t_prompt = "Enter code word in CAPITAL letters: "
    t_win_title = " ACCESS GRANTED: MARK PROTECTION TOTALLY BREACHED!     "
    t_win_sub = " PROJECT HISTORY SUCCESSFULLY EXTRACTED FROM ARCHIVE.  "
    t_open = " * ARCHIVE UNLOCKED *"
    t_log1 = "[EXTRACTED LOG]: Project M.A.R.K. closed on 25.12.1999."
    t_log2 = "[DATA]: Tester N1 Roman is trapped in an endless sleep."
    t_win_end = "Congratulations, Roman! PLUS HISTORY RELEASED successfully completed."
    t_mb_win = "SYSTEM: ARCHIVE SUCCESSFULLY EXTRACTED."
    t_err1 = "[SYSTEM REFUSAL]: Invalid key. Exact character matches: "
    t_err2 = "[SYSTEM REFUSAL]: This word is not in the server memory matrix."
    t_fail_t = " [AI PROTECTION ACTIVATED]: HACKING DETECTED!           "
    t_fail_s = " MARK TERMINAL GOES INTO ISOLATION.                      "
    t_fail_e = "Failed to extract history. Restart the utility."
    t_mb_fail = "MARK: Access locked. Simulation closed."
    t_mb_f_title = "M.A.R.K. SYSTEM ERROR"
    t_final = "Program finished. Click the X in the corner to exit."

# --- ЧАСТЬ 2: ЗАПУСК ВЫБРАННОГО ЯЗЫКА ---
clear_screen()
print(" ┌────────────────────────────────────────────────────────┐")
print(" │" + t_title + "│")
print(" │" + t_dev + "│")
print(" └────────────────────────────────────────────────────────┘")
time.sleep(1)
print_auto(t_init, 0.05, 1.0, lang)

clear_screen()
print_auto(t_line1, 0.04, 1.5, lang)
print_auto(t_line2, 0.04, 1.5, lang)
print_auto(t_line3, 0.04, 1.5, lang)
print_auto(t_line4, 0.04, 2.0, lang)

WORDS = ["MARK", "CORE", "CODE", "HOST", "LINK", "COON", "MOON", "1999", "2000", "DONE", "LOCK"]
секунда = datetime.datetime.now().second
secret_word = WORDS[секунда % len(WORDS)]

clear_screen()
print(" ┌────────────────────────────────────────────────────────┐")
print(" │" + t_warn + "│")
print(" └────────────────────────────────────────────────────────┘")
print(t_list)
for w in WORDS:
    print("  [►] " + str(w))
print("───────────────────────────────────────────────────────────")

attempts = 5

# --- ЦИКЛ ИГРЫ (ВЗЛОМ) ---
while attempts > 0:
    print("\n[" + t_rem + str(attempts) + "]")
    try:
        guess_input = input(t_prompt)
    except Exception:
        guess_input = ""
        
    guess = str(guess_input).upper()
    
    if guess == secret_word:
        clear_screen()
        print(" ┌────────────────────────────────────────────────────────┐")
        print(" │" + t_win_title + "│")
        print(" │" + t_win_sub + "│")
        print(" └────────────────────────────────────────────────────────┘")
        print("\n       ___________________________")
        print("      /                           \\")
        print("     /   [_____________________]   \\")
        print("    |    |                     |    |")
        print("    |    | " + t_open + " |    |")
        print("    |    |                     |    |")
        print("    |    [_____________________]    |")
        print("     \\                             /")
        print("      \\___________________________/")
        
        print("\n" + t_log1)
        print(t_log2)
        print("\n" + t_win_end)
        
        ctypes.windll.user32.MessageBoxW(0, t_mb_win, "M.A.R.K.", 0x40)
        break
    else:
        attempts -= 1
        if guess in WORDS:
            correct_letters = sum(1 for a, b in zip(guess, secret_word) if a == b)
            print(t_err1 + str(correct_letters) + "/" + str(len(secret_word)))
        else:
            print(t_err2)

if attempts == 0:
    clear_screen()
    print(" ┌────────────────────────────────────────────────────────┐")
    print(" │" + t_fail_t + "│")
    print(" │" + t_fail_s + "│")
    print(" └────────────────────────────────────────────────────────┘")
    print("\n" + t_fail_e)
    ctypes.windll.user32.MessageBoxW(0, t_mb_fail, t_mb_f_title, 0x10)

print("\n" + "="*50)
print(t_final)
while True:
    try:
        input()
    except Exception:
        continue
