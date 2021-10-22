* This is an easy to use visualization tool which will make your data visualization easy *
- If you want to use the graph.py tool

    ./graph.py -f ~/cloud9/Trabajo/Doctorado/Datasets/Botnet-Captures/CTU-Malware-Capture-Botnet-184-1/2016-07-29_winn3.binetflow > graph.dot
    cat graph.dot |sfdp -Tpng -o graph.png
    open graph.png


- If you want to use the graph2.py tool

    ./graph2.py -f ~/cloud9/Trabajo/Doctorado/Datasets/Botnet-Captures/CTU-Malware-Capture-Botnet-184-1/2016-07-29_winn3.binetflow -m 400 > graph.dot
    cat graph.dot |sfdp -Tpng -o graph.png
    open graph.png

