# simple_Hadoop_MapReduce_example
A simple example of Hadoop MapReduce in Python.

Adapted from [here](http://www.science.smith.edu/dftwiki/index.php/Hadoop_Tutorial_2_--_Running_WordCount_in_Python).


If you want to test that the mapper is working, you can do something like this:

`python mapper.py < shakespeare.txt | tail`

This takes the file shakespeare.txt as input for mapper.py and shows the last few lines of output.

Similarly, you can see if the reducer is working like so:

`python mapper.py < shakespeare.txt > map_output.txt`
`python reducer.py < map_output.txt`

This creates the file `map_output.txt` by processing shakespeare.txt with mapper.py, and then uses reducer.py to process the map_output.txt file. 

You can get the shakespeare.txt file with `wget https://norvig.com/ngrams/shakespeare.txt`

Testing the files in this way is much easier than trying to debug the errors from Hadoop streaming.  The errors from using Python above will be Python errors and easier to read than the complex Hadoop Java errors.