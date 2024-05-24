class ProcessFile:

    @staticmethod
    def read_file(path: str, encoding='utf-8') -> list[str]:
        with open(path, mode='r', encoding=encoding) as rfile:
            rows = rfile.readlines()

        return rows

    @staticmethod
    def write_file(path: str, data: list[str], encoding='utf-8') -> None:
        with open(path, mode='w', encoding=encoding) as wfile:
            wfile.writelines(data)
