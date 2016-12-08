""" Capture all packets in malware_pcap and retrieve the malicious parts """

import sys
import os
import dpkt


from settings import *
from util import *

mal_packet = [0,0]
nor_packet = [0,0]

def getPayload(filename, outputName, data_label="malware", mode=1, set_label=0):
    """Get payload according to some constrains.
    
    @parameter   filename: The pcap file you want to extract
               outputName: Write to this file
               data_label: Indicate normal or malware connection
                     mode: The capture mode, 1 for http req
                                             2 for payloads
                set_label: Indicate training set(0) or testing set(0)
    
    @returns: None
    """

    global mal_packet, nor_packet

    ipcounter = 0
    payloadcounter = 0

    outputFile = open(outputName, "a")
    pcapfile = dpkt.pcap.Reader(open(filename, "rb"))

    print 30 * '=' + "\n"
    print "Processing {}\n".format(filename)
    
    for ts, pkt in pcapfile:
        ipcounter += 1
        eth = dpkt.ethernet.Ethernet(pkt)
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue

        """ Include only TCP/IP protocol, 
        however not sure for whether capturing ICMP protocol or not. 
        """
        ip = eth.data
        if ip.p not in (dpkt.ip.IP_PROTO_TCP, dpkt.ip.IP_PROTO_UDP):
            continue
        tcp = ip.data
        
        
        if mode == 2:
            """ Get normal TCP payload """
            if len(tcp.data) > 0 and tcp.dport != 80:
                payloadcounter += 1
                
                print "packet {}: {}".format(ipcounter, len(tcp.data))
                outputFile.write(','.join(format(ord(x)) for x in tcp.data) + '\n')

        
        if mode == 1:
            """ Get http header """
            if tcp.dport == 80 and len(tcp.data) > 0:
                try:
                    http = dpkt.http.Request(tcp.data)
                except dpkt.NeedData:
                    extraction = handleErrorPacket(tcp.data)
                    print "packet {}: Missing Data {}".format(ipcounter, extraction)
                    outputFile.write(",".join(format(ord(x)) for x in extraction) + '\n')
                except dpkt.UnpackError:
                    ''' Invalid request such as some HTML fragments, not for use now '''
                    
                    print "packet " + str(ipcounter) + ": Invalid Request " + tcp.data
                    # outputFilep.write(' '.join(format(ord(x), 'b') for x in tcp.data) + '\n')
                else:
                    print "packet " + str(ipcounter) + ": " + http.method + http.uri
                    outputFile.write(",".join(format(ord(x)) for x in tcp.data) + '\n')

            # print "packet " + str(ipcounter) + " = " + str(len(tcp.data))

    outputFile.close()
    print "Total number of packets in the pcap file: {}".format(ipcounter)
    print "Extract: {}".format(payloadcounter)
    
    if data_label == "malware": mal_packet[catagory] += payloadcounter
    else: nor_packet[catagory] += payloadcounter


if __name__ == '__main__':
    

    """ Mode 1 to capture http request
        Mode 2 to capture tcp payloads
        Default is Mode 1
    """
    mode = 1
    if len(sys.argv) > 1:
        if sys.argv[1] == "-p":
            mode = 2
        else:
            print "Invalid argument, Use Default settings......"


    """ First we handle the malware pcap """
    trainFile = open(inputMalName[0], "w")
    testFile = open(inputMalName[1], "w")

    
    # Traverse pcap files in malware_pcap 
    for catagory in range(2):
        for file in os.listdir(dirMalName[catagory]):
            filepath = os.path.join(dirMalName[catagory], file)
            if ".pcap" in file:
                getPayload(filepath, inputMalName[catagory], data_label="malware", mode=mode, set_label=catagory)


    trainFile.close()
    testFile.close()
    

    """ Second we handle the normal pcap """
    trainFile = open(inputNorName[0], "w")
    testFile = open(inputNorName[1], "w")


    # Traverse pcap files in normal_pcap 
    for catagory in range(2):
        for file in os.listdir(dirNorName[catagory]):
            filepath = os.path.join(dirNorName[catagory], file)
            if ".pcap" in file:
                getPayload(filepath, inputNorName[catagory], data_label="normal", mode=mode, set_label=catagory)

    print "Totally collect {},{} packets from malware connection".format(mal_packet[0],mal_packet[1])
    print "Totally collect {},{} packets from normal connection".format(nor_packet[0],nor_packet[1])

    trainFile.close()
    testFile.close()