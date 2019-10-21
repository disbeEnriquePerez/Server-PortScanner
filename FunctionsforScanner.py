

def response():
    print("""
            1)SYN ACK Scan
            2)UDP Scan
            3)Comprehensive Scan""")
    resp2 = input("Please Enter the Scan you want to use: ")
    if int(resp2) > 3 or int(resp2) < 1:
        resp2 = ""
        response() 
    else:
        return resp2