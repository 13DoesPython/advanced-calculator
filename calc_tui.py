import math
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def evaluate_expression(expression: str):
    allowed_chars = set("0123456789+-*/().,^ ")
    words = "".join(c if c.isalpha() else " " for c in expression).split()

    allowed_words = {"sin", "cos", "tan", "sqrt", "log", "pi", "e", "ans", "factorial"}
    for word in words:
        if word not in allowed_words:
            raise ValueError(f"Unknown function or variable: '{word}")

    for char in expression:
        if char not in allowed_chars and not char.isalpha():
            raise ValueError(f"Invalid char: '{char}")

    safe_dict = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e,
        "factorial": math.factorial,
        "ans": LAST_ANS
    }

    evaluated_expression = expression.replace("^", "**")
    result = eval(evaluated_expression, {"__builtins__": {}}, safe_dict)

    if callable(result):
        raise ValueError("Call the function with parentheses, like sin(pi / 2).")

    return result

LAST_ANS = 0.0

def help_menu():
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[3J")
        sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "=" * 50)
    print(Style.BRIGHT + Fore.CYAN + "Help Guide".center(50))
    print(Fore.CYAN + "=" * 50)
    print("- Basic arithmetic: Use +, -, *, / for addition, subtraction, multiplication, and division.")
    print("- Power: Use ^ for exponentiation. Example: 2^3 = 8")
    print("- Square root: Use sqrt(). Example: sqrt(16) = 4")
    print("- Factorial: Use factorial(). Example: factorial(5) = 120")
    print("- Trigonometric functions: sin(), cos(), tan() accept radians. Example: sin(pi/2) = 1")
    print("- Logarithm: Use log() for natural logarithm. Example: log(e) = 1")
    print("- Constants: Use pi and e for mathematical constants.")
    print("- Memory: Use 'ans' to refer to the last answer.")
    print("- Commands: Type 'quit' to exit or 'clear' to reset memory.")
    print(Fore.CYAN + "=" * 50)

def print_menu():
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[3J")
        sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "=" * 50)
    print(Style.BRIGHT + Fore.CYAN + "Advanced terminal calculator".center(50))
    print(Fore.CYAN + "=" * 50)
    print("- Basic arithmetic equations! '1 + 1 / 2'")
    print("- Power and square root! '4^2 + sqrt(16)'")
    print("- Math functions! sin(), cos(), tan(), log()")
    print("- Irrational numbers! pi and e")
    print("- Commands! 'quit' to quit and 'clear' to clear memory")
    print("- Use 'ans' to go back to the last answer!")
    print("- Full help guide with command 'help'")
    print(Fore.CYAN + "=" * 50)

def main():
    global LAST_ANS
    message = ""

    while True:
        print_menu()
        if message:
            message_color = Fore.RED if message.startswith("Error:") else Fore.GREEN
            print(message_color + message)

        try:
            user_input = input(Fore.CYAN + "[Formula/Command]: " + Fore.WHITE).strip().lower()

            if user_input == "quit":
                sys.exit(0)

            if user_input == "clear":
                LAST_ANS = 0
                message = "Memory cleared!"
                continue

            if user_input == "help":
                help_menu()
                input(Fore.CYAN + "Press Enter to return to the main menu...")
                continue
            
            result = evaluate_expression(user_input)
            LAST_ANS = result

            display_result = result
            if isinstance(display_result, float):
                if display_result.is_integer():
                    display_result = int(display_result)
                else:
                    display_result = round(display_result, 6)
                
            message = f"Result: {display_result}"

        except EOFError:
            return
        except ZeroDivisionError:
            message = "Error: Cannot divide by zero!"
        except (ValueError, SyntaxError) as e:
            message = f"Error: Check your math formulation '{e}'"
        except Exception as e:
            message = f"Error: {e}"

if __name__ == "__main__":
    main()