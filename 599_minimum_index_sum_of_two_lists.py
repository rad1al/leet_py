class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1_index_dict = {item : i for i, item in enumerate(list1)}
        l2_index_dict = {item : i for i, item in enumerate(list2)}
        results = dict()
        for item_a in l1_index_dict:
            if item_a in l2_index_dict:
                results[item_a] = l1_index_dict[item_a] + l2_index_dict[item_a]
        min_val = min(results.values())
        output = [k for k in results if results[k] == min_val]
        return output
        