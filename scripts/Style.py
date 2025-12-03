import re
exempt = [
    "sliced", "diced", 'peeled', 'cored', 'melted', "thawed", 
    "quartered", "lightly", "beaten", "chopped", "drained", "divided", "thinly"
    ]


#ennumerating ingredients & nutrition
class Cleanup:

    def indent(header, string):
        """
            Uses the string of a header and styles it to be indented for every next item.
        """
        hl = header.capitalize()
        if header == 'directions':
            st = string.replace("\n", '').split('.')
            print(f"{hl}:")
            for s in st:
                print(f'\t Step {st.index(s)+1}. {s}.')
        else:
            pattern = r",\s*(?=(" + "|".join(re.escape(word) for word in exempt) + r"))"
            cleaned = re.sub(pattern, " ", string)
            final = re.sub(r",\s*", "\n\t", cleaned)
            print(f"{hl}: \n\t{final}")





        





