# Ransome-killer
This is the project on ransomware detection using machine learning technique.

In our experiments, malware pcaps were referenced from [Malware-traffic-analysis](http://www.malware-traffic-analysis.net/)

## Requirements
1. Python 2.7
2. dpkt
3. sklearn

## Data Sets
We gathered 155 different Ransomwares from Feb.2015 to Sep.2016, and seperated them into 7 main families:
> 1. cerber:9
> 2. CrypMic:28
> 3. Cryptowall:34
> 4. CryptXXX:34
> 5. Locky:16
> 6. Teslacrypt:22
> 7. Other:16

We use most three families for experiments: **CryptMic**, **Cryptowall**, and **CryptXXX**

## Extract packets
```
1. Put your ransomware pcap files in malware\_pcap and normal\_pcap
2. Run start.sh to extract http headers from pcap files
```
```
Use pcap_Parser -p if you want to parse TCP payloads
```
## Visulization on payloads
We use PCA to reduce dimensions of initial payloads.
```
python ./visual/pca.py [extracted_data]
```
It will produced a pickle file, and then use
```
python ./visual/show.py [pickle_file]
```
This will show the structure of those payloads.

## Examples

## Training
After PCA as pre-training, we could use those principle components to fit in different ML models.
As an example, we use SVM in sklearn to classify those payloads.
```
python ./model/svm.py [pickle_file]
```
The 5-folds cross validation results of Cryptmic are
```
SVM (C=1, linear kernel)
```
fold-1: 0.82227159 <br>
fold-2: 0.83194444 <br>
fold-3: 0.815      <br>
fold-4: 0.82361111 <br>
fold-5: 0.82272548 <br>


Our Results are published on [IEICE IA 2016](http://www.ieice.org/ken/paper/20161104Gbmd/eng/)
