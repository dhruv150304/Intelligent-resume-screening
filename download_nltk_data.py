import nltk

# Download required NLTK resources
for package in [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
]:
    nltk.download(package)

print("NLTK resources downloaded successfully!")
