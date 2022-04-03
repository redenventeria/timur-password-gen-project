import random

def load_database(path):
    file = open("./database.db", "r")
    words = file.read().split("\n")
    words = [word.rstrip(" ") for word in words]
    return words

def generate_memorable_password(
    dictonary,
    word_count=3,
    has_special_characters=True,
    special_characters=None,
    sep="_"):

    words_for_password = get_words(dictonary, word_count)
    password = add_sep(words_for_password, sep)

    password = add_digits(password, sep)

    if has_special_characters:
        if special_characters == None:
            special_characters = define_special_characters() # Доопределяем специальные симвлоы
            password = add_special(password, special_characters)
        else:
            password = add_special(password, special_characters)
    
    return password

def define_special_characters():
    return "#$&%@!?"

def get_words(dictonary, word_count):
    words_for_password = random.sample(dictonary, k=word_count)
    return words_for_password

def add_digits(password, sep):

    position_options = {("begin"), ("end")}

    password_words = password.split(sep)

    for word_number in range(len(password_words)):
        position_options.add( ("part_of_word", word_number, "begin") )
        position_options.add( ("part_of_word", word_number, "end") )

    amount = random.randint(1, 3)

    for i in range(amount):
        length = random.randint(1, 3)
        insert_type = random.choice(list(position_options))
        number = random.randint(10**(length - 1), 10**length - 1)

        if insert_type[0] == "begin":
            password = str(number) + password
            position_options.discard("begin")
        
        if insert_type[0] == "end":
            password = password + str(number) 
            position_options.discard("end")
        
        if insert_type[0] == "part_of_word":
            password_words = password.split(sep)
            if insert_type[2] == "begin":
                password_words[insert_type[1]] += str(number)
            else:
                password_words[insert_type[1]] = str(number) + password_words[insert_type[1]]

            password = sep.join(password_words)
            position_options.discard(insert_type)

    return password


def add_sep(words, sep):
    return sep.join(words)

def add_special(password, special_characters):
    return special_characters[:len(special_characters) // 2] + password + special_characters

dictonary = load_database("./database.db")
password = generate_memorable_password(dictonary)
print(password)
