# Calculator TUI

A terminal calculator for arithmetic, powers, and common math functions.

## Features

- Basic arithmetic and parentheses
- Powers with `^` and square roots with `sqrt()`
- Trigonometric functions: `sin()`, `cos()`, and `tan()`
- `log()`, plus the constants `pi` and `e`
- Reuse the previous result with `ans`
- Clear memory with `clear` or exit with `quit`

## Get the files

Clone the GitHub repository and enter its folder:

```bash
git clone https://github.com/13DoesPython/advanced-calculator.git
cd advanced-calculator
```

## Usage

From inside the cloned `advanced-calculator` folder, run `calc_tui.py`:

```bash
python calc_tui.py
```

At the prompt, enter an equation and press Enter. For example, `2 + 3` returns `5`. Use `ans` to reuse the last result, `clear` to reset memory, or `quit` to exit. The program requires Python 3.10 or newer and Colorama.