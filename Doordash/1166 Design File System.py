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
        

### Sol2: Trie
# Create a class for trie node
class TrieNode(object):
    def __init__(self, name):
        self.map = defaultdict(TrieNode)  # children
        self.name = name
        self.value = -1
        
class FileSystem(object):

    def __init__(self):
        # Initialize the root
        self.root = TrieNode("")
        
    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        ### Create a new path and associate a value to it
        # Split the path into several parts based on "/"
        path_components = path.split("/")[1:]
        print("components:", path_components)
        
        curr = self.root
        for i in range(len(path_components)):
            name = path_components[i]
            if i == len(path_components) - 1:
                if name not in curr.map:
                    curr.map[name] = TrieNode(name)
                    curr.map[name].value = value
                    return True
                else:
                    return False  
            else:
                # Not the last component
                if name not in curr.map:
                    return False
                else:
                    # move on
                    curr = curr.map[name]
        return False
        
    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        ### Returns the value associated with path
        path_components = path.split("/")[1:]
        print("components: ", path_components)
        
        curr = self.root
        for i in range(len(path_components)):
            name = path_components[i]
            if name not in curr.map:
                return -1
            curr = curr.map[name]
        return curr.value
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
