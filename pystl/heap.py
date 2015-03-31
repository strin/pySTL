import random
import pdb

class HeapNode:
    def __init__(me, data, father):
        me.deleted = False
        me.father = father
        me.left = None
        me.right = None
        me.data = data

    def is_leaf(me):
        return me.left == None and me.right == None

    def is_root(me):
        return me.father == None

    def swap(me):
        "swap node with the node's father"
        if me.is_root():
            return False
        father = me.father
        grandpa = me.father.father
        if me == father.left:
            left = father
            right = father.right
        else:
            left = father.left
            right = father
        father.left = me.left
        if me.left != None:
            me.left.father = father
        father.right = me.right
        if me.right != None:
            me.right.father = father
        me.left = left
        if left != None:
            left.father = me
        me.right = right
        if right != None:
            right.father = me
        me.father = grandpa
        if grandpa != None and father == grandpa.left:
            grandpa.left = me
        if grandpa != None and father == grandpa.right:
            grandpa.right = me
        return True

    def find_root(me):
        node = me
        while node.father != None:
            node = node.father
        return node

    def remove_leaf(me):
        assert(me.is_leaf())
        if me == me.father.left:
            me.father.left = None
        if me == me.father.right:
            me.father.right = None

    def __strs__(me):
        res = []
        if me.is_root():
            res += ['root ' + str(me.data)]
        else:
            res += ['node ' + str(me.data)]
        nodes = []
        if me.left != None:
            nodes += [me.left]
        if me.right != None:
            nodes += [me.right]
        for node in nodes:
            res += ['\t'+line for line in node.__strs__()]
        return res

    def __str__(me):
        return '\n'.join(me.__strs__())

class Heap:
    def __init__(me, key = lambda x : x):
        me.root = None
        me.key = lambda node : key(node.data) if node.deleted == False \
                                              else float('inf')

    def insert(me, data):
        if me.root == None:
            me.root = HeapNode(data, father=None)
            return me.root
        else:
            new_node = HeapNode(data, father=None)
            me.insert_random_leaf(me.root, new_node)
            me.update(new_node)
            return new_node

    def top(me):
        if me.root == None:
            raise Exception('Heap is empty.')
        return me.root.data

    def is_empty(me):
        return me.root == None

    def remove(me):
        node = me.root
        node.deleted = True
        me.update(node)
        if node == me.root:
            me.root = None
        else:
            node.remove_leaf()

    def update(me, node):
        if not node.is_root() and me.key(node) < me.key(node.father):
            if node.father == me.root:
                me.root = node
            node.swap()
            me.update(node)
        else:
            nodes = []
            if node.left != None and me.key(node.left) < me.key(node):
                nodes += [node.left]
            if node.right != None and me.key(node.right) < me.key(node):
                nodes += [node.right]
            if len(nodes) == 1:
                nodes[0].swap()
            elif len(nodes) == 2:
                min(nodes, key = lambda node : me.key(node)).swap()
            if len(nodes) > 0:
                if me.root == node:
                    me.root = node.father
                me.update(node)

    def insert_random_leaf(me, node, new_node):
        assert(isinstance(node, HeapNode))
        if node.left == None:
            node.left = new_node
            new_node.father = node
        elif node.right == None:
            node.right = new_node
            new_node.father = node
        else:
            coin = random.randint(0, 1)
            if coin == 0:
                me.insert_random_leaf(node.left, new_node)
            else:
                me.insert_random_leaf(node.right, new_node)

    def __str__(me):
        return str(me.root)


if __name__ == "__main__":
    heap = Heap()
    # for i in range(100):
    #     heap.insert(random.randint(0, 100))
    # for i in range(50):
    #     heap.remove()
    # heap.insert(3)
    # heap.insert(1)
    # heap.insert(2)
    # heap.remove()
    # node = heap.root
    # node.data = 1
    # heap.update(node)
    print heap
