from janome.tokenizer import Tokenizer
from tokenizer_wrapper import *

// https://qiita.com/polikeiji/items/2f6dc4618f5c8ab8a5a5
class janome_tokenizer_wrapper(st_tokenizer):
    def __init__(self):
        self.t=Tokenizer()

    def tokenize(self,text):
        return [st_token(t.surface,t.base_form,t.part_of_speech[0],t) for t in self.t.tokenize(text)]   

if __name__ == "__main__":
    jtw=janome_tokenizer_wrapper()
    result=jtw.tokenize("すもももももももものうち")
    print(result[0].lemma)