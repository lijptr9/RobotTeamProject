import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

def window():
    window = tkinter.Tk()
    window.title='CSSE120 Final Project'
    main_frame2 = ttk.Frame(window, padding=5)
    main_frame2.grid()

    canvas=tkinter.Canvas(main_frame2, background="white", width=500, height=400)
    canvas.grid(columnspan=4)
    canvas.grid(rowspan=4)

    canvas.create_text(250, 150, fill="darkblue", font="Times 20 italic bold",
                            text="CSSE120 Final Project")
    canvas.create_text(255, 180, fill="darkblue", font="Times 20 italic bold",
                       text="Dog Fun")

    continue_button = ttk.Button(main_frame2, text="Continue")
    continue_button.grid(row=4, column=3)
    continue_button['command']=lambda: next_window()
    window.mainloop()


def next_window():
    main()



def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Send command to dog")

    main_frame = ttk.Frame(root, padding=40, relief='raised')
    main_frame.grid()

    fetch_button = ttk.Button(main_frame, text="Go fetch!" )
    fetch_button.grid(row=0, column=0)
    fetch_button['command'] = lambda: send_fetch(mqtt_client)

    back_button = ttk.Button(main_frame, text="Come back")
    back_button.grid(row=0, column=2)
    back_button['command'] = lambda : send_comeback(mqtt_client)

    stop_button = ttk.Button(main_frame, text="Freeze")
    stop_button.grid(row=1, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)


    up_button = ttk.Button(main_frame, text="Pick it up")
    up_button.grid(row=3, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)

    down_button = ttk.Button(main_frame, text="Put it down")
    down_button.grid(row=3, column=2)
    down_button['command'] = lambda: send_down(mqtt_client)

    root.mainloop()

def send_fetch(mqtt_client):
    print("fetching")
    mqtt_client.send_message("go_fetch")


def send_comeback(mqtt_client):
    print("running back")
    mqtt_client.send_message("come_back")


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")

def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")

window()