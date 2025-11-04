class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        I'd approach this problem by using a hash map.
        First, iterate through each string in the list and sort its characters.
        Then, use the sorted string as a key in the hash map.
        If the key already exists, append the original string to that key's list.
        Finally, return all the grouped values as the result.
        """

        # Initialize a hash map with list as the default value type
        hash_map = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Sort the string to create a key representing its character composition
            sorted_s = ''.join(sorted(s))

            # Append the original string to the list of its corresponding sorted key
            hash_map[sorted_s].append(s)
        
        # Convert the hash map values into a list of lists and return it as the output
        return list(hash_map.values())

        """
        The time complexity is O(n * k log k) because each string of length k
        needs to be sorted, and there are n strings in total.
        The space complexity is O(n * k) because the hash map stores
        all input strings grouped by their sorted keys.
        """
