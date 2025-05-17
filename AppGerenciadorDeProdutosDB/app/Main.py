#Aplicação em si
import tkinter as tk;
import AppCrud as ac;
janela = tk.Tk();
principal = ac.MainApp(janela);
janela.title('Bem Vindo a Aplicação de banco de dados!');
janela.geometry('820x600+10+10');
janela.mainloop();