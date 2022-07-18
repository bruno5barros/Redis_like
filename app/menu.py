from redis.redis_dict import RedisDict

choice = 0
redis_dict = RedisDict()


def input_transaction(message):
    try:
        return input(message)
    except ValueError:
        print("Please, insert a valid input.")


while choice != 5:
    print(f"    **************************************\n\
    *                                    *\n\
    *        1 - GET content             *\n\
    *        2 - SET content             *\n\
    *        3 - UNSET content           *\n\
    *        4 - NUMEQUALTO              *\n\
    *        5 - END                     *\n\
    *        6 - BEGIN transactions      *\n\
    *        7 - COMMIT transactions     *\n\
    *        8 - ROLLBACK transactions   *\n\
    *                                    *\n\
    **************************************")
    try:
        choice = int(input("Please, select the desired command:"))
    except ValueError:
        choice = 0
        print("Please, insert a valid number.")

    if choice == 1:
        redis_dict.get_all_content()
        key = input_transaction(
            "Select the key of the content you want to be returned:")
        item_value = redis_dict.get_content(key)
        print(item_value) if item_value else print("NULL")
    elif choice == 2:
        key = input_transaction("Insert the key of content:")
        value = input_transaction("Insert the value of content:")
        item_value = redis_dict.set_content(key, value)
        print("\n")
    elif choice == 3:
        redis_dict.get_all_content()
        key = input_transaction(
            "Select the key of the content you want to be returned:")
        item_value = redis_dict.unset_content(key)
        print("\n")
    elif choice == 4:
        redis_dict.get_all_content()
        value = input_transaction("Insert the value of content:")
        list_idexes = redis_dict.find_content(value)
        print("List of indexes:", list_idexes)
    elif choice == 6:
        redis_dict.begin_transactions()
        print("\n")
    elif choice == 7:
        res = redis_dict.commit_transations()
        print(res) if res == "NO TRANSACTION" else print("\n")
    elif choice == 8:
        res = redis_dict.rollback_transations()
        print(res) if res == "NO TRANSACTION" else print("\n")
    else:
        if choice != 5:
            print("error")
