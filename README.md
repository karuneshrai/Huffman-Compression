# Huffman compressor and de-compressor
This algorithm can compress a large text for instance a Sherlock Holmes novel and another algorithm can DE-compress the compressed text. 
## INTRODUCTION
Huffman coding is an encoding technique which is used in data compression.The idea involves assigning particular binary numbers(called codewords) to all letters based on their frequency of occurrence.The assigning of codewords is done in such a way that no codeword is a prefix of any other codeword.It uses the idea of a binary tree to assign a unique codeword to every letter.

## GETTING STARTED 
There are two major parts in Huffman Coding:
1) Build a Huffman Tree from input characters.
2) Traverse the Huffman Tree and assign codes to characters.

Firstly we must surf our sample text to find the frequency of occurrence of each letter.
Then we would assign each letter the codeword such that the letters with higher frequency would get a codeword which has shorter length i.e. they would be assigned codewords which occur at the top of the tree.The codeword is basically made as follows:
1)Take an empty string and as you traverse towards left in the tree add “0” to the sting.
2)Moving towards right at a step would lead to addition of “1” instead of “0” 

Once codewords are assigned to each letter,simply replace the letters with their respective codewords.

## BUILDING A HUFFMAN TREE
1. Create a leaf node for unique character and build a table of all leaf nodes.
2. Extract two nodes of minimum frequency from the table and combine them to form a new node with value being equal to the sum of their values.
3. Repeat step 2 until the table contains only one node.
