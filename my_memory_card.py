#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QButtonGroup,QWidget,QRadioButton, QLabel,QVBoxLayout,QGroupBox,QHBoxLayout
from random import shuffle 
from random import randint
class Question():
    def __init__(self, qst, right_answer, wrong1, wrong2, wrong3):
        self.qst = qst
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

main_win = QWidget()

main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)


main_layout = QVBoxLayout()
question = QLabel('Вопрос')
btn_OK = QPushButton('Ответить')

ansBox = QGroupBox('Варианты ответов')
btn1 = QRadioButton('ans1')
btn2 = QRadioButton('ans2')
btn3 = QRadioButton('ans3')
btn4 = QRadioButton('ans4')

layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout2.addWidget(btn1)
layout2.addWidget(btn2)
layout3.addWidget(btn3)
layout3.addWidget(btn4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
ansBox.setLayout(layout1)

resBox = QGroupBox('Результаты теста')
layout = QVBoxLayout()
result = QLabel('Правильно/Неправильно')
right_ans = QLabel('Правильный ответ')
layout.addWidget(result)
layout.addWidget(right_ans, alignment = Qt.AlignCenter)
resBox.setLayout(layout)


layout_box = QVBoxLayout()
layout_box.addWidget(ansBox)
layout_box.addWidget(resBox)
resBox.hide()


main_layout.addWidget(question,alignment = Qt.AlignCenter)
main_layout.addLayout(layout_box)
main_layout.addWidget(btn_OK, alignment = Qt.AlignCenter)





main_win.setLayout(main_layout)
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)




def show_result():
    ansBox.hide()
    resBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ansBox.show()
    resBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(start_test)

answer = [btn1,btn2,btn3,btn4]
def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    right_ans.setText(q.right_answer)
    question.setText(q.qst)
    show_question()
q = Question('Вопрос?','ответ1', 'ответ2', 'ответ3', 'ответ4')
ask(q)
def check_answer():
    if answer[0].isChecked():
        show_correct('Верно')
        main_win.score += 1
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неверно')
   
    
    

question_list = []
question_list.append(Question('Вопрос ?', 'Ответ1',"Ответ2","Ответ3","Ответ99"))
question_list.append(Question('Вопрос1 ?', 'Ответ565',"Ответ4","Ответ5", "Ответ1221"))
question_list.append(Question('Вопрос2 ?', 'Ответ81',"Ответ9","Ответ7", "Ответ231"))

def next_question():
  
   # main_win.cur_question += 1
   cur_question = randint(0, len(question_list)-1)
   q = question_list[cur_question]
   main_win.total += 1
   print('Текущий вопрос', main_win.total)
   pts = main_win.score / main_win.total * 100
   print('Текущий вопрос', pts)
   ask(q)

   

    #if main_win.cur_question == len(question_list):
    #    main_win.cur_question = 0
    #q = question_list[main_win.cur_question]
    
#main_win.cur_question = -1

def show_correct(res):
    result.setText(res)
    show_result()
main_win.score = -1
main_win.total = 0
btn_OK.clicked.connect(check_answer)

main_win.show()
app.exec_()