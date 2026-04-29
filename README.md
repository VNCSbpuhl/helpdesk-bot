# Helpdesk Bot - Suporte de TI 💻

Este projeto consiste em um chatbot inteligente desenvolvido com o framework **Rasa**. Ele atua como um assistente de suporte técnico de primeiro nível, capaz de identificar problemas comuns relatados pelos usuários e fornecer orientações técnicas imediatas.

O projeto foi desenvolvido como parte de uma atividade acadêmica para o curso de **Desenvolvimento de Software Multiplataforma (DSM)**.

---

## 👥 Equipe
* **Vinícius Rodrigues Oliveira**
* **Nathan Bizinoto**
* **Bruno Santos**

---

## 🚀 Funcionalidades
O bot utiliza Processamento de Linguagem Natural (PLN) e uma lógica de mapeamento de sinônimos para identificar e resolver queixas como:
* **Lentidão e Travamentos:** Orientações sobre o Gerenciador de Tarefas e limpeza de cache.
* **Problemas de Conexão (Wi-Fi/Internet):** Procedimentos de reinicialização de roteadores e limpeza de DNS.
* **Tela Azul:** Diagnóstico de memória RAM e verificação de drivers.
* **Vírus e Malware:** Procedimentos de isolamento e varredura de segurança.
* **Impressora:** Resolução de erros na fila de impressão e reinicialização física.

---

## 🛠️ Tecnologias Utilizadas
* [Rasa Open Source](https://rasa.com/) - Framework de IA para conversas.
* [Python](https://www.python.org/) - Linguagem para o servidor de ações customizadas (Action Server).
* [HTML5/CSS3/JavaScript] - Interface de chat customizada com tema Dark/Tech.

---

## 🏃 Como Executar o Projeto

### 1. Preparar o Ambiente

Clone o repositório e crie o ambiente virtual:

```bash
git clone https://github.com/VNCSbpuhl/helpdesk-bot.git
cd helpdesk-bot
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Instale o Rasa:

```bash
pip install rasa
```

### 2. Treinar o Modelo

```bash
rasa train
```

### 3. Rodar o Bot

Abra **dois terminais** na pasta do projeto com o ambiente virtual ativo.

**Terminal 1 — Servidor principal do Rasa:**
```bash
rasa run --enable-api --cors "*"
```

**Terminal 2 — Servidor de ações customizadas:**
```bash
rasa run actions
```

### 4. Abrir a Interface

Com os dois servidores rodando, abra o arquivo `chat.html` no navegador.

```bash
# macOS
open chat.html

# Linux
xdg-open chat.html
```

---

## 💬 Exemplos de uso

| Mensagem do usuário | Problema identificado |
|---|---|
| "meu pc está travando" | Lentidão |
| "sem internet" | Conexão |
| "deu tela azul" | Tela Azul (BSOD) |
| "acho que peguei um vírus" | Vírus/Malware |
| "a impressora não imprime" | Impressora |
