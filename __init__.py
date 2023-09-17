import os

print ("Initializing example_app folder: " + os.getcwd())
if (os.path.exists("kanban/services.py")):
    from . import services
else:
    print("Services file does not exist")
    
