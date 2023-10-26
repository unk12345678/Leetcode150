"""
Problem Description:
The task is to encode a list of strings into a single string and decode it back. 
The encoded format should help in reconstructing the original list without ambiguity.
"""

class Codec:
    def encode(self, strs):
        # For each string in the input list, prefix the string with its length followed by a '#'.
        # The '#' serves as a delimiter to know where the length of the string ends and the string begins.
        # Finally, join all these prefixed strings to produce the encoded result.
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        res = []  # Resultant list to store the decoded strings
        i = 0  # Current position pointer
        
        while i < len(s):
            # Find the position of the next '#' to determine the length of the string.
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract the length of the string
            
            # Use the length to get the actual string.
            i = j + 1
            j = i + length
            res.append(s[i:j])  # Append the extracted string to the result list
            i = j
            
        return res

# Time Complexity: 
# Encoding: O(n), where n is the total number of characters in all strings.
# Decoding: O(n), where n is the length of the encoded string.

# Space Complexity: 
# Encoding: O(1), as no additional space is used.
# Decoding: O(m), where m is the number of strings in the original list.

"""
The encode method works by prefixing each string with its length followed by a '#'. 
The length helps in understanding where each string starts and ends during decoding. 
The decode method uses this information to extract each string from the encoded format and constructs the original list.
"""
