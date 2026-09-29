from itertools import count

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")
task_ids = count(1)
tasks = []


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    completed: bool = False


class Task(TaskCreate):
    id: int


@app.get("/tasks", response_model=list[Task], summary="Listar tarefas")
def list_tasks():
    """Retorne todas as tarefas cadastradas."""
    pass


@app.post("/tasks", response_model=Task, status_code=201, summary="Criar tarefa")
def create_task(task: TaskCreate):
    """Crie uma tarefa validada pelo modelo Pydantic."""
    pass


@app.get("/tasks/{task_id}", response_model=Task, summary="Consultar tarefa")
def get_task(task_id: int):
    """Retorne uma tarefa pelo seu identificador."""
    pass


@app.put("/tasks/{task_id}", response_model=Task, summary="Atualizar tarefa")
def update_task(task_id: int, task_update: TaskCreate):
    """Atualize o título e o status de uma tarefa."""
    pass


@app.delete("/tasks/{task_id}", status_code=204, summary="Excluir tarefa")
def delete_task(task_id: int):
    """Exclua uma tarefa pelo seu identificador."""
    pass
