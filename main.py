from retrieval_trie import RetrievalTrie
from trie import Trie
from parser_text import remove_punctuation

def main ():
    test_cases_retrieval_trie()

def test_cases_trie():
    trie = Trie(root = True)
    text = remove_punctuation(open("texts//text1.txt","r").read().lower())
    
    import time
    inicio = time.time()
    #region create trie
    trie.insert_text(text,'text1')
    #endregion
    print("\nTarda " +str(time.time()-inicio)+" para crear un trie de "+str(len(text))+" letras.") 

    text = remove_punctuation(open("texts//text2.txt","r").read().lower())
    trie.insert_text(text,'text2')

    text = remove_punctuation(open("texts//text3.txt","r").read().lower())
    trie.insert_text(text,'text3')

    while (True):
        print ("\nEntre la palabra que desea tener informacion")
        word = input()
        print ("\nEntre el id del documento del cual desea conocer informacion respecto a la palabra anterior")
        doc = input()

        print(word + " como prefijo aparece: " + str(trie.prefix_count_in_document(word,doc)))
        print(word + " como palabra aparece: " + str(trie.word_count_in_document(word,doc)))
        print(word + " aparece como prefijo en las posiciones: " + str(trie.prefix_position_in_document(word,doc)))
        print(word + " aparece como palabra en las posiciones: " + str(trie.word_position_in_document(word,doc)))
        print(word + " aparece en los documentos: "+str(str(trie.documents_of_word(word))))
        print("\n")

def test_cases_retrieval_trie():
    trie = RetrievalTrie(root = True)
    text = remove_punctuation(open("texts//text1.txt","r").read().lower())
    
    import time
    inicio = time.time()
    #region create trie
    trie.insert_text(text,'text1')
    #endregion
    print("\nTarda " +str(time.time()-inicio)+" para crear un trie de "+str(len(text))+" letras.") 

    text = remove_punctuation(open("texts//text2.txt","r").read().lower())
    trie.insert_text(text,'text2')

    text = remove_punctuation(open("texts//text3.txt","r").read().lower())
    trie.insert_text(text,'text3')
    
    text = open("texts//text4.txt","r").read()
    trie.insert_text(text,'text4')

    while (True):
        print ("\nEntre un documento para saber su fercuencia maxima")
        doc = input()

        print(" \nLa frecuencia maxima en el documento  " + doc +" es "+str(str(trie.max_count_in_document[doc])))

main()        