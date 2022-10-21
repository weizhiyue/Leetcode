### Sol1: Hashmap
class FileSystem(object):
    def __init__(self):
        # A path is a node of a tree
        # Use hash table to store the valid paths along with their values
        self.path_dict = {}
        
    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        ### Create a new path and associate a value to it
        # check whether the path is valid or not
        # Q: need checking if there are non-English letters existing?
        if not path or path == "/":
            return False
        if path in self.path_dict:
            return False
        
        split_path = path.split("/")
        parent_path = "/".join(split_path[:-1])
        
        # check the presence of its parent path
        if not parent_path or parent_path in self.path_dict:
            self.path_dict[path] = value
            return True
        else:
            return False
        
    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        ### Returns the value associated with path
        if path in self.path_dict:
            return self.path_dict[path]
        else:
            return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
