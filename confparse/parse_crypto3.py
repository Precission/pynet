from ciscoconfparse import CiscoConfParse

config = CiscoConfParse('cisco.txt')

crypto = config.find_objects(r"^crypto map CRYPTO")

for obj in crypto:
    aes_found = False
 
    for child in obj.children:
        if 'AES' in child.text:
            aes_found = True

    if aes_found == False:
        print obj.text
