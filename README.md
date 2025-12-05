# ⚙️ Blackline Tools | Text Summarizer (Mini-AI)

**[BLACKLINE CODE]** Engenharia de Precisão | Clean • Precise • Minimal

Este projeto demonstra a capacidade da Blackline Code em desenvolver **soluções de automação** focadas em Processamento de Linguagem Natural (PLN). O **Text Summarizer** é um utilitário de linha de comando (CLI) que aplica o algoritmo de frequência para extrair e apresentar o núcleo da informação de textos longos.

Ideal para sumários executivos, processamento de atas de reunião ou análise rápida de grandes volumes de texto.

---

## 💡 Princípios de Engenharia (Valor Agregado)

O script segue o padrão de excelência profissional:

* **Design Minimalista (CLI):** Uso de interface de linha de comando para máxima performance e mínima sobrecarga de recursos.
* **Performance:** Código otimizado em Python, livre de dependências pesadas, garantindo velocidade de execução.
* **Inteligência (PLN):** Seleção de frases baseada em relevância estatística, garantindo a coerência e precisão do resumo.
* **Interface Profissional (`argparse`):** Utiliza argumentos nomeados (`--text`, `--sentences`), facilitando a integração em fluxos de trabalho e servidores.

---

## 🚀 Guia de Execução (Desenvolvimento)

Para rodar esta ferramenta, siga os passos no seu ambiente Linux/Terminal:

### 1. Configuração do Ambiente

1.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Instale a Dependência:**
    ```bash
    pip install nltk
    ```
3.  **Download de Recursos NLTK (Obrigatório):**
    É necessário baixar os dados de linguagem para o algoritmo de PLN funcionar corretamente.
    ```bash
    python3
    >>> import nltk
    >>> nltk.download('all') 
    >>> exit()
    ```

### 2. Uso da Ferramenta

Execute o script com os argumentos nomeados (`--text` é obrigatório, `--sentences` é opcional). **Sempre utilize aspas duplas no texto de entrada.**

**Comando Padrão (Resumo de 2 Frases):**

```bash
python3 summarizer.py --text "Seu relatório longo e complexo vai aqui, envolto em aspas para garantir que o terminal leia tudo corretamente."
git 