# Crie uma função que retorne todas as permutações de uma string.
import itertools

palavra = input('Qual palavra deseja fazer a permutação? ')


def permutacao(palavra):
    nums = list(palavra)
    permutations = list(itertools.permutations(nums))

    return [''.join(permutation) for permutation in permutations]


print(permutacao(palavra))
