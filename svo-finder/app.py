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

            

    def find_v(self, strings):

        lowercased_strings = [self.find_root_subject(string) for string in strings]

        return self.capitalize_first_letter(lowercased_strings)
    
    def capitalize_first_letter(self, strings):
        capitalized_strings = [string.capitalize() for string in strings]
        return capitalized_strings
    

s = SVO()

array = s.create_array("There is nothing quite so helpful and satisfying as a well-described public API. The java- docs for the standard Java library are a case in point. It would be difficult, at best, to write Java programs without them. If you are writing a public API, then you should certainly write good javadocs for it. But keep in mind the rest of the advice in this chapter. Javadocs can be just as misleading, nonlocal, and dishonest as any other kind of comment.")

# s.find_v(array)


sentences = ["Nowadays, most good IDEs provide special gestures and features to locate all the TODO comments, so it’s not likely that they will get lost.", 
                        "Still, you don’t want your code to be littered with TODOs. So scan through them regularly and eliminate the ones you can.", 
                        "A comment may be used to amplify the importance of something that may otherwise seem inconsequential."]

# find_v(sentences)

# def get_text_content():
#     content = text_widget.get("1.0", tk.END)  # Retrieve text from the Text widget
#     cleaned_text = content.replace('\n', '').replace('\r', '').strip()

#     print(cleaned_text)

# def set_text_content():
#     new_content = "New text content."
#     text_widget.delete("1.0", tk.END)  # Clear existing content
#     text_widget.insert(tk.END, new_content)  # Set new content

# # Function for the "Custom Action" button
# def custom_action():
#     # Add your custom action here
#     print("Custom action executed.")

# root = tk.Tk()
# root.title("")

#     # Create a Text widget
# text_widget = tk.Text(root, height=10, width=40, wrap=tk.WORD)
# text_widget.pack(padx=10, pady=10)

#     # Create buttons to interact with the Text widget
# get_button = tk.Button(root, text="Get Text", command=get_text_content)
# get_button.pack(pady=5)

# set_button = tk.Button(root, text="Set Text", command=set_text_content)
# set_button.pack(pady=5)

#     # Create a button for a custom action
# custom_button = tk.Button(root, text="Custom Action", command=custom_action)
# custom_button.pack(pady=5)

#     # Run the Tkinter event loop
# root.mainloop()
# 

# def start_tkinter(self):
import tkinter as tk

def change_text_color():
    # Change the color of the word "michael" to blue
    start_index = text_widget1.search("michael", "1.0", tk.END, count=tk.END)
    end_index = f"{start_index}+7c"
    text_widget1.tag_configure("blue_tag", foreground="blue")
    text_widget1.tag_add("blue_tag", start_index, end_index)

# Create the main window
root = tk.Tk()
root.title("Text Color Example")

# Create the first Text widget with initial text
text_widget1 = tk.Text(root, height=5, width=40)
text_widget1.pack(padx=10, pady=10)
text_widget1.insert(tk.END, "hello my name is michael Jordan")

# Create the second Text widget with initial text
text_widget2 = tk.Text(root, height=5, width=40)
text_widget2.pack(pady=10)
text_widget2.insert(tk.END, "This is another Text widget.")

# Create a button to change text color for the first Text widget
button = tk.Button(root, text="Change Text Color", command=change_text_color)
button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

# GET TEXT
# SHOW BELOW
# I NEED GET INDEX AND LENGTH OF VERB
