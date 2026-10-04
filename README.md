# Calculator TUI

A terminal calculator for arithmetic, powers, and common math functions.

## Features

- Basic arithmetic and parentheses
- Powers with `^` and square roots with `sqrt()`
- Trigonometric functions: `sin()`, `cos()`, and `tan()`
- `log()`, plus the constants `pi` and `e`
- Reuse the previous result with `ans`
- Clear memory with `clear` or exit with `quit`

## Installation

Install from PyPI:

```bash
python -m pip install calculator-tui
```

Or install from the GitHub source:

```bash
git clone https://github.com/13DoesPython/advanced-calculator.git
cd advanced-calculator
python -m pip install .
```

## Usage

Start the calculator in a terminal:

```bash
calculator-tui
```

At the prompt, enter an equation and press Enter. For example:

```text
[Formula/Command]: 2 + 3
Result: 5
[Formula/Command]: ans * 2
Result: 10
```

Use `^` for powers, such as `4^2`, and call functions like `sqrt(81)` or `sin(pi / 2)`. Enter `clear` to reset the saved answer, or `quit` to exit.