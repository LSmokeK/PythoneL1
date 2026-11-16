from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def resume():
    return render_template("resume.html", title="Євгеній Вербицький — резюме")


@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    submitted = False
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        submitted = bool(name and email and message)
    return render_template("contacts.html", title="Контакти — Євгеній Вербицький", submitted=submitted)


if __name__ == "__main__":
    app.run(debug=True)
