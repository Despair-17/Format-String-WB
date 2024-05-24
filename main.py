from process_file.process_file import ProcessFile
from core.format_string import FormatString


def main():
    path_in = 'data/data_in.txt'
    path_out = 'data/data_out.txt'
    data_in = ProcessFile.read_file(path_in)

    otp_flag = input('Столбец с OTP есть (y/n)?: ')
    if otp_flag == 'y':
        format_string = FormatString().format_with_opt
        extra_content = [input('Введите клиент id: ')]

    else:
        format_string = FormatString().format_without_otp
        otp = input('Введите кастомный OPT: ')
        client_id = input('Введите клиент id: ')
        extra_content = [otp, client_id]

    data_out = []
    count = 0
    for row in data_in:
        clean_row = format_string(row)
        new_data = [clean_row] + extra_content
        new_string = f"{','.join(new_data)}\n"
        data_out.append(new_string)
        count += 1

    ProcessFile.write_file(path_out, data_out)
    print(f'Отформатировано {count} строки.')


if __name__ == '__main__':
    main()
