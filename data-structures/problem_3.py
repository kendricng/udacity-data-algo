from huffman import HuffmanEncoder, HuffmanDecoder

import pytest
import sys

def huffman_encoding(data):
    encoder = HuffmanEncoder(data)
    return encoder.encoding, encoder.tree

def huffman_decoding(data,tree):
    decoder = HuffmanDecoder(data, tree)
    return decoder.decoding

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
@pytest.fixture()
def inputs():
    data = [
        None, "", " ", "aaaaa",
        "The quick brown fox jumped over the lazy dog.",
        ("We the People of the United States, in Order to form a more "
         "perfect Union, establish Justice, insure domestic Tranquility, "
         "provide for the common defence, promote the general Welfare, "
         "and secure the Blessings of Liberty to ourselves and our "
         "Posterity, do ordain and establish this Constitution for "
         "the United States of America.")
    ]
    return data

# Test Case 1
def test_null_is_not_valid(inputs):
    with pytest.raises(Exception):
        huffman_encoding(inputs[0])

def test_no_char_is_not_valid(inputs):
    with pytest.raises(Exception):
        huffman_encoding(inputs[1])

# Test Case 2
def test_short_string(inputs):
    for i in (2, 3):
        encoding, tree = huffman_encoding(inputs[i])
        decoding = huffman_decoding(encoding, tree)
        assert inputs[i] == decoding

# Test Case 3
def test_long_string(inputs):
    for i in (4, 5):
        encoding, tree = huffman_encoding(inputs[i])
        decoding = huffman_decoding(encoding, tree)
        assert inputs[i] == decoding
