def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(char.isdigit() for char in password)
    cond3 = any(char.isalpha() for char in password)
    if len(password) > 9:
        cond2 = cond3 = True # cond4
    cond5 = 'password' not in password and 'PASSWORD' not in password
    cond6 = len(set(password)) > 2

    return all([cond1, cond2, cond3, cond5, cond6])
    #
    # if cond1:
    #     if all([cond4, cond6]):
    #         return cond5
    #     else:
    #         return all([cond2, cond3])
    # else:
    #     return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("12345678910"))
    # These "asserts" are used for self-checking
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("notshort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    print("The mission is done! Click 'Check Solution' to earn rewards!")

print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
