from flask import Flask, render_template, request
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

app = Flask(__name__)

EXCLUDE_CHARS = 'il1Lo0O'

@app.route("/", methods=["GET", "POST"])
def index():
    passwords = []
    if request.method == "POST":
        use_lowercase = request.form.get("lowercase") == "on"
        use_uppercase = request.form.get("uppercase") == "on"
        use_digits = request.form.get("digits") == "on"
        use_symbols = request.form.get("symbols") == "on"
        exclude_chars = request.form.get("exclude") == "on"
        count = int(request.form.get("count", 1))
        length = int(request.form.get("length", 8))

        chars = ""
        if use_lowercase: chars += ascii_lowercase
        if use_uppercase: chars += ascii_uppercase
        if use_digits: chars += digits
        if use_symbols: chars += punctuation

        if exclude_chars:
            chars = ''.join(set(chars) - set(EXCLUDE_CHARS))

        if not chars:
            passwords.append("Ошибка: не выбраны символы для генерации.")
        else:
            for _ in range(count):
                password = ''.join(choice(chars) for _ in range(length))
                passwords.append(password)

    return render_template("index.html", passwords=passwords)

if __name__ == "__main__":
    app.run(debug=True)
