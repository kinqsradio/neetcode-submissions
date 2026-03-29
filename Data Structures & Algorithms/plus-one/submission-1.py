class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        combined_string = "".join(map(str, digits))
        combined_number = int(combined_string)+1

        return [int(d) for d in str(combined_number)]        