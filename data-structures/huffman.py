import sys

class HuffmanNode(object):
    def __init__(self, char: str, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        Helper to use the comparison operator in
        the heapq library
        """
        return self.freq < other.freq

class HuffmanEncoder(HuffmanNode):
    def __init__(self, data=""):
        if not isinstance(data, str):
            raise Exception("Input has to be a string")

        elif len(data) < 1:
            raise Exception("Input has to have at least 1 character")

        else:
            self.data = str(data)
            self.data_size = sys.getsizeof(self.data)
            self.tree = self.build_huffman_tree()
            self.encoding = self.get_huffman_encoding()
            self.encoding_size = sys.getsizeof(int(self.encoding, base=2))

    def get_huffman_encoding(self) -> str:
        """
        Return
          encoing: the Huffman encoding of a string of data
        """
        encoding = ""
        code_table = self._build_huffman_code_table()

        for char in self.data:
            encoding += code_table[char]

        return encoding

    def build_huffman_tree(self) -> HuffmanNode:
        """
        Return
          tree: The root of a Huffman tree in a heap
        """
        import heapq

        tree = self._get_huffman_frequencies()
        heapq.heapify(tree)

        while len(tree) != 1:
            root = HuffmanNode(None, 0)
            left = heapq.heappop(tree)
            right = heapq.heappop(tree)
            root.left = left
            root.right = right
            root.freq = left.freq + right.freq
            heapq.heappush(tree, root)

        return tree[0]

    def _build_huffman_code_table(self) -> dict:
        """
        Return
          table: Huffman code table based on each
                 character's frequency
        """
        # traverse down the Huffman tree to Huffman
        # encode a char
        def _encode(node: HuffmanNode, code=""):
            if node is None or node.freq == 0:
                return

            if node.left is None and node.right is None:
                table[node.char] = code

            _encode(node.left, code + "0")
            _encode(node.right, code + "1")

        table = {}
        _encode(self.tree)

        # for 1 frequency data
        if len(table) == 1:
            table = {k: "0" for k in table.keys()}

        return table

    def _get_huffman_frequencies(self) -> list:
        """
        Helper function to generate a frequency table
        sorted by increasing frequency

        Return
          freq_sorted: sorted list of tuples (freq, char)
        """
        freq_dict = {}

        for char in self.data:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1

        frequencies = sorted(zip(
            freq_dict.values(), freq_dict.keys()
        ))

        for i, freq in enumerate(frequencies):
            frequencies[i] = HuffmanNode(freq[1], freq[0])

        return frequencies

    def __repr__(self):
        string = (
            f"The size of the data is: {self.data_size}\n"
            f"The content of the data is: {self.data}\n\n"
            f"The size of the encoded data is: {self.encoding_size}\n"
            f"The content of the encoded data is: {self.encoding}"
        )
        return string

class HuffmanDecoder:
    def __init__(self, encoding: str, tree: HuffmanNode):
        if not set(encoding).union(set({"0", "1"})) == set({"0", "1"}):
            raise Exception("Input can only have 0s and 1s")

        elif not isinstance(tree, HuffmanNode):
            raise Exception("Tree has to be a Huffman node instance")

        else:
            self.encoding = str(encoding)
            self.tree = tree
            self.decoding = self.decode()
            self.decoding_size = sys.getsizeof(self.decoding)

    def decode(self) -> str:
        # for 1 character encodings
        if len(set(self.encoding)) == 1:
            return self.tree.char * len(self.encoding)

        counter = 0
        decoder = ""
        while counter < len(self.encoding):
            node = self.tree

            while node.left is not None and node.right is not None:
                if self.encoding[counter] == "0":
                    node = node.left
                else:
                    node = node.right
                counter += 1

            decoder += node.char

        return decoder

    def __repr__(self):
        string = (
            f"The size of the decoded data is: {self.decoding_size}\n"
            f"The content of the encoded data is: {self.decoding}"
        )
        return string
