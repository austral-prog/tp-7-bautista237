def enumerate_list(lst):
    return [f"{i}. {word}" for i, word in enumerate(lst) if word != ""]

def enumerate_backwards(lst):
    return [f"{i}. {word[::-1]}" for i, word in enumerate(lst) if word != ""]

colors = ["Red", "Green", "", "White", "Black"]

print(enumerate_list(colors))
print(enumerate_backwards(colors))
