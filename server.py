import tkinter as tk
import socket
import threading


server = None
HOST_ADDR = "localhost"
HOST_PORT = 8080


client_name = ""
clients = []
clients_names = []



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
    global server, HOST_ADDR,HOST_PORT
    btn_start.config(state = tk.DISABLED)
    btn_stop.config(state = tk.NORMAL)

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)
    server.bind((HOST_ADDR,HOST_PORT))
    server.listen(5)

    threading._start_new_thread(accept_clients, (server, " "))


    lbl_host["text"] = "Host: " + HOST_ADDR
    lbl_port["text"] = "Port: " + str(HOST_PORT)
    print("Server iniciado!")


def stop_server():
    btn_start.config(state=tk.NORMAL)
    btn_stop.config(state=tk.DISABLED)
    print("Server finalizado!")

def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)
        
        threading._start_new_thread(send_receive_client_message, (client,addr))



def send_receive_client_message(client_connection, client_ip_addr):
    global server,client_name, clients, clients_addr
    client_msg = " "

    client_name = client_connection.recv(4096).decode("utf-8")
    welcome_msg = "Bem vindo! " + client_name + ". Use '/q' para sair"
    client_connection.send(welcome_msg.encode("utf-8"))

    clients_names.append(client_name)

    update_client_names_display(clients_names)

    while True:
        data = client_connection.recv(4096).decode("utf-8")
        if not data: break
        if data == "/q":break

        client_msg = data

        idx = get_client_index(clients,client_connection)
        sending_client_name = clients_names[idx]

        for c in clients:
            if c != client_connection:
                server_msg = str(sending_client_name + "->" + client_msg)
                c.send(server_msg.encode("utf-8"))



    idx = get_client_index(clients,client_connection)
    del clients_names[idx]
    server_msg = "Adeus!"
    client_connection.send(server_msg.encode("utf-8"))
    client_connection.close()

    update_client_names_display(clients_names)


def get_client_index(client_list,curr_client):
    idx=0
    for conn in client_list:
        if conn == curr_client:
            break
        idx+=1
    return idx


def update_client_names_display(names_list):
    tk_display.config(state=tk.NORMAL)
    tk_display.delete('1.0',tk.END)

    for c in names_list:
        tk_display.insert(tk.END,c+"\n")
    tk_display.config(state=tk.DISABLED)




window.mainloop()