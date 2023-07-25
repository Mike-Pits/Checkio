def checkio(game_result: list[str]) -> str:

    for i in range(len(game_result)):
        if game_result[i][0] == game_result[i][1] and game_result[i][0] == game_result[i][2]:
            if game_result[0].isalpha():
                return game_result[i][0]

    for i in range(len(game_result)):
        if game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            if game_result[0][i].isalpha():
                return game_result[0][i]

    if game_result[0][0] == game_result[1][1] and game_result[0][0] == game_result[2][2]:
        if game_result[i][0].isalpha():
            return game_result[i][0]

    elif game_result[0][2] == game_result[1][1] and game_result[0][2] == game_result[2][0]:
        if game_result[i][0].isalpha():
            return game_result[i][0]

    else:
        return 'D'


print("Example:")
print(checkio(["X.O", "XX.", "XOO"]))

# These "asserts" are used for self-checking
assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

print("The mission is done! Click 'Check Solution' to earn rewards!")
