![perm append multiple](https://github.com/markedwinharvey/permutations/blob/master/media/perm_fig.png)

`Permutations` ('perm') generates a variable-length list of permuted integer values from 0 -> (n-1). 

The goal was to generate a permuted set of values that can be reliably reconstructed
simply by using the same iterator value. 

The values are generated by sampling a sine wave at a user-determined frequency; 
values other than 2*pi (and its multiples) can produce reasonable (though variably periodic) scatter. 
By default, a list of 100 points is given, with an iterator (frequency) of 0.1, meaning that 
the sine wave is sampled at intervals of 0.1. 
Duplicates are rejected and sampling will repeat until the permutation list contains all unique values. 
The dynamic iterator option 'animate single' is selected by default, which will show 
dynamic behavior as the iterator increases over time. Alternatively, 'append multiple' 
displays html plot data as shown in the above figure, where each new plot appended to the interface 
is a result of increasing the iterator number. 

The program is run from the command line with the following invocation: `python perm.py`. 

This script attempts to start a local server on port 8000. 

The script loads an html page in the default browser. This can be changed to a preferred browser in `perm.py`.
 
The program `perm.py` loads data from `perm.html`, an html gui for selecting set length, sampling interval, and iterator options. 

Pressing 'visualize' sends data to `perm_op.py` for processing. 

The script `perm_op.py` generates data and passes it back to `perm.html` for dynamic updates. 
New content is then appended to the document. 

