class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = "\x1f"

        if not strs:
            return "\u00a4"

        return delimiter.join(strs) + delimiter

    def decode(self, s: str) -> List[str]:
        if s == "\u00a4":
            return []

        cur_str = ""
        result = []
        for c in s:
            if (c == "\x1f"):
                result.append(cur_str)
                cur_str = ""
                continue
            cur_str = cur_str + c
        return result
