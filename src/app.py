import json
from DataStructures import Queue
from sms import send

# There queue has to be declared globally (outside any other function)
# That way all methods have access to it
queue = Queue(mode="FIFO")
# FIFO = First in, first out
    
def print_queue():
    # You must print on the console the entire queue list
    print("Printing the entire list...")
    x = 0
    for name_in_list in queue.get_queue():
        name_in_list = queue.get_queue()[x]["name"]
        print(f"({x+1}) {name_in_list}")
        x+=1

def add():
    name = input("Please, write your name: \n")
    phone_number = input("Please write down your phone number: \n")
    client = {
        "name": name,
        "phone_number": phone_number
    }
    if queue.size() == 1:
        print(f"\nHi {name}, you have ({queue.enqueue(client)}) person ahead of you.")
    else:
        print(f"\nHi {name}, you have ({queue.enqueue(client)}) people ahead of you.")

def dequeue():
    if queue.size() == 0:
        print("There are no people on the list, try another option.")
    else:
        name_ready_to_eat = queue.get_queue()[0]["name"]
        print(f"{name_ready_to_eat} it's your turn, we'll remove you from the waiting list.")
        send("Hi " + name_ready_to_eat + ", your table is ready!!", queue.get_queue()[0]["phone_number"])
        queue.dequeue()

def save():
    def write_json(data, filename='queue.json'):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    write_json(queue.get_queue())
    print("Changes were saved!")

def load():
    file = open('queue.json',)
    data = json.load(file)
    queue.get_queue().clear()
    for index in data:
        queue.get_queue().append({"name":index["name"],"phone_number":index["phone_number"]})
    return queue.get_queue()

load()
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        print(load())
    elif option == 6:
        option = str(input("Would you like to save changes???  Y/N: "))
        if option == "y" or option == "Y":
            save()
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
