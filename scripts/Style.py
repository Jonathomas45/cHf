import re
exempt = [
    "sliced", "diced", 'peeled', 'cored', 'melted', "thawed", 
    "quartered", "lightly", "beaten","chopped"
    ]


#ennumerating ingredients & nutrition
class Cleanup():

    def indent(header, string):
        """
            Uses the string of a header and styles it to be indented for every next item.
        """
        pattern = r",\s*(?=(" + "|".join(re.escape(word) for word in exempt) + r"))"
        cleaned = re.sub(pattern, " ", string)
        final = re.sub(r",\s*", "\n\t", cleaned)
        hl = header.capitalize()
        print(f"{hl}: \n\t{final}")





        

# 



