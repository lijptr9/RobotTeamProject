import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Control Pad")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    fetch_button = ttk.Button(main_frame, text="Go fetch!" )
    fetch_button.grid(row=0, column=0)
    fetch_button['command'] = lambda: send_fetch(mqtt_client)

    faster_button = ttk.Button(main_frame, text="Go faster!")
    faster_button.grid(row=0, column=2)
    faster_button['command'] = lambda: send_faster(mqtt_client)

    back_button = ttk.Button(main_frame, text="Come back")
    back_button.grid(row=3, column=0)
    back_button['command'] = lambda : send_comeback(mqtt_client)

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=2)
    stop_button['command'] = lambda: send_stop(mqtt_client)


    up_button = ttk.Button(main_frame, text="Pick it up")
    up_button.grid(row=4, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)

    down_button = ttk.Button(main_frame, text="Put it down")
    down_button.grid(row=4, column=2)
    down_button['command'] = lambda: send_down(mqtt_client)

    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=1, column=1)
    quit_button['command'] = (lambda: quit_program(mqtt_client, False))

    exit_button = ttk.Button(main_frame, text="Exit")
    exit_button.grid(row=2, column=1)
    exit_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()

def send_fetch(mqtt_client):
    print("fetching")
    mqtt_client.send_message("go_fetch")


def send_faster(mqtt_client):
    print("running faster")
    mqtt_client.send_message("go_faster")


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

def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("exit")
    mqtt_client.close()
    exit()

main()
