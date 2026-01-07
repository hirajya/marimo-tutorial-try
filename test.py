import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", layout_file="layouts/test.slides.json")


@app.cell
def _():
    import marimo as mo

    mo.md("# Welcome to marimo!🥀")
    return (mo,)


@app.cell
def _(mo):
    text_input = "rodney"
    mo.md(f"Enter some text: {text_input}")
    return


@app.cell
def _():
    a = 3 
    b = 4
    print(a + b)
    return


@app.cell
def _():
    _a = 5
    return


@app.cell
def _():
    # lazy mode
    y = 36
    z = 20
    return y, z


@app.cell
def _(y, z):
    y + z
    return


@app.cell
def _(mo):
    icon = mo.ui.dropdown(["🥰", "😎", "🤖"], value="😎")
    return (icon,)


@app.cell
def _(icon, mo):
    repetitions = mo.ui.slider(1, 16, label=f"number of {icon.value}:")
    return (repetitions,)


@app.cell
def _(icon, repetitions):
    icon, repetitions
    return


@app.cell
def _(icon, mo, repetitions):
    mo.md("# " + icon.value * repetitions.value)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
