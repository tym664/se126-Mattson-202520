determine_ip_class = 0
ip_address = 0 
octets = 0
more_data = "y"
first_octet = 0 

while more_data == "y":
    ip_address= str(input("Enter an IP address:"))
    octets = ip_address.split(".")
    firstOctet = int(octets[0])
    if(firstOctet >= 1 and firstOctet <= 127):
            print ("Class A")
            more_data = input("Do you wish to contiune? (Y/N)").lower() 
            
    elif(firstOctet >= 128 and firstOctet <= 191):
        print ("Class B")
        more_data = input("Do you wish to contiune? (Y/N)").lower()
    
    elif(firstOctet >= 192 and firstOctet <= 223):
            print ("Class C")
            more_data = input("Do you wish to contiune? (Y/N)").lower()
 
    else:
       print ("Not a class A, B, or C")
       print ("Invalid IP address format")
       more_data = input("Do you wish to contiune? (Y/N)").lower()
           



    


