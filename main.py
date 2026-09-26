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
    text_editor.setText(notes[name]['текст'])
    tags_list.clear()
    tags_list.addItems(notes[name]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {"текст" : "", "теги" : []}
        notes_list.addItem(note_name)

def sv_note():
    if notes_list.selectedItems():
        note_text = text_editor.toPlainText()
        new_note = notes_list.selectedItems()[0].text()
        notes[new_note]["текст"] = note_text
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)

def del_note():
    if notes_list.selectedItems():
        text_editor.clear()
        tags_list.clear()
        note_name = notes_list.selectedItems()[0].text()
        del notes[note_name]
        notes_list.clear()
        notes_list.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)

def add_tag():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = new_tag_line.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            tags_list.addItem(tag)
            new_tag_line.clear()
            with open("notes_data.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, sort_keys=True)
        else:
            print("Заметка для добавления тега не выбрана")

def del_tag():
    if tags_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        tag = tags_list.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        tags_list.clear()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True)
        tags_list.addItems(notes[key]['теги'])
    else:
        print("Тег для удаления не выбран")


def srch_tag():
    tag = new_tag_line.text()
    if search_tag.text() == "Искать заметку по тегу" and tag:
        notes_filtered = {}
        for x in notes:
            if tag in notes[x]['теги']:
                notes_filtered[x] = notes[x]
        search_tag.setText('Сбросить поиск') 
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes_filtered)
    else:
        new_tag_line.clear()
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes)
        search_tag.setText('Искать заметку по тегу')

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

with open("notes_data.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
    notes_list.addItems(notes)

notes_list.itemClicked.connect(show_note)
make_note.clicked.connect(add_note)
save_note.clicked.connect(sv_note)
delete_note.clicked.connect(del_note)
connect_to_note.clicked.connect(add_tag)
disconnect_from_note.clicked.connect(del_tag)
search_tag.clicked.connect(srch_tag)

main_win.show()
app.exec_()
