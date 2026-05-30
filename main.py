import json, random, os
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    C = True
except ImportError:
    C = False
    class Fore:
        CYAN=YELLOW=GREEN=MAGENTA=RED=WHITE=""
    class Style:
        BRIGHT=RESET_ALL=""

def color(text, fore="", bright=False):
    if not C: return text
    return (Style.BRIGHT if bright else "") + fore + text + Style.RESET_ALL

def load_data():
    path = os.path.join(os.path.dirname(__file__), "tips.json")
    with open(path, "r") as f:
        return json.load(f)

def save_output(label, content, name):
    path = os.path.join(os.path.dirname(__file__), "output.txt")
    with open(path, "a") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {label} ({name}): {content}\n")

def banner():
    print(color("\n  ╔══════════════════════════════════════╗", Fore.CYAN, True))
    print(color("  ║    📚  Smart Student Assistant  📚   ║", Fore.CYAN, True))
    print(color("  ╚══════════════════════════════════════╝\n", Fore.CYAN, True))

def menu():
    print(color("\n  ┌─────────────────────────────────┐", Fore.YELLOW))
    print(color("  │          MAIN MENU              │", Fore.YELLOW, True))
    print(color("  │  1 ›  Study Tip                 │", Fore.YELLOW))
    print(color("  │  2 ›  Motivation Quote          │", Fore.YELLOW))
    print(color("  │  3 ›  Date & Time               │", Fore.YELLOW))
    print(color("  │  4 ›  Exit                      │", Fore.YELLOW))
    print(color("  └─────────────────────────────────┘", Fore.YELLOW))

def study_tip(data, name):
    tip = random.choice(data["study_tips"])
    print(color("\n  💡 Study Tip:", Fore.GREEN, True))
    print(color(f"  {tip}", Fore.WHITE))
    save_output("TIP", tip, name)
    print(color("  ✔ Saved to output.txt", Fore.CYAN))

def motivation(data, name):
    item = random.choice(data["motivation_quotes"])
    print(color("\n  🌟 Motivation:", Fore.MAGENTA, True))
    print(color(f'  "{item["quote"]}"', Fore.WHITE))
    print(color(f'  — {item["author"]}', Fore.MAGENTA))
    save_output("QUOTE", f'"{item["quote"]}" — {item["author"]}', name)
    print(color("  ✔ Saved to output.txt", Fore.CYAN))

def show_datetime(name):
    now = datetime.now()
    print(color("\n  🕒 Date & Time:", Fore.CYAN, True))
    print(color(f"  Date : {now:%A, %d %B %Y}", Fore.WHITE))
    print(color(f"  Time : {now:%I:%M:%S %p}", Fore.WHITE))
    save_output("DATETIME", f"{now:%Y-%m-%d %H:%M:%S}", name)
    print(color("  ✔ Saved to output.txt", Fore.CYAN))

def main():
    banner()
    name = input(color("  👋  Your name: ", Fore.CYAN, True)).strip() or "Student"

    h = datetime.now().hour
    greet = "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"
    print(color(f"\n  ✨  {greet}, {name}! Ready to learn?\n", Fore.GREEN, True))

    data = load_data()

    while True:
        menu()
        choice = input(color("\n  Choice (1-4): ", Fore.YELLOW)).strip()
        if   choice == "1": study_tip(data, name)
        elif choice == "2": motivation(data, name)
        elif choice == "3": show_datetime(name)
        elif choice == "4":
            print(color(f"\n  👋  Bye, {name}! Keep studying hard. 🎓\n", Fore.GREEN, True))
            break
        else:
            print(color("  ✘  Enter 1–4 only.", Fore.RED))

if __name__ == "__main__":
    main()
