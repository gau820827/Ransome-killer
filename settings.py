

# This is the original pcap source
dirNorName = ['./normal_pcap/train/',
              './normal_pcap/test/']
dirMalName = ['./malware_pcap/train_source',
              './malware_pcap/test_source']


# This is where the extraction data
inputMalName = ['./dataset/malware_feature.train',
                './dataset/malware_feature.test']
inputNorName = ['./dataset/normal_feature.train',
                './dataset/normal_feature.test']


# Final labeled train and test dataset
outputDataName = ['./dataset/train.in',
                  './dataset/test.in']
outputLabelName = ['./dataset/train.out',
                   './dataset/test.out']