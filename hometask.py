import requests
from collections import defaultdict
import matplotlib.pyplot as plt

def map_function(text):
    words = text.split()
    return [(word, 1) for word in words]

def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(shuffled_values):
    reduced = {}
    for key, values in shuffled_values:
        reduced[key] = sum(values)
    return reduced

def map_reduce(text):
    # Крок 1: Мапінг
    mapped_values = map_function(text)

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Крок 3: Редукція
    reduced_values = reduce_function(shuffled_values)

    return reduced_values

def visualize_top_words(word_counts, top_n=10):
    # Сортування слів за частотою
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_word_counts[:top_n]

    words = [word for word, count in top_words]
    counts = [count for word, count in top_words]

    # Створення горизонтальної гістограми
    plt.figure(figsize=(10, 6))
    plt.barh(words, counts, color='skyblue')
    plt.xlabel('Кількість')
    plt.ylabel('Слова')
    plt.title('Топ слів')
    plt.gca().invert_yaxis()  # Інвертувати вісь Y для відображення найбільш частих слів нагорі
    plt.show()

if __name__ == "__main__":
    # Отримання тексту за URL
    url = "https://www.gutenberg.org/files/11/11-0.txt?form=MG0AV3"
    response = requests.get(url)
    text = response.text

    # Застосування MapReduce
    word_counts = map_reduce(text)

    # Візуалізація результатів
    visualize_top_words(word_counts)