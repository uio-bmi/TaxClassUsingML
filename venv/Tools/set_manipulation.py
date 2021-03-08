class SetManupulation:

    # Method takes a set of lists and returns the length of the longest list.
    @staticmethod
    def findLongestList(lists):
        longestLength = 0
        for list in lists:
            if len(list) > longestLength:
                longestLength = len(list)
        return longestLength


    # ER IKKE I BRUK
    # Method takes a list of elements which may contain duplicates and returns a list where every element is unique.
    @staticmethod
    def __uniqueElements(list):
        unique_list = []
        # Add every new k-mer discovered to the output arrays.
        while len(list) > 0:
            elem = list[0]
            unique_kmers.append(elem)
            # Look for other identical k-mers in the list, count them and delete them.
            index = 1
            while index < len(list):
                other = list[index]
                if elem == other:
                    del list[index]
                    if index > 1:
                        index -= 1
                index += 1
            # Delete the k-mer which has been added to the list so it's only counted once.
            del list[0]
        return unique_list