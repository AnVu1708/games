import time
import turtle
import tkinter
# Custom class
import Layout
import MasterManager

oMasterManager = MasterManager.MasterManager()

# Question define
sAnswerValue = None
oCurrentQuestion : MasterManager.Question = None
iMaxQuestionNumber = oMasterManager.fnGetQuestionLength()
iCurrentQuestionNumber = 0
iScore = 0

# Screen define
mainWindow_width = 800
mainWindow_height = 500

# Setup window
mainWindow = turtle.Screen()
mainWindow.setup(mainWindow_width, mainWindow_height)
canvas = turtle.getcanvas()
parent = canvas.master

# Setup layout
questionBox = Layout.TextBox(-390, 240, 540, 230)
scoreBox = Layout.TextBox(160, 240, 220, 230)

questionText = tkinter.Text(parent, width=48, height=9, state="disabled", font=("Black", 15), wrap="word")
canvas.create_window((-120, -130), window=questionText)

scoreText = tkinter.Text(parent, width=13, height=6, state="disabled", font=("Black", 20), wrap="word")
scoreText.tag_configure("center", justify="center")
scoreText.tag_add("center", 1.0, "end")
canvas.create_window((270, -130), window=scoreText)

answerButton1 = tkinter.Button(parent, width=50, height=6, text='A. ', command=lambda sValue="A": fnButtonPress(sValue), anchor="w")
canvas.create_window((-200, 50), window=answerButton1)

answerButton2 = tkinter.Button(parent, width=50, height=6, text='B. ', command=lambda sValue="B": fnButtonPress(sValue), anchor="w")
canvas.create_window((190, 50), window=answerButton2)

answerButton3 = tkinter.Button(parent, width=50, height=6, text='C. ', command=lambda sValue="C": fnButtonPress(sValue), anchor="w")
canvas.create_window((-200, 175), window=answerButton3)

answerButton4 = tkinter.Button(parent, width=50, height=6, text='D. ', command=lambda sValue="D": fnButtonPress(sValue), anchor="w")
canvas.create_window((190, 175), window=answerButton4)

# Event press button answer
def fnButtonPress(sValue):
    global sAnswerValue

    sAnswerValue = sValue
    fnCheckAnswer()

# Generate question data
def fnGenerateQuestion(iQuestionNumber: int):
    global answerButton1
    global answerButton2
    global answerButton3
    global answerButton4
    global iCurrentQuestionNumber
    global oCurrentQuestion

    oCurrentQuestion = oMasterManager.fnGetQuestion(iQuestionNumber)
    iCurrentQuestionNumber = iQuestionNumber

    questionText.config(state="normal")
    questionText.delete(1.0, tkinter.END)
    questionText.insert(tkinter.END, oCurrentQuestion.fnGetQuestion())
    questionText.config(state="disabled")
    answerButton1.config(text="A. " + oCurrentQuestion.fnGetListAnswer().fnGetAAnswer())
    answerButton2.config(text="B. " + oCurrentQuestion.fnGetListAnswer().fnGetBAnswer())
    answerButton3.config(text="C. " + oCurrentQuestion.fnGetListAnswer().fnGetCAnswer())
    answerButton4.config(text="D. " + oCurrentQuestion.fnGetListAnswer().fnGetDAnswer())

# Check correct answer
def fnCheckAnswer():
    global sAnswerValue
    global iCurrentQuestionNumber
    global oCurrentQuestion
    global iScore
    
    if sAnswerValue == oCurrentQuestion.fnGetCorrectAnswer():
        iScore = iScore + 1
        scoreText.config(state="normal")
        scoreText.delete(1.0, tkinter.END)
        scoreText.insert(tkinter.END, str(iScore) + "\nScore", "center")
        scoreText.config(state="disabled")
    
    if iMaxQuestionNumber > (iCurrentQuestionNumber + 1):
        fnGenerateQuestion(iCurrentQuestionNumber + 1)
    else:
        answerButton1.config(state="disabled")
        answerButton2.config(state="disabled")
        answerButton3.config(state="disabled")
        answerButton4.config(state="disabled")

# Excute screen
questionBox.drawTextBox()
scoreBox.drawTextBox()
mainWindow.listen()
fnGenerateQuestion(0)

while True:
    mainWindow.update()