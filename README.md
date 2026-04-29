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
Certifique-se de que o ambiente virtual está ativo:
```bash
# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar o Rasa (caso ainda não tenha no ambiente)
pip install rasa