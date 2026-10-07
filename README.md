# Calculator

A web calculator built with Python and Node.js. The browser sends the numbers to a small Node.js server, which runs a Python script to do the math and sends the answer back.

## Features

- Calculator-style button layout
- Operators: `+`, `-`, `*`, `/`, `%`, and `^` (power)
- Keyboard support (digits, operators, Enter, Backspace, Escape)
- Error handling, such as division by zero

## How it works

```
Browser (index.html)  ->  Node.js (server.js)  ->  Python (calculator.py)
```

1. Clicking `=` sends the numbers and operator to `/calc`.
2. `server.js` runs `calculator.py` with those values.
3. Python prints the result, and Node sends it back to the page.

## Requirements

- [Node.js](https://nodejs.org)
- [Python 3](https://www.python.org)

## Run it

```
git clone https://github.com/[your-username]/calculator.git
cd calculator
node server.js
```

Then open http://localhost:3000 in your browser.

If `python` isn't recognized on your computer, change `"python"` to `"py"` in `server.js`.

## Project files

| File | Purpose |
|---|---|
| `calculator.py` | The math, run from the command line |
| `server.js` | Web server that connects the page to Python |
| `index.html` | The calculator interface |

## What I learned

[How to build using python and how to style it.]