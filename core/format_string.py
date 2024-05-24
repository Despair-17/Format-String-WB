import re


class FormatString:
    REGEX = re.compile(r'[^0-9]')

    def format_without_otp(self, string: str) -> str:
        new_string = self.REGEX.sub('', string)
        return new_string

    def format_with_opt(self, string: str) -> str:
        new_string = self.REGEX.sub('', string)
        number, otp = new_string[:-6], new_string[-6:]
        return ','.join([number, otp])
