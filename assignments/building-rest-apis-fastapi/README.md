# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Você aprenderá a construir uma API REST usando o framework FastAPI. Ao final, sua API permitirá criar, consultar, atualizar e remover tarefas, com validação de dados e documentação interativa.

## 📝 Tasks

### 🛠️ Criar o endpoint de consulta

#### Descrição

Instale o FastAPI e o servidor Uvicorn. Depois, complete o endpoint `GET /tasks` no arquivo inicial para retornar todas as tarefas armazenadas em memória.

#### Requisitos

O programa concluído deve:

- Iniciar com `uvicorn starter-code:app --reload`
- Criar uma aplicação FastAPI chamada `app`
- Responder a `GET /tasks` com status `200`
- Retornar uma lista de tarefas em formato JSON

### 🛠️ Adicionar tarefas com validação

#### Descrição

Defina um modelo Pydantic para representar uma nova tarefa e implemente `POST /tasks`. O endpoint deve validar os dados recebidos antes de adicionar a tarefa.

#### Requisitos

O programa concluído deve:

- Exigir um campo `title` com pelo menos 3 caracteres
- Aceitar um campo booleano `completed`, cujo valor padrão seja `false`
- Gerar um `id` único para cada nova tarefa
- Responder com status `201` e a tarefa criada
- Retornar um erro de validação quando os dados forem inválidos

Exemplo de requisição:

```json
{
  "title": "Estudar métodos HTTP",
  "completed": false
}
```

### 🛠️ Implementar operações CRUD

#### Descrição

Complete os endpoints para consultar uma tarefa específica, atualizar seu estado e removê-la. Use os códigos de status HTTP adequados para indicar sucesso ou recurso inexistente.

#### Requisitos

O programa concluído deve:

- Responder a `GET /tasks/{task_id}` com uma tarefa específica
- Responder a `PUT /tasks/{task_id}` atualizando título e status
- Responder a `DELETE /tasks/{task_id}` removendo a tarefa
- Retornar status `404` quando o `task_id` não existir
- Retornar a tarefa atualizada após uma operação `PUT`

### 🛠️ Explorar a documentação da API

#### Descrição

Use a documentação automática gerada pelo FastAPI para testar todos os endpoints e melhorar as respostas da API.

#### Requisitos

O programa concluído deve:

- Disponibilizar a interface Swagger em `/docs`
- Adicionar descrições curtas aos endpoints
- Usar modelos de resposta para deixar o formato da API claro
- Testar pelo menos um fluxo completo: criar, consultar, atualizar e excluir uma tarefa
- Registrar no README uma captura ou breve descrição do fluxo testado
