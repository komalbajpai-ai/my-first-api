from flask import Flask, request

app = Flask(__name__)

todos = []

@app.get("/hello")
def hello():
    return {"message": "Hello! My first API works."}

@app.get("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"result": a + b}

@app.get("/me")
def me():
    return {"name": "Komal Bajpai", "job_title": "Product Support Engineer"}

@app.get("/todos")
def list_todos():
    return {"todos": todos}

@app.post("/todos")
def add_todo():
    data = request.get_json()
    todo = {"id": len(todos) + 1, "task": data["task"], "done": False}
    todos.append(todo)
    return todo, 201

if __name__ == "__main__":
    app.run(port=5000)