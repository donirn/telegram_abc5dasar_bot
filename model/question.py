class Question:
    def __init__(self):
        self.text = "Sebutkan nama binatang dari huruf A!"

    def getText(self):
        return self.text

    def checkAnswer(self, answer_text):
        # TODO answer shouldn't be used more than once
        animals = ['anjing','ayam','angsa','anggora','anis','alap-alap','anoa','anjing laut']
        return answer_text in animals