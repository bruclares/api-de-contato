# 📧 API de Contato (Microsserviço)

API robusta e escalável desenvolvida em **FastAPI** para gerenciar o envio de formulários de contato.
Projetada com foco em **Segurança, Observabilidade e Performance**, pronta para atender múltiplos clientes através de uma arquitetura limpa e desacoplada.

---

## 🚀 Tecnologias e Bibliotecas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework moderno e assíncrono de alta performance.
- **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para produção.
- **[Pydantic V2](https://docs.pydantic.dev/)**: Validação de dados rigorosa e serialização.
- **[FastAPI-Mail](https://sabuhish.github.io/fastapi-mail/)**: Envio assíncrono de e-mails (Background Tasks).
- **[SlowAPI](https://pypi.org/project/slowapi/)**: Rate Limiting para proteção contra Spam/DoS.
- **[Loguru](https://github.com/Delgan/loguru)**: Logging estruturado e rotação de arquivos de log.

---

## ✨ Funcionalidades Principais

- **🛡️ Segurança Avançada**:

  - **CORS Dinâmico**: Configuração via variáveis de ambiente para restringir origens permitidas.
  - **Rate Limiting**: Proteção contra abuso (ex: 5 requisições/minuto por IP).
  - **Sanitização**: Limpeza automática de inputs (trim) antes do processamento.

- **👁️ Observabilidade Completa**:

  - **Logs Estruturados**: Registros detalhados de sucesso, erro e alertas no console e em arquivo.
  - **Monitoramento de Requisições**: Middleware que registra rota, status HTTP e tempo de latência (ms).
  - **Tratamento de Erros**: Captura global de exceções e falhas de validação (422) com logs detalhados.

- **⚡ Performance**:
  - **Envio Assíncrono**: O e-mail é processado em _background_, não travando a resposta para o usuário.

---

## 📂 Estrutura do Projeto

O projeto segue uma estrutura modular simples e eficiente:

```text
📂 backend-api-fastapi
    ├── .env
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── 📁 app/
    │   ├── config.py
    │   ├── logger.py
    │   ├── main.py
    │   ├── routers.py
    │   ├── schemas.py
    │   └── services.py
    └── 📁 logs/
```

## 🛠️ Instalação e Configuração

1. Pré-requisitos
   Python 3.10+

Conta de E-mail com acesso SMTP (ex: Gmail App Password)

2. Configuração Local

```text
# Clone o repositório
git clone [https://github.com/seu-usuario/api-de-contato.git](https://github.com/seu-usuario/api-de-contato.git)
cd api-de-contato

# Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

## Variáveis de Ambiente (.env)

Crie um arquivo .env na raiz e configure:

```text
MAIL_USERNAME=seu@email.com
MAIL_PASSWORD=sua_senha_de_app
MAIL_FROM=seu@email.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_TO=destinatario@email.com
# Lista de sites permitidos (separados por vírgula, sem espaços)
ALLOWED_ORIGINS=http://localhost:5500,[https://seu-site.vercel.app](https://seu-site.vercel.app)
```

## Executando

```text
uvicorn app.main:app --reload
```

## ☁️ Deploy (Render.com)

Esta API está pronta para deploy como Web Service no Render.

1. Conecte o repositório no Render.

2. Defina o Build Command: pip install -r requirements.txt

3. Defina o Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000

4. Adicione as variáveis de ambiente na aba "Environment".

### Desenvolvido por Bruna Clares
