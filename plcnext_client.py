# %%
# PLCnext Engineer
# OPC UA Settings:
# Basic Settings -> Information Model -> Visibility.. -> Marked
# Security -> Certificate -> Self signed
# Security -> Security Policies -> Enable basic 256 algorithm
#

import sys
from asyncua import ua
from asyncua.sync import Client

# %%
sys.path.insert(0, "../..")

url = "opc.tcp://192.168.1.10:4840"
client = Client(url=url)
client.set_user("admin")
client.set_password("*********")
security_string = "Basic256,Sign,certificate-example.der,private-key-example.pem"
client.set_security_string(security_string)

# %%
client.connect()

# %%
root_children = client.nodes.root.get_children()
for node in root_children:
    print(node.read_browse_name())

print("----")
objects = root_children[1].get_children()
for obj in objects:
    print(obj.read_browse_name())

print("----")
plcn = objects[4]
plcn_children = plcn.get_children()
for pc in plcn_children:
    print(pc.read_browse_name())

print("----")
arp = plcn_children[0]
arp_children = arp.get_children()
for x in arp_children:
    print(x.read_browse_name())

print("----")
inst = arp_children[0]
inst_children = inst.get_children()
for x in inst_children:
    print(x.read_browse_name())
# %%
print("---")

out_var = client.get_node("ns=6;s=Arp.Plc.Eclr/Instance_ServoControl.IP_w_InA")
print(out_var.read_data_type())
print(out_var.get_access_level())
print(out_var.read_value())

# %%
out_var.set_value(ua.DataValue(ua.Variant(16_000, ua.VariantType.UInt16)))


# %%

client.disconnect()
