

class English:
    """English translator"""

    def translate(self,msg):
        return msg

class Chinese:

    def __init__(self):
        self.data = {'cat':'猫','dog':'狗'}

    def translate(self,msg):
        return self.data.get(msg,msg)



def load(language):
    data = {'English':English,'Chinese':Chinese}
    assert language in data
    return data[language]


c,e = load('Chinese')(),load('English')()
for v in 'cat dog fish'.split(' '):
    print(c.translate(v),e.translate(v))