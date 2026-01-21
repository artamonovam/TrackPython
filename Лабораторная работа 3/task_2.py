# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(part1, part2, spl = ","):
    res1 = set(part1.split(spl))
    res2 = set(part2.split(spl))
    sort = list(res1.intersection(res2))
    return sort

print(find_common_participants(participants_first_group, participants_second_group, "|"))

