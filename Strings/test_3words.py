def checkio(game_result: list[str]) -> str:
    for string in game_result:
        if string[0] == 'X':
            print('X')
    # return ""


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
