import re
import string
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class WordFrequencyAnalyzer:
    def __init__(self):
        self.stop_words = set([
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'were', 'will', 'with'
        ])
        self.word_counts = Counter()

    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    def clean_text(self, text):
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        return text

    def tokenize(self, text):
        return text.split()

    def remove_stop_words(self, words):
        return [word for word in words if word not in self.stop_words]

    def analyze(self, text):
        cleaned_text = self.clean_text(text)
        words = self.tokenize(cleaned_text)
        words = self.remove_stop_words(words)
        self.word_counts.update(words)

    def get_top_words(self, n=10):
        return self.word_counts.most_common(n)

    def print_top_words(self, n=10):
        for word, count in self.get_top_words(n):
            print(f"{word}: {count}")

    def plot_top_words(self, n=10):
        words, counts = zip(*self.get_top_words(n))
        plt.figure(figsize=(12, 6))
        plt.bar(words, counts)
        plt.title(f"Top {n} Words")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_word_cloud(self):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(self.word_counts)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Word Cloud")
        plt.show()

def main():
    analyzer = WordFrequencyAnalyzer()

    while True:
        print("\nWord Frequency Analyzer")
        print("1. Analyze text from file")
        print("2. Analyze text from input")
        print("3. Print top words")
        print("4. Plot top words")
        print("5. Generate word cloud")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the filename: ")
            try:
                text = analyzer.read_file(filename)
                analyzer.analyze(text)
                print("File analyzed successfully!")
            except FileNotFoundError:
                print("File not found. Please check the filename and try again.")

        elif choice == '2':
            text = input("Enter the text to analyze: ")
            analyzer.analyze(text)
            print("Text analyzed successfully!")

        elif choice == '3':
            n = int(input("How many top words to display? "))
            analyzer.print_top_words(n)

        elif choice == '4':
            n = int(input("How many top words to plot? "))
            analyzer.plot_top_words(n)

        elif choice == '5':
            analyzer.generate_word_cloud()

        elif choice == '6':
            print("Thank you for using Word Frequency Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
