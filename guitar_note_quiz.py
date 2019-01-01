import random
import time
import ctypes

def main():
    quiz_start()
    note_quiz(strings=["E", "A"], note_list=notes, repeat=8, time_interval=5, random_element=True)

# ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

strings = ["E", "A", "D", "G", "B", "e"]

notes = ["A", "A#", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb",
         "E", "F", "F#", "Gb", "G", "G#", "Ab"]


def note_quiz(strings, note_list, time_interval, repeat=17, random_element=False):
    used_notes = []  # initiate list to hold used notes
    for i in range(0, repeat):
        if random_element:  # is True then select random list element, can repeat and exclude values
            index_num = rand_int_in_range(note_list)
        else:  # is False then shuffle list, select notes in order and repeat list from beginning
            if i < 1:
                random.shuffle(note_list)
            if i > (len(note_list) - 1):
                index_num = i - len(note_list)
            else:
                index_num = i
        time.sleep(time_interval)
        string = strings[random.randint(0, len(strings)-1)]
        print("Play",notes[index_num], "on the", string, "string")
        used_notes.append(notes[index_num] + " on " + string )
    time.sleep(1.5)
    print("Here are the notes you practiced:")
    print(used_notes)

def rand_int_in_range(notes_list):
    # select random index num of list
    return random.randint(0, len(notes_list)-1)

def quiz_start():
    print("Get ready to practice")
    time.sleep(2)
    print("3")
    time.sleep(.5)
    print("2")
    time.sleep(.5)
    print("1")
    time.sleep(.5)
    print("Go!")

if __name__ == '__main__': main()
