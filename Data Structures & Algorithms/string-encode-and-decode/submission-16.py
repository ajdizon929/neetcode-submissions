class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            length = len(s)
            result.append(str(length)+"#"+s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        reading = False
        str_buffer = []
        str_len = int()

        for c in s:
            # Check for #
            if (not reading) and (c=="#"):
                # if valid length, reset the string and update count
                len_str = "".join(str_buffer)
                if (len_str.isdigit()):
                    str_buffer = []
                    str_len = int(len_str)
                    if (str_len == 0):
                        result.append("".join(str_buffer))
                        continue
                    reading = True
                continue

            str_buffer.append(c)
            if reading:
                str_len -= 1
                if str_len == 0:
                # done reading len of str, reset state
                    result.append("".join(str_buffer))
                    reading = False
                    str_buffer = []
                    continue   

        return result
