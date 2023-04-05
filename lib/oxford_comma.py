def oxford_comma(items):
    if (len(items) >= 3):
        first_items = [", ".join(items[0:-1])]
        last_item = [items[-1]]
        print(", and ".join(first_items + last_item))
        # print(", and ".join([", ".join(items[0:-1])] + [", and".join(items[-1])]))
        return ", and ".join(first_items + last_item)
    elif (len(items) == 2):
        print(" and ".join(items))
        return " and ".join(items)
    else:
        print("".join(items))
        return "".join(items)

# def oxford_comma(items):
#     if len(items) > 1:
#         items[-1] = "and " + items[-1]

#     if len(items) > 2:
#         return ', '.join(items)
#     else:
#         return ' '.join(items)
    

oxford_comma(["a", "b", "c"])
