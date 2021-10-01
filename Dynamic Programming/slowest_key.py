# Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
# Output: "a"
# Explanation: The keypresses were as follows:
# Keypress for 's' had a duration of 12.
# Keypress for 'p' had a duration of 23 - 12 = 11.
# Keypress for 'u' had a duration of 36 - 23 = 13.
# Keypress for 'd' had a duration of 46 - 36 = 10.
# Keypress for 'a' had a duration of 62 - 46 = 16.
# The longest of these was the keypress for 'a' with duration 16.

releaseTimes = [12, 23, 36, 46, 62]
keysPressed = "spuda"


def slowest_key(releaseTimes, keysPressed):
    slowest_key = 'a'
    longest_duration = 0
    n = len(keysPressed)
    for i in range(n):
        pressedTime = releaseTimes[i - 1] if i > 0 else 0
        duration = releaseTimes[i] - pressedTime
        if duration == longest_duration:
            slowest_key = max(slowest_key, keysPressed[i])
        elif duration > longest_duration:
            slowest_key = keysPressed[i]
            longest_duration = duration
        return slowest_key


print("slowest key: ", slowest_key(releaseTimes, keysPressed))
