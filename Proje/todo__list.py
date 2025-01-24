from flask import Flask, render_template, request, redirect, url_for
import os

print("Current directory:", os.getcwd())

app = Flask(__name__, template_folder="templates")

todos = [{"todo": "Sample Todo", "done": False}, {"todo": "Alisveris", "done": True}]
deleted_todos = []  

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"todo": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['todo'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    deleted_todos.append(todos.pop(index))
    return redirect(url_for("index"))

@app.route("/deleted")
def show_deleted():
    return render_template("deleted.html", deleted_todos=deleted_todos)

@app.route("/restore/<int:index>")
def restore(index):
    todo_to_restore = deleted_todos.pop(index)
    todos.append(todo_to_restore)
    return redirect(url_for("show_deleted"))
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
