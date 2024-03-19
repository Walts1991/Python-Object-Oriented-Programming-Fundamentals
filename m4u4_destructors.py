#Destructors free up space in computer memory
#Python no longer needs object - deletes for space

class MyClass:
    def __init__(self):
        print('Creating new object...')

    def __del__(self):
        print('Destroying used object...')

def main():
    object1 = MyClass()
    object2 = MyClass()
    object3 = MyClass()

    print("\n\n")

    del(object1)  # Deleting an object using the 'delete' keyword.
    del(object2)
    del(object3)

#Call main function
main()
