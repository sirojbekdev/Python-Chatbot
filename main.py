from tkinter import *
from threading import Timer
import tkinter.ttk as ttk
import wikipedia
import pyttsx3
import re
import responses as res


speaker = pyttsx3.init()
speaker.setProperty('rate', 130)
FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 13 bold"

window = Tk("U.S.A Presidents")
window.resizable(width=False, height=False)
window.geometry("700x800")
tabControl = ttk.Notebook(window)

bot = ttk.Frame(tabControl)
wiki = ttk.Frame(tabControl)

# Wiki Tab

top_frame = Frame(wiki)

top_label = Label(top_frame, text="Search: ", width=10)
top_label.pack(side="left")

# textbox for search input
top_entry = Entry(top_frame, width=40)
top_entry.pack(side="left")

lb = Text(wiki, bg="wheat", height=25, wrap="word", pady=5, padx=10)
lb.pack(side="bottom", fill="x")

# output of the summary
out_frame = Frame(wiki, height=350)
out_frame.pack(fill=BOTH, side="bottom")


def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        info = wikipedia.page(data).summary
        lb.delete("1.0", END)
        lb.insert('1.0', info)
        if lb.count('1.0', END):
            speaker.say(info)
            speaker.runAndWait()
    else:
        lb.configure(text="")


# list output
main_Listbox = Listbox(out_frame, height=15)
main_Listbox.bind("<<ListboxSelect>>", callback)

# Scrollbar
scr = Scrollbar(out_frame)
scr.pack(side=RIGHT, fill=BOTH)
main_Listbox.config(yscrollcommand=scr.set)
main_Listbox.pack(side="top", fill=BOTH)
scr.config(command=main_Listbox.yview)


# Search from Wikipedia
def search():
    result = wikipedia.search(top_entry.get())

    if not result:
        ttk.messagebox.showinfo("Please fill the search field")

    else:
        if not main_Listbox.get(0, END):
            for index, item in enumerate(result):
                main_Listbox.insert(index, item)
        else:
            main_Listbox.delete(0, 'end')
            for index, item in enumerate(result):
                main_Listbox.insert(index, item)


top_btn = Button(top_frame, command=search, text="Search", width="15")
top_btn.pack(side="right")
top_frame.pack(side="top", fill="x")


# Bot Tab
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def loop_through_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, required_words)

    for key in res.shorts:
        response(key['bot_response'], key['list_of_words'], key['required_words'])

    for key in res.longs:
        response(key['bot_response'], key['list_of_words'], key['required_words'])

    # takes best match from highest_prop_list
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return res.no_response_wiki_advice() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = loop_through_messages(split_message)
    return response


def _on_enter_pressed(event):
    msg = msg_entry.get()
    _insert_message(msg)


# Inserts dialog
def _insert_message(msg):
    if not msg:
        return

    msg_entry.delete(0, END)
    msg1 = f"You: {msg}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, msg1)
    text_widget.configure(state=DISABLED)

    respo = get_response(msg)
    msg2 = f"Bot: {respo}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, msg2)
    text_widget.configure(state=DISABLED)

    text_widget.see(END)
    speaker.say(respo)
    # speaker.runAndWait()
    time = Timer(0.5, speaker.runAndWait, None)
    time.start()


#  divider
line = Label(bot, width=450, bg="#CFCFCF")
line.place(relwidth=1, rely=0.07, relheight=0.012)

# text widget
text_widget = Text(bot, width=22, height=5, bg="#FDFDFD", fg="#050505", font=FONT, padx=15, pady=5, wrap='word')
text_widget.place(relheight=1, relwidth=1, rely=0.01)
text_widget.configure(cursor="arrow", state=DISABLED)

# scroll bar
scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.99)
scrollbar.configure(command=text_widget.yview)

# bottom label
bottom_label = Label(bot, bg="#CFCFCF", height=40)
bottom_label.place(relwidth=1, rely=0.9)

# message entry box
msg_entry = Entry(bottom_label, bg="#8C3E50", fg="#050505", font=FONT)
msg_entry.place(relwidth=0.84, relheight=0.1, rely=0.01, relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>", _on_enter_pressed)

# send button
send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg="#CFCFCF", command=lambda: _on_enter_pressed(None))
send_button.place(relx=0.87, rely=0.01, relheight=0.1, relwidth=0.1)


# Packing the tabs

tabControl.add(bot, text='Bot', underline=True, padding=5)
tabControl.add(wiki, text='Wiki', underline=True, padding=10)
tabControl.pack(expand=1, fill="both")


window.mainloop()
