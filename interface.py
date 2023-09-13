import tkinter as tk
import main


window = tk.Tk()
window.title('Text Analyser')
window.geometry('1920x1080')


def checkbutton_morphy():
    parts_of_speech_checkbuttom = []
    for list_parts_of_speech in for_parts_of_speech:
        if list_parts_of_speech[0] == 1:
            parts_of_speech_checkbuttom.append(list_parts_of_speech[1])
    return parts_of_speech_checkbuttom


def path_to_file():
    text_analyser = main.TextAnalyser(source_file=packs['path_to_file_entry'].get(), parts_of_speech=lambda: checkbutton_morphy())


packs = {}
# ввод пути к файлу
packs['path_to_file_lable'] = tk.Label(text='Введите имя файла:', font=("Arial", 14))
packs['path_to_file_entry'] = tk.Entry(width=30, font=1)

# выбор частей речи
for_parts_of_speech = []
packs['morphy_lable'] = tk.Label(text='Выберите части речи:', font=("Arial", 12))
noun = [tk.IntVar(), 'NOUN']
packs['noun_checkbuttom'] = tk.Checkbutton(text='Существительные', variable=noun[0])
for_parts_of_speech.append(noun)
pronoun = [tk.IntVar(), 'PRONOUN']
packs['pronoun_checkbuttom'] = tk.Checkbutton(text='Местоимения', variable=pronoun[0])
for_parts_of_speech.append(pronoun)
verb = [tk.IntVar(), 'VERB']
packs['verb_checkbuttom'] = tk.Checkbutton(text='Глаголы', variable=verb[0])
for_parts_of_speech.append(verb)
adjective = [tk.IntVar(), 'ADJECTIVE']
packs['adjective_checkbuttom'] = tk.Checkbutton(text='Прилагательные', variable=adjective[0])
for_parts_of_speech.append(adjective)
adverb = [tk.IntVar(), 'ADVERB']
packs['adverb_checkbuttom'] = tk.Checkbutton(text='Наречия', variable=adverb)
for_parts_of_speech.append(adverb)
preposition = [tk.IntVar(), 'PREPOSITION']
packs['preposition_checkbuttom'] = tk.Checkbutton(text='Предлоги', variable=preposition[0])
for_parts_of_speech.append(preposition)
counjunction = [tk.IntVar(), 'COUNJUNCTION']
packs['counjunction_checkbuttom'] = tk.Checkbutton(text='Союзы', variable=counjunction[0])
for_parts_of_speech.append(counjunction)
interjection = [tk.IntVar(), 'INTERJECT']
packs['interjection'] = tk.Checkbutton(text='Существительные', variable=interjection[0])
for_parts_of_speech.append(interjection)

packs['path_to_file_buttom'] = tk.Button(text='Провести анализ текста', command=path_to_file)

for item in packs.items():
    item[1].pack(anchor='nw', padx=5, pady=2)




window.mainloop()