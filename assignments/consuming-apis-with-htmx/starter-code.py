from html import escape
from itertools import count
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI(title="HTMX Task Board")
base_dir = Path(__file__).parent
task_ids = count(3)
tasks = [
    {"id": 1, "title": "Conhecer o HTMX", "completed": True},
    {"id": 2, "title": "Criar uma tarefa", "completed": False},
]


def render_task(task):
    status = "completed" if task["completed"] else "pending"
    button_label = "Reabrir" if task["completed"] else "Concluir"
    return f"""<li id=\"task-{task['id']}\" class=\"{status}\">
  <span>{escape(task['title'])}</span>
  <button>{button_label}</button>
</li>"""


@app.get("/", response_class=FileResponse)
def home():
    return FileResponse(base_dir / "index.html")


@app.get("/tasks", response_class=HTMLResponse)
def list_tasks():
    return "".join(render_task(task) for task in tasks)


@app.post("/tasks", response_class=HTMLResponse)
def create_task(title: str = Form(...)):
    task = {"id": next(task_ids), "title": title, "completed": False}
    tasks.insert(0, task)
    return render_task(task)


@app.patch("/tasks/{task_id}/complete", response_class=HTMLResponse)
def complete_task(task_id: int):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    task["completed"] = not task["completed"]
    return render_task(task)
