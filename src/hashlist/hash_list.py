
class hash_list():

    def __init__(self):
        self.hash_list = {}

    def add(self, *args):
        if args:
            for item in args:
                key = self._key_(item)
                if self.hash_list.get(key):
                    self.hash_list[key].append(item)
                else:
                    self.hash_list[key] = [item]
        else:
            raise Exception('No arguments passed.')

    def get_item_index(self, item):
        key = self._key_(item)
        if self.hash_list.get(key):
            items_lst = self.hash_list[key]
            if item in items_lst:
                return (key, items_lst.index(item))
            else:
                raise Exception(f"'{item}' may have the same key but is not in hashlist")
        else:
            raise Exception(f"'{item}' not found")

    def get_item_by_index(self, index):
        try:
            return self.hash_list[index[0]][index[1]]
        except Exception:
            raise Exception('Index out of bound')

    def remove_item_by_index(self, index):
        try:
            self.hash_list[index[0]].pop(index[1])
            if len(self.hash_list[index[0]]) == 0:
                self.delete_index(index[0])
        except Exception:
            raise Exception('Index out of  bound.')

    def remove_item_by_name(self, item):
        index = self.get_item_index(item)
        self.remove_item_by_index(index)

    def delete_index(self, index):
        self.hash_list.pop(index)

    def indexes(self):
        ind = [index for index in self.hash_list.keys()]
        return ind

    def _key_(self, word):
        if word:
            key = sum([ord(letter) for letter in word])//len(word)
            return key
        raise Exception('Argument can not be None')

    def print(self):
        print(self.hash_list)
