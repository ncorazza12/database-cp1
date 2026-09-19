# Database-CP1 — API REST de Gerenciamento de Alunos

**Aluno:** Nickolas Corazza Alves
**RM:** 562265
**Disciplina/Atividade:** Database-CP1

## Sobre o projeto

API REST desenvolvida com **FastAPI** e **MongoDB**, permitindo o cadastro, consulta, atualização e exclusão de alunos. As operações foram validadas utilizando o **Postman**, seguindo os requisitos da atividade prática.

**Stack utilizada:**
- Python 3
- FastAPI
- Uvicorn
- PyMongo
- MongoDB (local)
- Postman (testes)

## Estrutura do projeto

```
api_alunos/
├── main.py            # Endpoints da API (CRUD de alunos)
├── models.py           # Modelos Pydantic e validações
├── database.py          # Conexão com o MongoDB
├── requirements.txt        # Dependências do projeto
└── images/             # Evidências (prints) de execução e testes
```

## Como executar

```bash
# Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt

# Iniciar o MongoDB local (caso ainda não esteja rodando)
net start mongodb

# Iniciar a API
uvicorn main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000` e a documentação interativa em `http://127.0.0.1:8000/docs`.

## Evidências de execução

### 1. Instalação das dependências do projeto

Execução do gerenciador de pacotes do Python via terminal, download e instalação de todas as bibliotecas necessárias para o funcionamento do projeto.

![Instalação das dependências do projeto](./images/1.%20Instala%C3%A7%C3%A3o%20das%20depend%C3%AAncias%20do%20projeto..jpeg)

### 2. Execução do FastAPI com Uvicorn

Inicialização da aplicação via terminal, ativa o servidor de desenvolvimento na porta padrão 8000 com `--reload` habilitado, garantindo o recarregamento automático da aplicação a cada alteração no código-fonte.

![Execução do FastAPI com Uvicorn](./images/2.%20Execu%C3%A7%C3%A3o%20do%20FastAPI%20com%20Uvicorn..jpeg)

### 3. Documentação interativa UI

Acesso à UI de documentação interativa da API navegando pela URL `127.0.0.1:8000/docs`. A página lista de forma estruturada todos os endpoints disponíveis na aplicação (métodos POST, GET, PUT e DELETE), permitindo o teste das requisições e a visualização dos esquemas de dados diretamente pelo navegador.

![Documentação interativa UI](./images/3.%20Documenta%C3%A7%C3%A3o%20interativa%20UI..jpeg)

### 4. Cadastro de aluno com sucesso

Execução do cadastro de um novo aluno enviando os atributos obrigatórios (nome, email, idade e curso) no corpo da requisição em formato JSON. A API processa a solicitação, persiste o documento no banco de dados MongoDB e retorna o status HTTP 201 Created, exibindo o objeto cadastrado acompanhado do campo `id` gerado dinamicamente.

![Cadastro de Aluno 1 com Sucesso](./images/4.%20Cadastro%20de%20Aluno1%20com%20Sucesso..jpeg)
![Cadastro de Aluno 2 com Sucesso](./images/4.%20Cadastro%20de%20Aluno2%20com%20Sucesso..jpeg)

### 5. Validação de dados e tratamento de erros

Demonstração do mecanismo de validação de dados da API via Pydantic. Ao enviar uma requisição contendo dados inválidos (como nome e curso vazios, formato de e-mail incorreto e idade inferior a 16 anos), a aplicação intercepta a chamada e recusa o cadastro, retornando o status HTTP 422 Unprocessable Entity juntamente com a estrutura JSON detalhando os erros encontrados em cada campo.

![Validação de Dados e Tratamento de Erros](./images/5.%20Valida%C3%A7%C3%A3o%20de%20Dados%20e%20Tratamento%20de%20Erros..jpeg)

### 6. Listagem de todos os alunos

Consulta de todos os registros armazenados na coleção `alunos` do MongoDB. A requisição retorna o status HTTP 200 OK contendo um array JSON com a lista completa de todos os alunos previamente cadastrados.

![Listagem de Todos os Alunos](./images/6.%20Listagem%20de%20Todos%20os%20Alunos..jpeg)

### 7. Consulta de aluno específico por ID

Busca pontual de um único aluno passando o seu identificador único do MongoDB (ObjectId) diretamente no caminho da URL. A API localiza o registro correspondente no banco de dados e retorna o status HTTP 200 OK com os dados exclusivos do aluno solicitado.

![Consulta de Aluno Específico por ID](./images/7.%20Consulta%20de%20Aluno%20Espec%C3%ADfico%20por%20ID..jpeg)

### 8. Tratamento para aluno não encontrado

Validação do comportamento da API ao buscar por um identificador que não existe na base de dados. Ao informar um id inexistente na URL, a aplicação trata a exceção adequadamente e responde com o status HTTP 404 Not Found, confirmando que o registro não foi localizado.

![Tratamento para Aluno Não Encontrado](./images/8.%20Tratamento%20para%20Aluno%20N%C3%A3o%20Encontrado..jpeg)

### 9. Atualização de dados do aluno

Atualização dos dados de um aluno existente no banco de dados. Enviando o identificador na URL e a nova estrutura de dados no corpo da requisição em JSON, a API efetua a alteração no MongoDB e retorna o status HTTP 200 OK exibindo as informações atualizadas.

![Atualização de Dados do Aluno](./images/9.%20Atualiza%C3%A7%C3%A3o%20de%20Dados%20do%20Aluno..jpeg)

### 10. Exclusão de aluno

Remoção permanente de um registro da coleção de alunos do MongoDB informando o seu id na URL. A API executa a exclusão no banco de dados e responde com o status HTTP 200 OK (ou 204 No Content), confirmando a remoção do registro.

![Exclusão de Aluno](./images/10.%20Exclus%C3%A3o%20de%20Aluno..jpeg)

## Endpoints da API

| Método | Rota            | Descrição                       |
|--------|-----------------|----------------------------------|
| POST   | `/alunos`       | Cadastra um novo aluno           |
| GET    | `/alunos`       | Lista todos os alunos            |
| GET    | `/alunos/{id}`  | Consulta um aluno específico     |
| PUT    | `/alunos/{id}`  | Atualiza os dados de um aluno    |
| DELETE | `/alunos/{id}`  | Remove um aluno                  |

## Regras de validação

- `nome` não pode ser vazio;
- `email` deve possuir formato válido;
- `idade` deve ser maior ou igual a 16;
- `curso` não pode ser vazio;
- Não é permitido cadastrar dois alunos com o mesmo e-mail (índice único no MongoDB).

## Banco de dados

```
MongoDB
└── banco: escola
    └── coleção: alunos
```

## Repositório

https://github.com/ncorazza12/database-cp1.git
