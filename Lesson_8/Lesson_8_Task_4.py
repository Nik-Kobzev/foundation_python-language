class Tex:
    def __init__(self):
        self.tex = {}
        self.i = 0

    def texn(self, tex):
        self.i += 1
        self.tex.setdefault(self.i, tex)


e = Tex()
e.texn('cnjk')
e.texn('fgd')
print(e.tex)
