from flask import Flask, render_template, request, redirect, session, flash
import os

app = Flask(__name__)
app.secret_key = "driftwood_secret_key"

# Environment (DEV by default, can override with ENV_NAME variable)
app.config["ENV_NAME"] = os.environ.get("ENV_NAME", "DEV")

@app.context_processor
def inject_env():
    return dict(env_name=app.config["ENV_NAME"])

# Hardcoded users
users = {
    "curator": {"password": "curator123", "role": "curator"},
    "artisan": {"password": "artisan123", "role": "artisan"}
}

# In-memory task list
tasks = []


@app.route("/")
def home():
    if "username" in session:
        if session["role"] == "curator":
            return redirect("/curator")
        else:
            return redirect("/artisan")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["username"] = username
            session["role"] = users[username]["role"]
            flash("Login successful!", "success")
            return redirect("/")
        else:
            flash("Invalid credentials", "error")
            return redirect("/login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect("/login")


@app.route("/curator", methods=["GET", "POST"])
def curator_dashboard():
    if "username" not in session or session["role"] != "curator":
        return redirect("/login")

    if request.method == "POST":
        task_title = request.form["task"]

        # Create task with proper ID
        tasks.append({
            "id": len(tasks),
            "title": task_title,
            "completed": False
        })

        flash("Task created successfully!", "success")
        return redirect("/curator")

    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks) * 100) if tasks else 0

    return render_template(
        "curator.html",
        tasks=tasks,
        progress=progress,
        env_name=app.config["ENV_NAME"]
    )


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if "username" not in session or session["role"] != "artisan":
        return redirect("/login")

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            flash("Task marked as complete!", "success")
            break

    return redirect("/artisan")


@app.route("/artisan")
def artisan_dashboard():
    if "username" not in session or session["role"] != "artisan":
        return redirect("/login")

    return render_template(
        "artisan.html",
        tasks=tasks,
        env_name=app.config["ENV_NAME"]
    )

@app.route("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": app.config["ENV_NAME"]
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
