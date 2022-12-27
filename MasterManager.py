class Answer:
    A = None
    B = None
    C = None
    D = None
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    
    def fnGetAAnswer(self):
        return self.A

    def fnGetBAnswer(self):
        return self.B

    def fnGetCAnswer(self):
        return self.C

    def fnGetDAnswer(self):
        return self.D

class Question:
    sQuestion = None
    aAnswer = None
    sCorrectAnswer = None

    def __init__(self, sQuestion, sCorrectAnswer, aAnswer: Answer = None):
        self.sQuestion = sQuestion
        self.sCorrectAnswer = sCorrectAnswer
        self.aAnswer = aAnswer

    def fnGetQuestion(self):
        return self.sQuestion
    
    def fnGetCorrectAnswer(self):
        return self.sCorrectAnswer

    def fnGetListAnswer(self):
        return self.aAnswer

class MasterManager:
    aListQuestion = []

    def __init__(self):
        oTempQuestion = Question
        
        self.aListQuestion.append(Question("Thủ đô Việt Nam nằm ở đâu?", "C", Answer("Hồ Chí Minh", "Đồng Tháp", "Hà Nội", "Huế")))
        self.aListQuestion.append(Question("Đâu là vựa lúa lớn nhất của Việt Nam?", "A", Answer("An Giang", "Thái Bình", "Hà Nội", "Hà Tĩnh")))
        self.aListQuestion.append(Question("'Bình Tây đại nguyên soái' là danh xưng của vị nào trong lịch sử Việt Nam?", "C", Answer("Hồ Nguyên Trừng", "Phan Bội Châu", "Trương Định", "Hoàng Hoa Thám")))
        self.aListQuestion.append(Question("Ai là người nói câu sau đây:\n - Đầu thần chưa rơi xuống đất, xin bệ hạ cứ yên lòng.", "D", Answer("Lý Công Uẩn", "Trần Thủ Độ", "Lý Bí", "Lý Thường Kiệt")))

    def fnGetQuestion(self, iQuestionNumber: int = 0):
        return self.aListQuestion[iQuestionNumber]

    def fnGetQuestionLength(self):
        return len(self.aListQuestion)