import sys

from asyncua.sync import Client

sys.path.insert(0, "../..")

with Client("opc.tcp://localhost:4840/freeopcua/server/") as client:
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
    # Node objects have methods to read and write node attributes as well as browse or populate address space
    # print("Children of root are: ", client.nodes.root.get_children())

    test_var = client.nodes.root.get_child(["0:Objects", "2:TestObject", "2:TestVariable"])
    # print(test_var)
    print(f"old value: {test_var.read_value()}")
    test_var.write_value(99)
    print(f"new value: {test_var.read_value()}")
    test_var.write_value(42)
    print(f"reset to: {test_var.read_value()}")