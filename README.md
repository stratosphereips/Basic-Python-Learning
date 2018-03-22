# Template Program for basic python learning
This is a template for learning python. The idea is to have a template to analyze text files.

The binetflow file in this project is: http://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-184-1/2016-07-29_winn3.binetflow   


## Usage
- If you want to use the graph1.py tool

    ./graph.py -f ~/cloud9/Trabajo/Doctorado/Datasets/Botnet-Captures/CTU-Malware-Capture-Botnet-184-1/2016-07-29_winn3.binetflow > graph.dot
    cat graph.dot |sfdp -Tpng -o graph.png
    open graph.png


- If you want to use the graph1.py tool

    ./graph2.py -f ~/cloud9/Trabajo/Doctorado/Datasets/Botnet-Captures/CTU-Malware-Capture-Botnet-184-1/2016-07-29_winn3.binetflow -m 400 > graph.dot
    cat graph.dot |sfdp -Tpng -o graph.png
    open graph.png

