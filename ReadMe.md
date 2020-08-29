
# MATRIX VIRUS SPREAD PROBLEM

The files in a folder are stored in an nXm matrix, where n gives the number of rows and m gives the number of columns. The numbering system starts from (1,1).

There is a powerful virus in one of the files and the location of the file is given by (r,c).

The virus spreads to adjacent blocks in one second. From each infected block, it takes another second to spread to its adjacent blocks. And so on.

For example, if the virus is at (1,1), it takes a second to spread to the blocks (1,2), (2,1) and (2,2). After two seconds, the infected blocks are (1,1), (1,2), (2,1), (2,2), (1,3), (2,3), (3,3), (3,2), (3,1).

And so on.

So, given the values of n, m and (r,c), find the number of seconds it will take to spread through the entire folder.

Input Format

The input contains:

The first line contains t test cases.

Each test case contains two lines:

The first line contains n and m separated by a space. Next line of the test case contains (r,c) which gives the position of the virus infected file in the folder. Output Format

The output contains t lines each of which contains the time needed for the virus to spread to the entire folder in minutes and seconds. Note that if the time taken is less than a minute, the output should be x seconds. If the time is 1 second, the output should be 1 second. If the time is 1 minute, then the time should be output as 1 minute 0 seconds. See the test cases for clarity.

Sample Input

3

6 5

(2,2)

100 50

(39,5)

44 130

(1,1)

Sample Output

4 seconds

1 minute 1 second

2 minutes

9 seconds

Explanation

For the first test case, there are 6 rows and 5 columns. The virus is at position (2,2) it will take 1 second to spread to (1,1), (1,2), (1,3), (2,1), (2,3), (3,1), (3,2), (3,3). From there it will take 1 more second to spread to adjacent files. To spread to all the files, it will take total of 4 seconds.
