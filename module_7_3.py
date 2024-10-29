class WordsFinder:
    file_names = []
    words_list = []
    new_dict = {}

    def __init__(self, *args):
        self.args = args
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        for i in self.file_names:
            with open(i) as file:
                for i in file:
                    self.words_list.append(i.lower().split())
        self.new_dict = dict(zip(self.file_names, self.words_list))
        return self.new_dict

    def find(self, word):
        dict_lict = {}
        pos_list = []
        not_in = True
        for i in self.words_list:
            a = 0
            for item in i:
                a += 1
                if word in item:
                    pos_list.append(a)
                    not_in = False
                    break
                else:
                    continue

            if not_in:
                pos_list.append(0)

        dict_lict = dict(zip(self.file_names, pos_list))
        return dict_lict

    def count(self, word):
        list = []
        dict_list = {}
        for i in self.words_list:
            a = 0
            for item in i:
                if word in item:
                    a += 1
                else:
                    continue
            list.append(a)
        dict_list = dict(zip(self.file_names, list))
        return dict_list

w1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
#print(w1.file_names)
print(w1.get_all_words())
print(w1.words_list)
print(w1.find('text'))
print(w1.count('text'))
