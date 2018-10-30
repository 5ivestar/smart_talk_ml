class st_tokenizer:
    def tokenize(self,text):
        return []

class st_token:
    def __init__(self,surface,lemma,token_type,token_obj):
        self.surface=surface
        self.lemma=lemma
        self.token_type=token_type
        self.token_obj=token_obj

