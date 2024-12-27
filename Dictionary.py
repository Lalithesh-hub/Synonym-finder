import streamlit as st
import nltk
from nltk.corpus import wordnet

# Function to get synonyms using WordNet from nltk
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Streamlit UI
def main():
    st.title("Word Synonym Finder")

    # User input for word
    word = st.text_input("Enter a word to find its synonyms:")

    if word:
        # Get synonyms for the provided word
        synonyms = get_synonyms(word)
        
        if synonyms:
            # Display the synonyms
            st.write(f"Synonyms for '{word}':")
            st.write(synonyms)
        else:
            st.write(f"No synonyms found for '{word}'. Try another word.")

if __name__ == "__main__":
    main()
