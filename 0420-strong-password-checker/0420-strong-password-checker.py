class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = 3 - (has_lower + has_upper + has_digit)

        change = 0
        one_mod = two_mod = 0  # סופרי רצפים לפי אורך % 3
        i = 2

        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1

                change += length // 3
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)

        elif n <= 20:
            return max(missing_types, change)

        else:
            to_delete = n - 20
            del_use = min(to_delete, one_mod * 1)
            change -= del_use // 1
            to_delete -= del_use

            del_use = min(to_delete, two_mod * 2)
            change -= del_use // 2
            to_delete -= del_use

            change -= to_delete // 3

            return (n - 20) + max(missing_types, change)
