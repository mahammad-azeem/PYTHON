class Palindrome:
    def __init__(self, value):
        self.value = value
    
    def reverse_check(self):
        word = self.value
        if word == word[::-1]:
            print(word+' is a Palindrome !!!')
        else:
            print(word+' is a Not Palindrome')
test_case = Palindrome('gadag')
test_case.reverse_check()