# 📘 Assignment: Consuming APIs with HTMX

## 🎯 Objective

Você aprenderá a criar uma interface web dinâmica usando HTML e HTMX, conectando formulários e botões a uma aplicação FastAPI sem escrever JavaScript para cada interação. Ao final, a página permitirá listar, criar e concluir tarefas.

## 📝 Tasks

### 🛠️ Carregar tarefas com HTMX

#### Descrição

Complete a página `index.html` usando atributos HTMX para carregar a lista de tarefas assim que a página for aberta. Use o servidor FastAPI fornecido para testar o resultado.

Instale as dependências com `pip install fastapi uvicorn python-multipart` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Iniciar com `uvicorn starter-code:app --reload`
- Fazer uma requisição `GET` para `/tasks` quando a página carregar
- Inserir a resposta no elemento com id `task-list`
- Exibir as tarefas retornadas pelo servidor sem recarregar a página

### 🛠️ Criar tarefas pelo formulário

#### Descrição

Configure o formulário para enviar novas tarefas ao servidor usando HTMX. A resposta do servidor deve aparecer na lista imediatamente.

#### Requisitos

O programa concluído deve:

- Enviar o formulário para `POST /tasks`
- Enviar o campo `title` usando o nome esperado pela API
- Inserir a nova tarefa no início da lista
- Limpar o formulário após uma resposta bem-sucedida
- Evitar o recarregamento completo da página

Exemplo de interação:

```text
Digite: Revisar métodos HTTP
Resultado: a nova tarefa aparece na lista sem atualizar o navegador
```

### 🛠️ Atualizar tarefas sem JavaScript

#### Descrição

Adicione um botão em cada tarefa para marcar a atividade como concluída. Use os atributos HTMX para enviar a requisição e substituir apenas o item alterado.

#### Requisitos

O programa concluído deve:

- Enviar `PATCH /tasks/{task_id}/complete` ao clicar no botão
- Atualizar somente o item da tarefa modificada
- Mostrar visualmente quando uma tarefa estiver concluída
- Usar um alvo HTMX específico para cada tarefa
- Exibir uma mensagem de erro amigável quando uma requisição falhar
