from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco.txt')

crypto = config.find_objects(r"^crypto map CRYPTO")

for obj in crypto:
    print obj.text
    
    for child in obj.children:
        print child.text

