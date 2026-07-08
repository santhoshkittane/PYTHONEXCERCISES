user_input = input('Enter your name: ')
print(f'User entered {user_input}')
s = ''.join(i for i in user_input)
if(s == s[::-1]):
    print(f'{user_input}'+' is a palindrome')
else:
    print(f'{user_input} is not a palindrome')
    '''
    ytest
    ing
    '''

user_input = user_input +'mid'+ user_input
print('Double user Input:', user_input)

s= '*'.join(i for i in user_input)

print(s)
