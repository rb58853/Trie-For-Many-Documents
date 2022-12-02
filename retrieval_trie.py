from trie import Trie
class RetrievalTrie(Trie):
    def __init__(self, value="^", root=False, document_id='default', parent = None):
        super().__init__(value, root, document_id)
        
        self.max_count_in_document = {}

        if root == True:
            self.root = self
        else:
            self.root = parent.root

    def new_max_count(self, document, new_max):
        try:
            max_count = self.root.max_count_in_document[document]
            self.root.max_count_in_document[document] = max(max_count,new_max)
        except:
            self.root.max_count_in_document[document] = 1
    
    def insert_char_in_children(self,char,word,pos,document_id):
        try : 
            node = self.childs[char]
            if len(word) == 1:
                try: node.count_as_word_in_document[document_id]+=1
                except: node.count_as_word_in_document[document_id]=1
            
                try:node.position_in_document_as_word[document_id].append(pos)
                except:node.position_in_document_as_word[document_id]=[pos]
                
                # Max Frec In Document
                self.new_max_count(document_id,node.count_as_word_in_document[document_id])
            
            try: node.count_as_prefix_in_document[document_id]+=1
            except: node.count_as_prefix_in_document[document_id]=1
            
            try:node.position_in_document[document_id].append(pos)
            except:node.position_in_document[document_id]=[pos]
            
            if node.documents.__contains__(document_id) == False:  node.documents.append(document_id)
            
            self.childs[char] = node
            self.childs[char].insert_word(word[1:],pos,document_id) #rec

        except:
            node = Trie(char,False,document_id)
            if len(word) == 1:
                node.count_as_word_in_document[document_id] = 1
                node.position_in_document_as_word[document_id] = [pos]   
                
                # Max Frec In Document
                self.new_max_count(document_id,node.count_as_word_in_document[document_id])
             
            node.count_as_prefix_in_document[document_id] = 1
            node.position_in_document[document_id] = [pos]    
            
            self.childs[char] = node
            self.childs[char].insert_word(word[1:],pos,document_id) #rec
            
