words = [
    "something",
    "Perceptrone",
    "малина",
    "Світланочка",
    "актова зала",
    "біоресурси",
    "єдиний",
    "Їжак",
    "Іван",
    "кава"
]

def sorting(word):
    first_letter = word[0].lower()
    ukrainian = "абвгґдеєжзийіїклмнопрстуфхцчшщьюя"
    if first_letter in ukrainian:
        return(0, word.lower())
    else:
        return(1, word.lower())
    
print("Список: ")
print(words)

sorted_words = sorted(words, key=sorting)

print("\nВідсортований список: ")
print(sorted_words)