def is_palindrome_iterative(word):
    inverted_word = word[::-1]
    if not word or word == '':
        return False
    if word == inverted_word:
        return True
    if word != inverted_word:
        return False


# Teste do Requisito 6
# print(is_palindrome_iterative('pedra'))
