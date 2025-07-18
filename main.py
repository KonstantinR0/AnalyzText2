def word_count(words):
    return len(words)
    print(f"Количество слов в тексте: {len(words)}")


def long_words(text):
    one_word = ""
    for word in text:
        len(text) > len(one_word)
        one_word = word


def voweles(text):
    vowel = "аеёиоуыэюя"
    count = 0
    for char in text:
        if char in vowel:
            count = +1
    return count


def count_word_frequency(text):
    word_counts = {}
    words = text.lower().split()
    for word in words:
        word = word.strip('.,!?;:()')
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


text = input("Введите текст:").split()
print(f"Количество слов в тексте: {word_count(text)}")
print(f"Саммое длинное слово в тексте: {long_words(text)}")
print(f" Количество глассных: {voweles(text)}")
print(f"частота слов: {count_word_frequency(text)}")

# Подсчитывает количество слов в тексте.