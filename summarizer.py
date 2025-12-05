# summarizer.py - Ferramenta de Resumo Blackline Code (PLN)

import sys 
import argparse # Módulo profissional para interfaces de linha de comando
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
        stop_words = set(stopwords.words('portuguese'))
    except LookupError:
        stop_words = set()
    
    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # 3. Pontuação das Frases: A frase ganha pontos se contiver palavras frequentes.
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in word_freq.items():
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

    # 4. Seleciona as N frases com maior pontuação
    summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    
    # Junta as frases selecionadas no resumo final
    return ' '.join([sentence for sentence, score in summary_sentences]).strip()

# --- Bloco de Execução Profissional com Argumentos Nomeados (argparse) ---

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description='Text Summarizer Tool (Blackline Code) - Generates a precise summary of input text.',
        epilog='Use aspas para envolver o texto de entrada.'
    )
    
    # Argumento OBRIGATÓRIO: O texto a ser resumido
    parser.add_argument(
        '--text', 
        type=str, 
        required=True, 
        help='The text input to be summarized (enclose in quotes).'
    )
    
    # Argumento OPCIONAL: O número de frases
    parser.add_argument(
        '--sentences', 
        type=int, 
        default=2, 
        help='The desired number of sentences for the summary (default is 2).'
    )
    
    args = parser.parse_args()
    
    # Gera o resumo
    resumo = summarize_text(args.text, num_sentences=args.sentences)
    
    print("====================================")
    print(f"RESUMO BLACKLINE CODE ({args.sentences} Frases):")
    print(resumo)
    print("====================================")