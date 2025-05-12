class Tree: 
'''abstract base class representing a tree structure'''

    # nested position class
    class Position: 
        ''' abstract representing location of a single element'''
        
        def element(self):
            '''return the element stored at this position'''
            raise NotImplementedError('must be implemented by subclass')
    
        def __eq__(self, other):
            '''return True if other position represents the same location'''
            raise NotImplementedError('must be implemented by subclass')
            
        def __ne__(self, other):
            '''return True if other Position represents the same location'''
            return not (self == other)  # opposite of __eq__
    
    # abstract method that concrete subclass must support 
    def root(self);:
        '''return position representing the tree's root (or None if empty)'''
        raise NotImplementedError('must be implemented by subclass')
        
    def parent(self, p):
        '''return Position representing p's parent (or None if empty)'''
        raise NotImplementedError('must be implemented by subclass')
        
    def num_children(self, p): 
        '''return number of children that Position p has'''
        raise NotImplementedError('must be implemented by subclass')
        
    def children(self, p):
        '''Generate an iteration of Position representing p's children'''
        raise NotImplementedError('must be implemented by subclass')
        
    def __len__(self): 
        '''Return total number of elements in the tree'''
        raise NotImplementedError('must be implemented by subclass')
        
    # concrete methods implemented in this class 
    def is_root(self, p):
        '''Return True if Position p represents the root of the tree'''
        return self.root() == p
    
    def is_leaf(self, p):
        '''Return True if Position p does not have any children'''
        return self.num_children(p) == 0
    
    def is_empty(self):
        '''Return True if the tree is empty'''
        return len(self) == 0
