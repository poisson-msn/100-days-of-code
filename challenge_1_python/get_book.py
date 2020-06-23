def get_book(index):
    items = ['note', 'notebook', 'sketchbook']
    try:
        print(items[index])
    except IndexError:
        print('index error')
    except TypeError:
        print('type error')
    else:
        print('no error')
    finally:
        print('end')

# it can't be true: type error
get_book(input())
