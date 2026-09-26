from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QTextEdit, QInputDialog
import json


'''notes = {
    'Добро пожаловать!' : {
        'текст' : 'Это самое лучшее приложение для заметок в мире',
        'теги' : []
    }
}

with open("notes_data.json", "w", encoding='utf-8') as file:
    json.dump(notes, file, ensure_ascii=False)
'''

def show_note():
    name = notes_list.selectedItems()[0].text()
    for x in notes:
        if name == x[0]:
            text_editor.setText(x[1])
            tags_list.clear()
            tags_list.addItems(x[2])
            break

def add_note():
    note_name, ok = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        note = list()
        note = [note_name, '', ['тестовыйтег']]
        notes.append(note)
        notes_list.addItem(note[0])
        filename = str(len(notes) - 1) + '.txt'
        with open (filename, 'w', encoding='utf-8') as file:
            for x in note[:-1]:
                file.write(x + '\n')
            file.write(note[2][0])
        


def sv_note():
    if notes_list.selectedItems():
        new_note = notes_list.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == new_note:
                note[1] = text_editor.toPlainText()
                filename = str(i) + '.txt'
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(note[0] + '\n')
                    file.write(note[1] + '\n')
                    for tag in note[2]:
                        file.write(tag + ' ')
                    file.write('\n')
            i += 1

def del_note():
    pass

def add_tag():
    pass

def del_tag():
    pass

def srch_tag():
    pass

app = QApplication([])
main_win = QWidget()
main_win.resize(800, 600)
main_win.setWindowTitle("Умные заметки")

text_editor = QTextEdit()
text1 = QLabel('Список замечаний')
notes_list = QListWidget()
make_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
text2 = QLabel('Список тегов')
tags_list = QListWidget()
new_tag_line = QLineEdit()
connect_to_note = QPushButton('Добавить к заметке')
disconnect_from_note = QPushButton('Открепить от заметки')
search_tag = QPushButton('Искать заметку по тегу')
new_tag_line.setPlaceholderText('Введите тег')

main_h_line = QHBoxLayout()
main_v_line1 = QVBoxLayout()
main_v_line2 = QVBoxLayout()

main_h_line.addLayout(main_v_line1)
main_h_line.addLayout(main_v_line2)

main_v_line1.addWidget(text_editor)
main_v_line2.addWidget(text1)
main_v_line2.addWidget(notes_list)

h_line1 = QHBoxLayout()
main_v_line2.addLayout(h_line1)

h_line1.addWidget(make_note)
h_line1.addWidget(delete_note)
main_v_line2.addWidget(save_note)
main_v_line2.addWidget(text2)
main_v_line2.addWidget(tags_list)
main_v_line2.addWidget(new_tag_line)

h_line2 = QHBoxLayout()
main_v_line2.addLayout(h_line2)

h_line2.addWidget(connect_to_note)
h_line2.addWidget(disconnect_from_note)
main_v_line2.addWidget(search_tag)

main_win.setLayout(main_h_line)

notes_list.itemClicked.connect(show_note)
make_note.clicked.connect(add_note)
save_note.clicked.connect(sv_note)
delete_note.clicked.connect(del_note)
connect_to_note.clicked.connect(add_tag)
disconnect_from_note.clicked.connect(del_tag)
search_tag.clicked.connect(srch_tag)

name = 0
notes = []
while True:
    filename = str(name) + '.txt'
    note = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for x in file:
                x = x.replace('\n', '')
                note.append(x)
            try:
                note[2] = note[2].split()
            except:
                pass
        notes.append(note)
        name += 1
    except IOError:
        break        

print(notes)
for x in notes:
    notes_list.addItem(x[0])

main_win.show()
app.exec_()
