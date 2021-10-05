
class hash_list():

	def __init__(self):
		self.hash_list = {}

	def add(self, *args):
		for item in args:
			key = self.__key__(item)
			try:
				self.hash_list[key] += [item]
			except Exception:
				self.hash_list[key] = [item]

	def get_item(self, item=None, index=None):
		if item:
			return self.__get_item_by_name__(item)
		elif index:
			return self.__get_item_by_index__(index)

	def remove_item(self, item=None, index=None):
		if item:
			self.__remove_item_by_name__(item)
		else:
			self.__remove_item_by_index__(index)

	def delete_index(self, index):
		self.hash_list.pop(index)

	def indexes(self):
		ind = [index for index in self.hash_list.keys()]
		return ind

	def __key__(self, word):
		key = sum([ord(letter) for letter in word])//len(word)
		return key

	def __remove_item_by_name__(self, item):
		itm = self.__get_item_by_name__(item)
		self.__remove_item_by_index__(index=itm)

	def __remove_item_by_index__(self, index):
		self.hash_list[index[0]].pop(index[1])
		if len(self.hash_list[index[0]]) == 0:
			self.delete_index(index[0])

	def __get_item_by_index__(self, index):
		return self.hash_list[index[0]][index[1]]
	
	def __get_item_by_name__(self, item):
		key = self.__key__(item)
		items_lst = self.hash_list[key]
		if item in items_lst:
			return (key, items_lst.index(item))
		else:
			raise Exception(f"'{item}'")

	def print(self):
		print(self.hash_list)
