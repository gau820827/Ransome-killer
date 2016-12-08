

def handleErrorPacket(packetData):
    """Gets payload even if error raised.
    @param packetData: dick.

    @returns: 
    """
    

    for info in packetData.split("\n"):
        if any(method in info for method in ["GET", "POST", "PUT"]):
            return info.split("HTTP")[0]


def infoDisplay(counter, ipcounter, tcpcounter, udpcounter, httpcounter):
    """Display the information about the connection
    @param *info: those counters in the connection
    
    @returns: None
    """


    print "Total number of packets in the pcap file: ", counter
    print "Total number of ip packets: ", ipcounter
    print "Total number of tcp packets: ", tcpcounter
    print "Total number of udp packets: ", udpcounter
    print "Total number if http requests: ", httpcounter