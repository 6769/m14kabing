if "%1"=="merge" (
    echo Merge File to _fileName
    mv generated_graph_*.png _generated_graph.png
    mv generated_graph_*.gv  _generated_graph.gv
    rem exit
    )
