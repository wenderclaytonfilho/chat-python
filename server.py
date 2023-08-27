import tkinter as tk
import socket
import threading

#Janela do servidor

window = tk.Tk()
window.title("Server")

top_frame = tk.Frame(window)
btn_start = tk.Button(top_frame, text="Conectar", command=lambda:start_server())
btn_start.pack(side=tk.LEFT)
btn_stop = tk.Button(top_frame,text="Sair",command=lambda : stop_server(),state=tk.DISABLED)
btn_stop.pack(side=tk.LEFT)
top_frame.pack(side=tk.TOP,pady=(5,0))

middle_frame = tk.Frame(window)
lbl_host = tk.Label(middle_frame,text = "Host:X.X.X.X")
lbl_host.pack(side=tk.LEFT)
lbl_port=tk.Label(middle_frame,text="Porta:XXXX")
lbl_port.pack(side=tk.LEFT)
middle_frame.pack(side=tk.TOP,pady=(5,0))

client_frame = tk.Frame(window)
lbl_line=tk.Label(client_frame,text="---Lista de clientes---").pack()
scroll = tk.Scrollbar(client_frame)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
tk_display = tk.Text(client_frame,height=15,width=40)
tk_display.pack(side=tk.LEFT,fill=tk.Y,padx=(5,0))

tk_display.insert(tk.END, "User 1\n")
tk_display.insert(tk.END, "User 2\n")
tk_display.insert(tk.END, "User 3\n")
tk_display.insert(tk.END, "User 4\n")
tk_display.insert(tk.END, "User 5\n")
tk_display.insert(tk.END, "User 6\n")
tk_display.insert(tk.END, "User 7\n")
tk_display.insert(tk.END, "User 8\n")
scroll.config(command=tk_display.yview)
tk_display.config(yscrollcommand=scroll.set,background="#FFF",highlightbackground="grey", state="disabled")
client_frame.pack(side=tk.BOTTOM, pady=(5, 10))

#Fim da janela do servidor


def start_server():
    btn_start.config(state = tk.DISABLED)
    btn_stop.config(state = tk.NORMAL)

def stop_server():
    btn_start.config(state=tk.NORMAL)
    btn_stop.config(state=tk.DISABLED)





window.mainloop()