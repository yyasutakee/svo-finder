import tkinter as tk

import spacy



class SVO:

    def create_array(self, text):

        sentences = text.split('.')

        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        return sentences
    
    def find_root_verb(self, sentence):

        nlp = spacy.load("en_core_web_sm")

        doc = nlp(sentence)

        root = ""

        for token in doc:
            if token.dep_ == "ROOT":
                root = token.text
                #  return root
                break

        return root

    def find_root_subject_de(self, sentence):

        nlp = spacy.load("de_core_news_sm")
        doc = nlp(sentence)
        tkn = []
        tkn_dp = []
        for token in doc: 
            tkn.append(token.text)
            tkn_dp.append(token.dep_)
        result = [tkn, tkn_dp]
        return result

    def get_root(self, sentence):

        nlp = spacy.load("en_core_web_sm")

        doc = nlp(sentence)

        tkn = []
        tkn_dp = []

        for token in doc:
            tkn.append(token.text)
            tkn_dp.append(token.dep_)
        result = [tkn, tkn_dp]
        return result

    def find_root_de(self, paragraph):

        sentences = [self.find_root_subject_de(sentence) for sentence in paragraph]

        return sentences

    def extract_entities(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp("this is a cat")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        result = []
        for token in doc:
            result.append(token.text)
        return result
        return entities

    def find_subject(self, token):
        for child in token.children:
            if child.dep_ == "nsubj":
                return child
        return None

    def find_object(self, token):
        for child in token.children:
            if child.dep_ == "dobj" or child.dep_ == "attr":
                return child
        return None

    def find_acomp_or_object(self, token):


        for child in token.children:
            if child.dep_ == "acomp" or child.dep_ == "dobj" or child.dep_ == "attr":
                return child
        return None

    def find_root_subject(self, sentence):

        nlp = spacy.load("en_core_web_sm")

        doc = nlp(sentence)

        root = None

        for token in doc:
            if token.dep_ == "ROOT":
                root = token
                break

        if root is not None:
            subject = self.find_subject(root)
            acomp_object = self.find_acomp_or_object(root)
            if subject is not None:
                subject_text = subject.text
            else:
                subject_text = "-"


            root_text = root.text


            if acomp_object is not None:
                acomp_object_text = acomp_object.text
            else:
                acomp_object_text = "-"
            print(root_text)

            result = f"{subject_text} {root_text} {acomp_object_text}"
            print(result)
            return result
        else:
            msg = "No root found in the sentence"
            print(msg)
            return msg



    def find_v_from_a_sentence(self, sentence):

        nlp = spacy.load("en_core_web_sm")

        doc = nlp(sentence)

        root = None
        print(doc)

        i = 0

        length = 0

        # GET INDEX

        # GET LENGTH

        for token in doc:
            
            if token.dep_ == "ROOT":
                root = token

                length = len(token)
                break

            i += len(token) + 1


        
        if root is not None:
            subject = self.find_subject(root)
            acomp_object = self.find_acomp_or_object(root)
            if subject is not None:
                subject_text = subject.text
            else:
                subject_text = "-"


            root_text = root.text

            return (i, length)
            return root_text
    
        else:
            msg = "No root found in the sentence"
            print(msg)
            return ""
        
       



            

    def find_v(self, strings):

        lowercased_strings = [self.find_root_subject(string) for string in strings]

        return self.capitalize_first_letter(lowercased_strings)
    
    def capitalize_first_letter(self, strings):
        capitalized_strings = [string.capitalize() for string in strings]
        return capitalized_strings
    


import tkinter as tk

def on_button_click():
    entered_text = entry.get()
    print("Text entered:", entered_text)


    s = SVO()

    sentences = s.create_array(entered_text)




s = SVO()

v = s.find_v_from_a_sentence("Many users rely on private browsers to keep their Internet habits away from prying eyes. ")

# print(v)

# # Create the main window
# root = tk.Tk()
# root.title("Text Field Example")

# # Create a text field
# entry = tk.Entry(root, width=30)
# entry.pack(pady=10)

# # Create a button
# button = tk.Button(root, text="Get Text", command=on_button_click)

# button.pack()

# Start the Tkinter event loop
# root.mainloop()



# def start_tkinter(self):
import tkinter as tk

def change_text_color():
    # Change the color of the word "michael" to blue

    text_from_widget1 = text_widget1.get("1.0", tk.END)


    s = SVO()

    v = s.find_v_from_a_sentence(text_from_widget1)

 
    start_index = v[0]


    length = v[1]

    start_index = f"1.{start_index}"

    # start_index = float(start_index)

 
 
    # end_index = v[0] + v[1]

    # end_index = f"1.{length}"

    # end_index = float(end_index)

    end_index = start_index + "+" + f"{length}c"
  #  start_index = text_widget1.search("my", "1.0", tk.END, count=tk.END)
    # end_index = f"{start_index}+{length}c"


    print(f"start index {start_index}")

    print(f"edn index {end_index}")




    text_widget1.tag_configure("blue_tag", foreground="blue")
    text_widget1.tag_add("blue_tag", start_index, end_index)

root = tk.Tk()

root.title("Text Color Example")

text_widget1 = tk.Text(root, height=5, width=40)

text_widget1.pack(padx=10, pady=10)

text_widget1.insert(tk.END, "hello my name is michael Jordan")

text_widget2 = tk.Text(root, height=5, width=40)

text_widget2.pack(pady=10)

text_widget2.insert(tk.END, "This is another Text widget.")

button = tk.Button(root, text="Change Text Color", command=change_text_color)

button.pack(pady=5)

root.mainloop()
