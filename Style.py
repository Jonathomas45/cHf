import re
exempt = ["sliced", "diced", 'peeled', 'cored', 'melted', "thawed"]


#ennumerating ingredients & nutrition
class Cleanup():

    def indent(header, string):
        pattern = r",\s*(?=(" + "|".join(re.escape(word) for word in exempt) + r"))"
        cleaned = re.sub(pattern, " ", string)
        final = re.sub(r",\s*", "\n\t", cleaned)
        hl = header.capitalize()
        print(f"{hl}: \n\t{final}")





        

# 



