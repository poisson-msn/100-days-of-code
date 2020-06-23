dict_a = {'x': 'note', 'y': 'notebook'}

books = 'I like {x}, but I hate {y}'
print(books.format(**dict_a))
