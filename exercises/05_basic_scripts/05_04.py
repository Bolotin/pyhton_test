from sys import argv

num, word = argv[1:]
num = int(num)
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_list.reverse()
word_list.reverse()

print('Num last index: {}'.format(str(len(num_list) - num_list.index(num) - 1)))
print('Word last index: {}'.format(str(len(word_list) - word_list.index(word) - 1)))
