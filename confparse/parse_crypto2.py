from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco.txt')

crypto = config.find_objects(r"^crypto map CRYPTO")

for obj in crypto:
    
    for child in obj.children:
        if 'pfs group2' in child.text:
            print obj.text
