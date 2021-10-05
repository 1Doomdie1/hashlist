## Description

This package is meant to store data in a smart way so when you are dealing with large amounts of data it will be faster to query the list and get an answer. For now the package supports only strings as data types but I am working to improve this and allowing for other data types, data structures and objects to be stored.


## Methods

- add(args*)
  - Can add multiple elements at a time into the hash list object
- get_item(item=None, index=None)
  - If used with the item argument the object will return a tuple of (key, index)
  - if used with the index argument the object will return the item
- indexes()
  - The method returns a list of all the keys in the hashed list
- remove_item(item=None, index=None)
  - Removes an item form the hashed list either by it's 'name' or by the index. Note that the index should be a tuple of (key, index). 
  - Use the get_item(item=<item_name>) to get the index 
- delete_index(index)
	- The method deletes a key and all the items associated with it. Be careful how you use this method in your code. The index argument expects an integer (int).
- print()
	- Prints the hashed list object contents.
## Usage

Let's create an instance of the class and add some items and print the hash list:

```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')

'''
> Output:
{112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
'''
```

- Note that you can add 1 item at a time or multiple items.
- The resulting hash list is a dictionary that has stored the words in a key:value pair
- The key, for now, is calculated by adding the ASCII values of the letters from the word and dividing the sum to the length of the word:

```python
def __key__(self, word):
		key = sum([ord(letter) for letter in word])//len(word)
		return key
```

- You can see all the public methods that the class offers by running this code:

```python
from hashlist import hast_list
method_list = [method for method in dir(MyClass) if method.startswith('__') is False]
print(method_list)

'''
> Output:
> ['add', 'delete_index', 'get_item', 'indexes', 'print', 'remove_item']
'''
```

- Ok, great! Now let's use some of those methods. let's start with get_item() method.
- get_item(item=None, index=None) will return a tuple of values. The first value in
the tuple is the item's key and the second value will represent the position of the
item in the array:

```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
item = h_lst.get_item(item='my')
print(item)

'''
> Output:
>(115, 0)
'''
```

- But what if you want to get the actual item (in this case the word). Well we can use the get_item() method but towice:
```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
index= h_lst.get_item(item='my')
item = h_lst.get_item(index=index)
print(index)
print(item)
'''
> Output:
> (115, 0)
> my
'''
```

- Now let's use the indexes() method. This method return a list of all the keys that are in your hash list
```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
all_indexes = h_lst.indexes()
print(all_indexes)

'''
> Output:
> [112, 115, 103, 111]
'''
```

- Perfect, there are 2 more methods from this class, delete_index() and remove_item(). Let's focus on delete_index(). This method will delete a key form your hash list and all of it's items. Be very careful how you use it:
```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
index = h_lst.indexes()[0]
h_lst.print()
h_lst.delete_index(index)
h_lst.print()

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> {115: ['my'], 103: ['hashed'], 111: ['list']}
'''
```

- And finally we have remove_item(item=None, index=None). This method can delete an item from the hash list either by it's 'name' or by it's index. Let's show them both.
- Removing an item by it's 'name':
```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
h_lst.print() # hash list before removing an item
h_lst.remove_item(item='my')
h_lst.print() # hash list after removing an item

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> {112: ['test', 'python'], 103: ['hashed'], 111: ['list']}
'''
```

- If you can see the class automatically deletes the entire key if there is no value associate with it. In this case the word 'my' had the key 115 but because we removed the item the key has no value associate with it so the class deletes the key.
- Removing an item by it's index:
```python
from hashlist import hast_list
h_lst = hast_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
h_lst.print() # hash list before removing an item
index = h_lst.get_item(item='test')
print(index)
h_lst.remove_item(index=index)
h_lst.print() # hash list after removing an item

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> (112, 0)
> {112: ['python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
'''
```