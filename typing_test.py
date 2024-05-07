import curses
from curses import wrapper
import time as t
import random as r


def start_screen(std_scr) -> None:
    std_scr.clear()
    std_scr.addstr("Welcome to the Speed Typing Test!")
    std_scr.addstr("\nPress any key to begin!")
    std_scr.refresh()
    std_scr.getkey()


def display_text(std_scr, target, current, wpm=0.0) -> None:
    std_scr.addstr(target)
    std_scr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)

        if char != correct_char:
            color = curses.color_pair(2)

        std_scr.addstr(0, i, char, color)


def pick_up_random_line() -> str:
    with open("words.txt", "r") as f:
        return r.choice(
            f.readlines()
        ).strip()


def wpm_test(std_scr):
    """
    The sun rose over the horizon, casting golden hues across the landscape.
    Birds chirped melodiously in the treetops, welcoming the new day.
    A gentle breeze rustled through the leaves, carrying the scent of fresh flowers.
    The river flowed quietly beside the winding path, reflecting the morning light.
    In the distance, mountains loomed majestically against the clear blue sky.
    A lone traveler walked along the path, taking in the serene surroundings.
    The air was crisp and clean, invigorating the senses with each breath.
    Wildflowers dotted the meadow, painting it with vibrant colors.
    A deer emerged from the forest, pausing to drink from the clear stream.
    Nature was alive with activity, a symphony of sights and sounds.
    """

    target_text = pick_up_random_line()
    current_text = []
    start_time = t.time()
    std_scr.nodelay(True)

    while True:
        time_elapsed = max(t.time() - start_time, 1)
        wpm = round(
                len(target_text) / (time_elapsed / 60) / 5
        )

        std_scr.clear()
        display_text(std_scr, target_text, current_text, wpm)
        std_scr.refresh()

        if "".join(current_text) == target_text:
            std_scr.nodelay(False)
            break

        try:
            key = std_scr.getkey()
        except:
            continue

        # If 'Esc' button is pressed - exit loop
        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(std_scr) -> None:
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(std_scr)
    while True:
        wpm_test(std_scr)
        std_scr.addstr(2, 0, "You completed the test! Press any key to continue.")
        key = std_scr.getkey()

        # Finish of this test
        if ord(key) == 27:
            break


wrapper(main)
