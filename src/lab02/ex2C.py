def format_record(write):
    answer = ''
    if len(write[0]) == 0:
        return "ValueError"
    else:
        newfio = write[0].split()
        answer += newfio[0][0].upper() + newfio[0][1: ] + ' '
        for initial in newfio[1:]:
            answer += initial[0].upper() + '.'
    answer += ', гр. '
    if len(write[1]) == 0:
        return "ValueError"
    else:
        answer += write[1] + ', '
    if 0 <= write[2] <= 5.0:
        answer += f'GPA {format(write[2], '.2f')}'
    else:
        return "ValueError"
    return answer
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))


        