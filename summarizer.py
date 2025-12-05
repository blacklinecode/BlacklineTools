# summarizer.py - Ferramenta de Resumo Blackline Code (PLN)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# A principal função: a "Inteligência" do script
def summarize_text(text, num_sentences=3):
    """
    Gera um resumo conciso e preciso de um texto (algoritmo de frequencia).
    """
    if not text:
        return "Texto de entrada vazio."

    # 1. Separa o texto em frases
    sentences = sent_tokenize(text)
    
    if len(sentences) <= num_sentences:
        return text

    # 2. Conta a frequência das palavras importantes
    word_freq = {}
    
    # Tentativa de carregar stopwords em português
    try:
        # Usa o set de stopwords (palavras comuns que não contam)
        stop_words = set(stopwords.words('portuguese'))
    except LookupError:
        # Se as stopwords não estiverem baixadas, usa um set vazio
        stop_words = set()
    
    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            # Conta a frequência da palavra
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # 3. Pontuação das Frases: A frase ganha pontos se contiver palavras frequentes.
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence.lower():
                # Adiciona a frequência da palavra na pontuação total da frase
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

    # 4. Seleciona as N frases com maior pontuação
    # O "sorted" é o que garante que as frases mais importantes venham primeiro.
    summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    
    # Junta as frases selecionadas no resumo final
    return ' '.join([sentence for sentence, score in summary_sentences]).strip()

# --- Bloco de Teste para o Desenvolvedor ---

if __name__ == "__main__":
    
    # Texto de exemplo (com cara de projeto ou reunião)
    input_text = """
    A reunião de hoje focou na melhoria da performance da API. 
    A equipe de desenvolvimento propôs uma migração do banco de dados 
    para um serviço mais rápido. Essa mudança, apesar de custosa no curto prazo, 
    garantirá uma latência de menos de 100ms nas principais requisições, 
    cumprindo a meta de otimização de performance do Q4. 
    Será necessário automatizar o processo de migração para evitar erros manuais.
    """
    
    # Gera um resumo de 2 frases
    resumo = summarize_text(input_text, num_sentences=2)
    
    print("====================================")
    print("RESUMO BLACKLINE CODE (2 Frases):")
    print(resumo)
    print("====================================")