# username - galnadler1
# id1      - 209036524
# name1    - Tal baram
# id2      - 206964090
# name2    - Gal nadler


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    complexity:O(1)
    """

    def __init__(self, key=None, value=None, parent=None):
        self.key, self.value, self.parent = key, value, parent
        if key is None:  # node is virtual
            self.left = None
            self.right = None
            self.height = -1
            self.size = 0
            self.Oldheight = 0

        else:  # node is leaf
            self.left = AVLNode(None, None, self)
            self.right = AVLNode(None, None, self)
            self.height = 0
            self.size = 1
            self.Oldheight = 0

    """returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual

	complexity:O(1)
	"""

    def get_key(self):
        return self.key

    """returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual

	complexity:O(1)
	"""

    def get_value(self):
        return self.value

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)

	complexity:O(1)
	"""

    def get_left(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)

	complexity:O(1)
	"""

    def get_right(self):
        return self.right

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent

	complexity:O(1)
	"""

    def get_parent(self):
        return self.parent

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual

	complexity:O(1)
	"""

    def get_height(self):
        if not self.is_real_node():
            return -1
        return self.height

    """returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual

	complexity:O(1)
	"""

    def get_size(self):
        if not self.is_real_node():
            return 0
        return self.size

    """sets key

	@type key: int or None
	@param key: key

	complexity:O(1)
	"""

    def set_key(self, key):
        self.key = key

    """sets value

	@type value: any
	@param value: data

	complexity:O(1)
	"""

    def set_value(self, value):
        self.value = value

    """sets left child

	@type node: AVLNode
	@param node: a node

	complexity:O(1)
	"""

    def set_left(self, node):
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node

	complexity:O(1)
	"""

    def set_right(self, node):
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node

	complexity:O(1)
	"""

    def set_parent(self, node):
        self.parent = node

    """sets the height of the node

	@type h: int
	@param h: the height

	complexity:O(1)
	"""

    def set_height(self, h):
        self.height = h

    """sets the size of node

	@type s: int
	@param s: the size

	complexity:O(1)
	"""

    def set_size(self, s):
        self.size = s

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.

	complexity:O(1)
	"""

    def is_real_node(self):
        if self.key is None:
            return False
        return True

    ###########################################
    #####         added functions        ######
    ###########################################

    """returns balance factor 

    	@rtype: int
    	@returns: returns the balance factor.

    	complexity:O(1)
    	"""

    def BFF(self):
        return self.get_left().get_height() - self.get_right().get_height()

    """sets the heights and sizes by the children 

    	complexity:O(1)
    	"""

    def setHeightAndSize(self):
        self.set_size(1 + self.right.get_size() + self.left.get_size())
        self.set_height(1 + max(self.right.get_height(), self.left.get_height()))

    """returns the successor 

    	complexity:O(log n)
    	"""

    def successor_specific(self):
        node = self
        node = node.get_right()
        if node is None:
            return None
        while node.is_real_node():
            node = node.get_left()
        return node.get_parent()


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
	Constructor, you are allowed to add more fields.

	"""

    def __init__(self):
        self.root = None
        self.max = None


    """searches for a node in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key.

    complexity: O(log n)
    """
    ''

    def search(self, key):
        node = self.get_root()
        if node is None:
            return None
        while node.get_key() != None:
            if key == node.get_key():
                return node  # found
            elif key < node.get_key():
                node = node.get_left()
            else:
                node = node.get_right()
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing

    complexity:O(log n)
    """

    def insert(self, key, val):
        if self.root is None:
            self.root = AVLNode(key, val)
            return 0
        if self.root.get_value() is None:
            self.root = AVLNode(key, val)
            return 0

        parent = None
        cur = self.root
        while cur.get_key() != None:
            parent = cur
            if key < cur.get_key():
                cur = cur.get_left()
            elif key > cur.get_key():
                cur = cur.get_right()
            else:
                cur.set_value(val)
                return 0

        if key < parent.get_key():
            our_node = AVLNode(key, val)
            parent.set_left(our_node)
            our_node.set_parent(parent)
        else:
            our_node = AVLNode(key, val)
            parent.set_right(our_node)
            our_node.set_parent(parent)

        return self.TreeFixer(our_node, True)

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing

    complexity: O( log n )
    """

    def delete(self, node):

        # handeling virtual nodes
        if not node.is_real_node():
            return 0

        # finiding out if has sons
        l = node.get_left()  # left son#
        r = node.get_right()  # right son#
        rr = r.is_real_node()
        ll = l.is_real_node()
        papa = node.get_parent()
        res = 0

        ## leaf
        if (ll == False and rr == False):
            if papa == None:
                node = AVLNode(None)
                self.root = None
                return res
            elif node == papa.get_left():
                papa.set_left(node.get_left())
                node.get_left().set_parent(papa)
            else:
                papa.set_right(node.get_right())
                node.get_right().set_parent(papa)
            node.set_left(None)
            node.set_right(None)
            node.set_parent(None)

        ##node has left cild
        elif (ll == True and rr == False):
            kido = node.get_left()
            if papa == None:
                kido.set_parent(None)
                node.set_left(None)
                self.root = kido
                return res
            if node == papa.get_left():
                papa.set_left(kido)
            else:
                papa.set_right(kido)
            kido.set_parent(papa)
            node.set_left(None)
            node.set_parent(None)

        ##node has right child
        elif (rr == True and ll == False):
            kido = node.get_right()
            if papa == None:
                kido.set_parent(None)
                node.set_right(None)
                self.root = kido
                return res
            if papa.get_left() == node:
                papa.set_left(kido)
            else:
                papa.set_right(kido)
            kido.set_parent(papa)
            node.set_right(None)
            node.set_parent(None)

        ##has two children
        elif (rr == True and ll == True):
            tmp = node.successor_specific()
            tmp_val = tmp.get_value()
            tmp_key = tmp.get_key()
            node.set_value(tmp_val)
            node.set_key(tmp_key)
            papa = tmp.get_parent()
            node = tmp
            kido = node.get_right()
            if papa.get_left() == node:
                papa.set_left(kido)
            else:
                papa.set_right(kido)
            kido.set_parent(papa)
            node.set_right(None)
            node.set_left(None)
            node.set_parent(None)
        node = papa
        res += self.TreeFixer(node)
        return res

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure

    complexity:  O(n)
    """

    def avl_to_array(self):
        return self.avl_to_array_rec(self.get_root())

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 

    complexity:O(1) 
    """

    def size(self):
        if self.get_root() == None or not self.get_root().is_real_node():
            return 0
        return self.get_root().get_size()

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.

    complexity: O(log n )
    """

    def split(self, node):
        left_tree = AVLTree()
        right_tree = AVLTree()
        left_tree.root = node.get_left()
        right_tree.root = node.get_right()

        # disconnect node from these trees
        left_tree.get_root().set_parent(None)
        right_tree.get_root().set_parent(None)
        node.set_right(None)
        node.set_left(None)

        while node is not None:

            # if node has no parent
            if node.get_parent() == None:
                if left_tree.get_root().is_real_node() == False:
                    left_tree.root = None
                if right_tree.get_root().is_real_node() == False:
                    right_tree.root = None
                return [left_tree, right_tree]

            # if node does have parent, check right or left
            node2 = node.get_parent()
            has_left_parent = True if node2.get_left() == node else False

            if not has_left_parent:
                # join the new tree
                l = AVLTree()
                l.root = node2.get_left()
                # diconnect l from node2
                node2.set_left(None)
                l.get_root().set_parent(None)
                left_tree.join(l, node2.get_key(), node2.get_value())

                node = node2
            else:
                r = AVLTree()
                r.root = node2.get_right()
                # diconnect r from node
                node2.set_right(None)
                r.get_root().set_parent(None)
                right_tree.join(r, node2.get_key(), node2.get_value())

                node = node2

        if left_tree.get_root().is_real_node() == False:
            left_tree.root = None
        if right_tree.get_root().is_real_node() == False:
            right_tree.root = None
        return [left_tree, right_tree]

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined +1

    complexity: O( log n )
    """

    def join(self, tree, key, val):
        x = AVLNode(key, val)
        # None cases
        if tree.get_root() is None and self.get_root() is None:
            self.insert(key, val)
            self.update_root()
            tree.root = self.get_root()

            return 1
        elif tree.get_root() is None:
            self_height = abs(self.get_root().get_height())
            self.insert(key, val)
            self.update_root()
            tree.root = self.get_root()

            return self_height + 2
        elif self.get_root() is None:
            tree_height = tree.get_root().get_height()
            tree.insert(key, val)

            tree.update_root()
            self.root = tree.get_root()
            return tree_height + 2

        # Handeling virtual children
        if tree.get_root().get_value() == None and self.get_root().get_value() == None:
            self.insert(key, val)
            self.update_root()
            tree.root = self.get_root()

            return 1
        elif tree.get_root().get_value() == None:
            self_height = abs(self.get_root().get_height())
            self.insert(key, val)

            self.update_root()
            tree.root = self.get_root()
            return self_height + 2
        elif self.get_root().get_value() == None:
            tree_height = tree.get_root().get_height()
            tree.insert(key, val)

            tree.update_root()
            self.root = tree.get_root()
            return tree_height + 2

        a = self.get_root().get_value()
        self_height = self.get_root().get_height()
        tree_height = tree.get_root().get_height()
        dif = self_height - tree_height
        res = abs(dif) + 1
        two = AVLNode(None, None, None)  ##for the future
        if (dif <= 0 and a < val) or (dif >= 0 and a > val):
            if a > val:
                start = self.get_root()
                one = tree.get_root()
                finish = tree.get_root().get_height()
            else:
                start = tree.get_root()
                one = self.get_root()
                finish = self.get_root().get_height()

            while start.get_left().get_value() is not None and start.get_left().get_height() > finish:
                two = start
                start = start.get_left()

            one.set_parent(x)
            start.set_parent(x)
            x.set_left(one)
            x.set_right(start)

            if two.is_real_node():
                two.set_left(x)
                x.set_parent(two)

            self.update_root()
            tree.update_root()
            self.TreeFixer(x)
            return res

        else:
            if a > val:
                start = tree.get_root()
                one = self.get_root()
                finish = self.get_root().get_height()
            else:
                start = self.get_root()
                one = tree.get_root()
                finish = tree.get_root().get_height()

            while (start.get_right().get_value() is not None) and (start.get_right().get_height() > finish):
                two = start
                start = start.get_right()
            one.set_parent(x)
            start.set_parent(x)
            x.set_left(start)
            x.set_right(one)

            if two.is_real_node():
                two.set_right(x)
                x.set_parent(two)

            self.update_root()
            tree.update_root()
            self.TreeFixer(x)

            return res

    """compute the rank of node in the self

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self

    complexity:O(log n)
    """

    def rank(self, node: AVLNode):
        if node == None or not node.is_real_node():
            return None
        y = node
        cur = y.get_left().get_size() + 1  ##if y is root##

        while y.get_parent() is not None:
            if y.get_parent().get_right() is y:  # from y going up and then back down#
                cur += y.get_parent().get_left().get_size() + 1
            y = y.get_parent()

        return cur

    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self

    complexity: O(log n)
    """

    def select(self, i):

        def select_rec(node: AVLNode, j):
            r = 0

            r = node.get_left().get_size() + 1 if node.is_real_node() else 0
            if j == r:
                return node
            elif j < r:
                return select_rec(node.get_left(), j)
            # search for the j'th smallest item in the left subtree
            else:
                return select_rec(node.get_right(), j - r)
            # search for the j-r'th smallest item in the right subtree

        return select_rec(self.get_root(), i)

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty

    complexity:O(1)
    """

    def get_root(self):
        return self.root

    ###########################################
    #####         added functions        ######
    ###########################################

    """returns the minimum of the tree

    @rtype: AVLNode
    @returns: the node with the minimal value

    complexity:O(log n)
    """

    def min_tree(self):
        x = self.get_root()
        while x.get_left().get_value() != None:
            x = x.get_left()
        return x

    """returns the maximum of the tree

    @rtype: AVLNode
    @returns: the node with the maxmimal value

    complexity:O(log n)
    """

    def max_tree(self, node: AVLNode):
        if self.max is None:
            if node.get_value() is None:
                return None
            else:
                self.max = node
                return node
        if node.get_value() is None:
            return self.max
        if self.max.get_value() > node.get_value():
            return self.max
        else:
            self.max = node
            return node

    """updates the tree root


     complexity:O(log n)
     """

    def update_root(self):
        x = self.get_root()
        while x != None:
            x.setHeightAndSize()
            self.root = x
            x = x.parent

    """returns an array representing dictionary 

    	@rtype: list
    	@returns: a sorted list according to key of touples (key, value) representing the data structure

    complexity:  O(n)
    """

    def avl_to_array_rec(self, node):
        if node == None or not node.is_real_node():
            return []
        left_list = self.avl_to_array_rec(node.get_left())
        node_list = [(node.get_key(), node.get_value())]
        right_list = self.avl_to_array_rec(node.get_right())

        return left_list + node_list + right_list

    """Fixes and rebalances tree if needed

    	@param node: a pointer to the node that we are checking for rebalancing
    	@rtype: int
    	@returns: the number of rebalancing operation due to AVL rebalancing
    	complexity:O(log n)
    	"""

    def TreeFixer(self, node, is_insert=False):
        cur = node
        while cur != None:
            cur.Oldheight = cur.get_height()
            cur.setHeightAndSize()
            cur = cur.get_parent()

        # rotation itself#
        rotateCNT = 0
        if is_insert:
            tmp = node.get_parent()
        else:
            tmp = node

        while tmp != None:
            tmp.setHeightAndSize()

            if abs(tmp.BFF()) < 2:
                if tmp.Oldheight != tmp.get_height():
                    rotateCNT += 1
                if tmp.Oldheight == tmp.get_height() and is_insert == True:
                    break
                tmp = tmp.get_parent()
                continue

            par = tmp.get_parent()
            tmpBF = tmp.BFF()
            if tmpBF == 2:
                leftBF = tmp.get_left().BFF()
                if leftBF == -1:
                    self.leftright_rotation(tmp)
                    rotateCNT += 2
                else:
                    self.right_rotation(tmp)
                    rotateCNT += 1
                tmp = par

            else:  # tmpBF== -2
                rightBF = tmp.get_right().BFF()
                if rightBF == 1:
                    self.rightleft_rotation(tmp)
                    rotateCNT += 2
                else:
                    self.left_rotation(tmp)
                    rotateCNT += 1
                tmp = par

        # update root#
        tmp2 = node
        while tmp2 != None:
            tmp2.setHeightAndSize()
            self.root = tmp2
            tmp2 = tmp2.parent
        self.update_root()
        return rotateCNT



    """rotates left

    	@param node: a pointer to the node that we want to rotate by
    	@returns: the parent of the right node
    	complexity:O(1)
    	"""

    def left_rotation(self, node):
        right = node.get_right()
        node.set_right(right.get_left())
        node.get_right().set_parent(node)
        right.set_left(node)
        right.set_parent(node.get_parent())
        node.set_parent(right)
        if right.get_parent() is not None:
            if right.get_parent().get_left() == node:
                right.get_parent().set_left(right)
            else:
                right.get_parent().set_right(right)
        node.setHeightAndSize()
        right.setHeightAndSize()
        if right.get_parent() != None:
            return right.get_parent()

    """rotates right then left

    	@param node: a pointer to the node that we want to rotate by
    	complexity:O(1)
    	"""

    def rightleft_rotation(self, node):
        node = self.right_rotation(node.get_right())
        node2 = self.left_rotation(node)

    """rotates left then right

    	@param node: a pointer to the node that we want to rotate by
    	complexity:O(1)
    	"""

    def leftright_rotation(self, node):
        node = self.left_rotation(node.get_left())
        node2 = self.right_rotation(node)

    """rotates right

    	@param node: a pointer to the node that we want to rotate by
    	@returns: the parent of the left node
    	complexity:O(1)
    	"""

    def right_rotation(self, node):
        left = node.get_left()
        node.set_left(left.get_right())
        node.get_left().set_parent(node)
        left.set_right(node)
        left.set_parent(node.get_parent())
        node.set_parent(left)
        if left.get_parent() is not None:
            if left.get_parent().get_right() == node:
                left.get_parent().set_right(left)
            else:
                left.get_parent().set_left(left)
        node.setHeightAndSize()
        left.setHeightAndSize()
        if left.get_parent() != None:
            return left.get_parent()