class FruitBasket:
    def __init__(self, fruits):
        self.fruits = fruits
        self.start = 0
        self.max_length = 0
        self.fruit_freq = {}

    def max_fruits_in_baskets(self):
        for end in range(len(self.fruits)):
            right_fruit = self.fruits[end]
            if right_fruit not in self.fruit_freq:
                self.fruit_freq[right_fruit] = 0
            self.fruit_freq[right_fruit] += 1

            # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
            while len(self.fruit_freq) > 2:
                left_fruit = self.fruits[self.start]
                self.fruit_freq[left_fruit] -= 1
                if self.fruit_freq[left_fruit] == 0:
                    del self.fruit_freq[left_fruit]
                self.start += 1

            self.max_length = max(self.max_length, end - self.start + 1)

        return self.max_length


if __name__ == '__main__':
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']
    fruit_basket = FruitBasket(fruits)
    result = fruit_basket.max_fruits_in_baskets()
    print(result)
