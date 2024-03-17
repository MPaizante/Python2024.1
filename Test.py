class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs


# Create an instance of Animal with 4 arms and 4 legs
spider = Animal(4, 4)

# Call the limbs method on the spider instance
spidlimbs = spider.limbs()

print("Spider has {} limbs.".format(spidlimbs))
