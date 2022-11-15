MIN_LENGTH = 6


def main():
    users_password = get_name()
    display_stars(users_password)


def display_stars(users_password):
    print('*' * len(users_password))


def get_name():
    users_password = input("Enter password: ")
    while len(users_password) < MIN_LENGTH:
        print(f"Invalid. Please enter at least {MIN_LENGTH} character")
        users_password = input("Enter password: ")
    return users_password


main()


