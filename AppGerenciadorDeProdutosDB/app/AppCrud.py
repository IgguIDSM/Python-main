import tkinter as tk;
from tkinter import ttk
from numpy import delete

from pandas import read_feather;
import Crud as crud;

class MainApp:
    def __init__(self,win):
        self.objDB = crud.AppDB();
        #components
        self.lblCodigo = tk.Label(win,text='Codigo do produto:');
        self.lblNome = tk.Label(win,text='Nome do produto:');
        self.lblPreco = tk.Label(win,text='Preço do produto:');
        ###
        self.txtCodigo = tk.Entry(bd = 3);
        self.txtNome = tk.Entry();
        self.txtPreco = tk.Entry();
        #Buttons
        self.btnRegister = tk.Button(win,text='Cadastrar',command=self.fRegisterProduct);
        self.btnUpdate = tk.Button(win,text='Atualizar',command=self.fUpdateProduct);
        self.btnRemove = tk.Button(win,text='Excluir',command=self.fRemoveProduct);
        self.btnClear = tk.Button(win,text='Limpar',command=self.fClearScreen);
        #Tree View Components...
        self.columnData = ('Código','Nome','Preço');
        self.treeProducts = ttk.Treeview(win,columns=self.columnData,selectmode='browse');
        #
        #
        self.scrlBar = ttk.Scrollbar(win,orient='vertical',command=self.treeProducts.yview);
        self.scrlBar.pack(side='right',fill='x');
        #
        #
        self.treeProducts.configure(yscrollcommand=self.scrlBar.set);
        self.treeProducts.heading('Código',text='Código');
        self.treeProducts.heading('Nome',text='Nome');
        self.treeProducts.heading('Preço',text='Preço');
        #
        self.treeProducts.column('Código',minwidth=0,width=100);
        self.treeProducts.column('Nome',minwidth=0,width=100);
        self.treeProducts.column('Preço',minwidth=0,width=100);
        #
        self.treeProducts.pack(padx=10,pady=10);
        #
        self.treeProducts.bind('<<TreeviewSelect>>',self.showSelectedRegister);
        #Components positioning on screen
        #-------------------------------------------------------------------------#
        self.lblCodigo.place(x=100,y=50);
        self.txtCodigo.place(x=250,y=50);
        #
        self.lblNome.place(x=100,y=100);
        self.txtNome.place(x=250,y=100);
        #
        self.lblPreco.place(x=100,y=150);
        self.txtPreco.place(x=250,y=150);
        #
        self.btnRegister.place(x=100,y=200);
        self.btnUpdate.place(x=200,y=200);
        self.btnRemove.place(x=300,y=200);
        self.btnClear.place(x=400,y=200);
        #
        self.treeProducts.place(x=100,y=300);
        self.scrlBar.place(x=805,y=300,height=225);
        self.loadInitialData();
        #-------------------------------------------------------------------------#
        #end of INIT
    #_______________-------------------___________________#
    #Functions
    def showSelectedRegister(self,event):
        self.fClearScreen();
        for selection in self.treeProducts.selection():
            item = self.treeProducts.item(selection);
            codigo,nome,preco = item['values'][0:3]; # não sei o que o [0:3] quer dizer....
            self.txtCodigo.insert(0,codigo);
            self.txtNome.insert(0,nome);
            self.txtPreco.insert(0,preco);
    
    def loadInitialData(self):
        try:
            self.id = 0;
            self.iid= 0;
            regs = self.objDB.SelectData();
            for item in regs:
                codigo = item[0]; #cada iterador representa uma coluna para o requerimento do dado na linha
                nome = item[1];
                preco = item[2];
                self.treeProducts.insert('','end',iid=self.iid,values=(codigo,nome,preco));
                self.iid += 1;
                self.id += 1;
        except:
            print("Cant load a empty database....");
    
    def readFields(self):
        try:
            codigo = int(self.txtCodigo.get());
            nome = self.txtNome.get();
            preco = float(self.txtPreco.get());
        except:
            print('Something went wrong on data read....');
        return codigo,nome,preco; #type:ignore

    def fRegisterProduct(self):
        try:
            codigo,nome,preco = self.readFields();
            self.objDB.InsertData(codigo,nome,preco);
            self.treeProducts.insert('','end',iid=self.iid,values=(codigo,nome,preco));
            self.iid +=1;    
            self.id += 1;
            self.fClearScreen();
        except:
            print('Something went wrong on Product Register...');

    def fUpdateProduct(self):
        try:
            codigo,nome,preco = self.readFields();
            self.objDB.UpdateData(codigo,nome,preco);
            self.treeProducts.delete(*self.treeProducts.get_children());
            self.loadInitialData();
            self.fClearScreen();
        except:
            print('Something went wrong on Product Update......');
    
    def fRemoveProduct(self):
        try:
            codigo,nome,preco = self.readFields();
            self.objDB.RemoveData(codigo);
            self.treeProducts.delete(*self.treeProducts.get_children());
            self.loadInitialData();
            self.fClearScreen();
        except:
            print('Something went wrog on Product Remove......');
    
    def fClearScreen(self):
        try:
            self.txtCodigo.delete(0,tk.END);
            self.txtNome.delete(0,tk.END);
            self.txtPreco.delete(0,tk.END);
        except:
            print('Something went wrong in Clear Screen Procedure..........');
