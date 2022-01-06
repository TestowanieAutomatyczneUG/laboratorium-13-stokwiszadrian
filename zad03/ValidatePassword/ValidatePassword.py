import re


class ValidatePassword:
    def validate(self, p):
        if not isinstance(p, str):
            raise TypeError("Password must be a string")
        valid = False
        if len(p) > 7:
            chars = re.compile("[$&+,:;=?@#|'<>.^*()%!-]")
            upper = re.compile("[A-Z]")
            num = re.compile("[0-9]")
            if re.search(chars, p) and re.search(upper, p) and re.search(num, p):
                valid = True
        return valid


if __name__ == "__main__":
    test = ValidatePassword()
    print(test.validate("aaaaa11@@"))