## Description

This package is meant to store data in a smart way so when you are dealing with large amounts of data it will be faster to query the list and get an answer. For now the package supports only strings as data types but I am working to improve this and allowing for other data types, data structures and objects to be stored.


## Methods

- add(args*)
  - Can add multiple elements at a time into the hash list object
- get_item_index(item)
  - Returns a tuple of form (key, index)
- get_item_by_index(index)
  - Returns the item by providing the index (key, index)
- remove_item_by_index(index)
  - Removes an item form the hashed list either by it's index. Note that the index should be a tuple of (key, index). 
- remove_item_by_name(item)
  - Removes the item by it's 'name'.
- delete_key(key)
	- The method deletes a key and all the items associated with it. Be careful how you use this method in your code. The index argument expects an integer (int).
- keys()
  - The method returns a list of all the keys in the hashed list
- print()
	- Prints the hashed list object contents.



## Usage

- To get this module you can install it by using pip as follows:

```bash
pip install hashlist
```

- If you have hashlist installed update it from time to time using this command:

```bash
pip install --upgrade hashlist
```

- Once you have your module installed let's create an instance of the class and add some items and print the hash list:

```python
from hashlist import hash_list

h_lst = hash_list()
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
def _key(self, word):
    if word:
        key = sum([ord(letter) for letter in word])//len(word)
        return key
    raise TypeError('Argument can not be None')
```

- You can see all the public methods that the class offers by running this code:

```python
from hashlist import hash_list

method_list = [method for method in dir(hash_list) if method.startswith('_') is False]
print(method_list)

'''
> Output:
> ['add', 'delete_index', 'get_item_by_index', 'get_item_index', 'indexes', 'print', 'remove_item_by_index', 'remove_item_by_name']
'''
```

- Ok, great! Now let's use some of those methods. let's start with get_item_index() method.
- get_item_index(index) will return a tuple of values. The first value in
the tuple is the item's key and the second value will represent the position of the
item in the array:

```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
item = h_lst.get_item_index('my')
print(item)

'''
> Output:
>(115, 0)
'''
```

- But what if you want to get the actual item (in this case the word). Well we can use the get_item_index() and get_item_by_index():
```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
index= h_lst.get_item_index('my')
item = h_lst.get_item_by_index(index)
print(index)
print(item)
'''
> Output:
> (115, 0)
> my
'''
```

- Now let's use the keys() method. This method return a list of all the keys that are in your hash list
```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
all_keys = h_lst.keys()
print(all_keys)

'''
> Output:
> [112, 115, 103, 111]
'''
```

- You can use the delete_key() method to delete a key from the hash list. 
```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
key = h_lst.keys()[0]
h_lst.print()
h_lst.delete_key(key)
h_lst.print()

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> {115: ['my'], 103: ['hashed'], 111: ['list']}
'''
```


- If you want to delete an item from the hash list but you don't know it's (key, index) you can use the remove_item_by_name()
```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
h_lst.print() # hash list before removing an item
h_lst.remove_item_by_name('my')
h_lst.print() # hash list after removing an item

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> {112: ['test', 'python'], 103: ['hashed'], 111: ['list']}
'''
```

- If you can see the class automatically deletes the entire key if there is no value associate with it. In this case the word 'my' had the key 115 but because we removed the item the key has no value associate with it so the class deletes the key.
- You can remove an item by using it's (key, index) by using remove_item_by_index() method:
```python
from hashlist import hash_list

h_lst = hash_list()
h_lst.add('test', 'my', 'python', 'hashed', 'list')
h_lst.print() # hash list before removing an item
index = h_lst.get_item_index('test')
print(index)
h_lst.remove_item_by_index(index)
h_lst.print() # hash list after removing an item

'''
> Output:
> {112: ['test', 'python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
> (112, 0)
> {112: ['python'], 115: ['my'], 103: ['hashed'], 111: ['list']}
'''
```
