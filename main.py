from trie import Trie

def main ():
    test_cases_trie()

def test_cases_trie():
    trie = Trie(root = True)
    text = open("texts//texto.txt","r").read()
    
    import time
    inicio = time.time()
    #region create trie
    trie.insert_text(text)
    #endregion
    print("\nTarda " +str(time.time()-inicio)+" para crear un trie de "+str(len(text))+" letras.") 


    trie.insert_text(text,'test')

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

main()        