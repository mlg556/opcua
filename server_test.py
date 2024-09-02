# first install opcua-asyncio with "pip install asyncua"
# then run server_test.py
# while running, run client_test.py

import sys
import time

from asyncua.sync import Server

sys.path.insert(0, "../..")

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# set up our own namespace, not really necessary but should as spec
uri = "http://examples.freeopcua.github.io"
idx = server.register_namespace(uri)

test_obj = server.nodes.objects.add_object(idx, "TestObject")
test_var = test_obj.add_variable(idx, "TestVariable", 42)
test_var.set_writable()

# starting!
server.start()

print("Server running...")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    server.stop()
    print("EXIT")


