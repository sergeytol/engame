#!/usr/bin/env python3
import os
import random
from time import sleep


def load_lines():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/5000_words.txt", "r") as file:
        return file.read().splitlines()


def mask_word(word, mask_count=1):
    count = 0
    masked_word = word
    while count < mask_count:
        index = random.randint(0, len(word)-1)
        if masked_word[index] != '.':
            masked_word = masked_word[:index] + '.' + masked_word[index + 1:]
            count += 1
    return masked_word


def main_loop():
    lines = load_lines()
    lines_count = len(lines)

    while True:
        line = lines[random.randint(0, lines_count - 1)]
        word, translation = [x.strip('"') for x in line.split(";")]
        masked_word = mask_word(word, mask_count=2)

        print(f"Слово: {masked_word}")
        print(f"Перевод: {translation}")
        answer = input("Введите ответ: ")
        if not answer:
            print("\033[93mПравильный ответ: ", f"{word} - {translation}")
        elif word.lower() == answer.lower():
            print("\033[92mПравильно!", f"{word} - {translation}")
        else:
            print("\033[91mНе правильно.", f"{word} - {translation}")
        sleep(1)
        print("\033[0m")


if __name__ == "__main__":
    main_loop()
