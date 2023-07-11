import spacy




def find_root_subject_de(sentence):

    nlp = spacy.load("de_core_news_sm")
    doc = nlp(sentence)
    tkn = []
    tkn_dp = []
    for token in doc: 
        tkn.append(token.text)
        tkn_dp.append(token.dep_)
    result = [tkn, tkn_dp]
    return result
    return tkn_dp

def get_root(sentence):

   nlp = spacy.load("en_core_web_sm")

   doc = nlp(sentence)

   tkn = []
   tkn_dp = []

   for token in doc:
       tkn.append(token.text)
       tkn_dp.append(token.dep_)
   result = [tkn, tkn_dp]
   return result

  
      


    

def find_root_de(paragraph):

    sentences = [find_root_subject_de(sentence) for sentence in paragraph]

    return sentences

def lowercase_strings(strings):

    lowercased_strings = [find_root_subject(string) for string in strings]

    return capitalize_first_letter(lowercased_strings)


def capitalize_first_letter(strings):
    capitalized_strings = [string.capitalize() for string in strings]
    return capitalized_strings

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("this is a cat")
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    result = []
    for token in doc:
        result.append(token.text)
    return result
    return entities




def find_root_subject(sentence):

   nlp = spacy.load("en_core_web_sm")

   doc = nlp(sentence)

   root = None

   for token in doc:
       if token.dep_ == "ROOT":
           root = token
           break

   if root is not None:
       subject = find_subject(root)
       acomp_object = find_acomp_or_object(root)
       if subject is not None:
           subject_text = subject.text
       else:
           subject_text = "-"


       root_text = root.text


       if acomp_object is not None:
           acomp_object_text = acomp_object.text
       else:
           acomp_object_text = "-"


       result = f"{subject_text} {root_text} {acomp_object_text}"
       print(result)
       return result
   else:
       msg = "No root found in the sentence"
       print(msg)
       return msg


   if root is not None:
       subject = find_subject(root)
       acomp_object = find_acomp_or_object(root)
       if subject is not None:
           print(f"Subject of root ({root.text}): {subject.text}")
       else:
           print(f"No subject found for root ({root.text})")


       if acomp_object is not None:
           print(f"Acomp or object of root ({root.text}): {acomp_object.text}")
       else:
           print(f"No acomp or object found for root ({root.text})")
   else:
       print("No root found in the sentence")


       



def find_subject(token):
   for child in token.children:
       if child.dep_ == "nsubj":
           return child
   return None


def find_object(token):
   for child in token.children:
       if child.dep_ == "dobj" or child.dep_ == "attr":
           return child
   return None


def find_acomp_or_object(token):


   for child in token.children:
       if child.dep_ == "acomp" or child.dep_ == "dobj" or child.dep_ == "attr":
           return child
   return None



