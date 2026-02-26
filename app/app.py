from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Barista Task List ☕</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f1ea;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #6b3e26;
            }
            input {
                padding: 10px;
                width: 250px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                padding: 8px 12px;
                background: #6b3e26;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-left: 5px;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: white;
                margin: 10px auto;
                padding: 10px;
                width: 320px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <h1>☕ Barista Task List</h1>

        <input type="text" id="taskInput" placeholder="Enter new task">
        <button onclick="addTask()">Add</button>

        <ul id="taskList"></ul>

        <script>
            async function fetchTasks() {
                const response = await fetch('/tasks');
                const tasks = await response.json();
                const list = document.getElementById('taskList');
                list.innerHTML = '';

                tasks.forEach(task => {
                    const li = document.createElement('li');

                    let text = task.task;
                    if (task.status === "completed") {
                        text = "<s>" + task.task + "</s>";
                    }

                    li.innerHTML = text +
                        ' <button onclick="toggleTask(' + task.id + ')">✔</button>' +
                        ' <button onclick="deleteTask(' + task.id + ')">❌</button>';

                    list.appendChild(li);
                });
            }

            async function addTask() {
                const input = document.getElementById('taskInput');
                if (!input.value) return;

                await fetch('/tasks', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({task: input.value})
                });

                input.value = '';
                fetchTasks();
            }

            async function deleteTask(id) {
                await fetch('/tasks/' + id, {method: 'DELETE'});
                fetchTasks();
            }

            async function toggleTask(id) {
                await fetch('/tasks/' + id + '/toggle', {method: 'PUT'});
                fetchTasks();
            }

            fetchTasks();
        </script>
    </body>
    </html>
    """

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "task": data.get("task"),
        "status": "pending"
    }
    tasks.append(task)
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

@app.route("/tasks/<int:task_id>/toggle", methods=["PUT"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "pending":
                task["status"] = "completed"
            else:
                task["status"] = "pending"
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
