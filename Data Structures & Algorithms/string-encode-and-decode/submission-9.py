class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()
        for string in strs:
            length = len(string)
            res += (str(length)+"#"+string)
        return res

    def decode(self, s: str) -> List[str]:
        reading = False
        read_count = int()
        cur_string = str()
        res = []

        for char in s:
            ## Check for #
            if ((not reading) and (char=='#')):
                ## if valid length start reading
                if (cur_string.isdigit()):
                    read_count = int(cur_string)
                    reading = True
                    cur_string = str()
                    ## skip the #
                    if (read_count==0):
                        ## handles empty string
                        res.append(cur_string)
                        reading = False
                        cur_string = str()
                    continue

            if (reading):
                cur_string += char
                read_count -= 1
                ## if done reading then everything reset
                if (read_count==0):
                    res.append(cur_string)
                    reading = False
                    cur_string = str()
            else:
                cur_string += char
            
        return res

            
