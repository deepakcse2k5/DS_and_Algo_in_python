num = "alex"

def isLongPressedName(name: str, typed: str) -> bool:
        # edge case
        i = 0
        j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)

print(isLongPressedName("alex","aaleex"))