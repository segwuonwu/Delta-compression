# Delta Compression - Decoding
### Programming challenge description:
In data transmission, delta compression is used to encode data as a difference between successive values (e.g. bytes), rather than using the values themselves.

Let's look on an example of how to encode the byte sequence 28 30 33 30 28 29 31 66 65 65 65 64 using delta compression. The first value is simply copied from the original data to the delta encoded output stream. Each subsequent value in the output stream is equal to the difference (i.e. delta) between the corresponding value in the input stream and the prior value in the input stream.

Decoding reverses the compression process by consecutively summing (i.e. accumulating) the differences starting from the first value.

### Write a program to decode a delta encoded stream.

Input:
A delta encoded stream expressed as a space-delimited list of integers. For example:

28 2 3 -3 -2 1 2 35 -1 0 0 -1  
Output:  
Print a decoded (source) data stream as a space-delimited list of integers. For example, the input above should result in:  
28 30 33 30 28 29 31 66 65 65 65 64  

Test 1  
Test Input  
Download Test 1 Input  
28 2 3 -3 -2 1 2 35 -1 0 0 -1  
Expected Output  
Download Test 1 Input  
28 30 33 30 28 29 31 66 65 65 65 64  

Test 2  
Test Input  
Download Test 2 Input  
5 1 1 1 1 0 0 0 -1 -1 -1 -1  
Expected Output  
Download Test 2 Input  
5 6 7 8 9 9 9 9 8 7 6 5  

Test 3  
Test Input  
Download Test 3 Input  
14 2 -2 -3 0 -1 4 0 -1 1 4 -2 -3 -3 -2  
Expected Output  
Download Test 3 Input  
14 16 14 11 11 10 14 14 13 14 18 16 13 10 8  

Test 4  
Test Input  
Download Test 4 Input  
-123 -11 6 14 -1 -3 4 9 1 5 -6 3 -10 155 -7 0 14 -9 15 3 11 -1 -10 -8 5  
Expected Output  
Download Test 4 Input  
-123 -134 -128 -114 -115 -118 -114 -105 -104 -99 -105 -102 -112 43 36 36 50 41 56 59 70 69 59 51 56
