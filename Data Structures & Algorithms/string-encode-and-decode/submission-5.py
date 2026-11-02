class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += f"¶{len(string)}¶{string}"
        return encoded_str


    def decode(self, s: str) -> List[str]:
        index = 0
        decoded_strs = []
        start = False
        length = ""
        
        while index < len(s):

            if s[index] == "¶" and not start:
                start = True
            
            elif s[index] == "¶" and start:
                start = False 
                decoded_strs.append(s[index+1:index+int(length)+1])
                length = ""
            
            elif start:
                length += s[index]
            
            index += 1
        
        return decoded_strs