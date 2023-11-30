from Biblioteca import *


class Dados:
    def __init__(self):
        self.limpar_tela()
        self.conectar_bd()
        self.desconectar_bd()
        self.bd_clientes()
        self.adicionar_cliente()
        self.select_lista()
        self.select_cliente()
        self.deletar_cl()
        self.alterar_cl()
        self.localiza_cl()
        self.calendario()
        self.print_calendario()

    def limpar_tela(self):
        self.n_lab2.delete(0, END)
        self.nome_ent.delete(0, END)
        self.id_ent.delete(0, END)
        self.cid_ent.delete(0, END)
        self.tel_ent.delete(0, END)

    def conectar_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor();
        print("Conectando ao Banco de Dados")

    def desconectar_bd(self):
        self.conn.close();
        print("Banco de dados Desconectado")

    def bd_clientes(self):
        self.conectar_bd()
        # Tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                N INTEGER PRIMARY KEY,
                cod INTEGER(11),
                Nome_cliente CHAR(40) NOT NULL,
                tel INTEGER(20),
                Cidade CHAR(40)
            );
        """)
        self.conn.commit();
        print("Banco Criado")
        self.desconectar_bd()

    def adicionar_cliente(self):
        self.n = self.n_lab2.get()
        self.id = self.id_ent.get()
        self.nome = self.nome_ent.get().upper()
        self.tel = self.tel_ent.get()
        self.cid = self.cid_ent.get().upper()
        if self.nome_ent.get() == "":
            msg = "O Prenchimento Nome não pode ficar em branco"
            messagebox.showwarning("Erro no Preenchimento", msg)
        elif self.id_ent.get() == "":
            msg2 = "Cpf tem que ser digitados"
            messagebox.showwarning(" CPF", msg2)
        elif len(self.id_ent.get()) < 11:
            msg3 = "Cpf têm 11 números"
            messagebox.showerror("Erro no CPF", msg3)
            mm = 5, 5
        else:
            listaCPF = []
            x = self.id_ent.get();
            x.split()
            for l2 in x:
                listaCPF.append(int(l2))
            print(listaCPF)
            listad1 = []
            listad2 = []
            mult = 10
            n = 0
            while n < 9:
                listad1.append(listaCPF[n] * mult)
                n += 1
                mult -= 1
            dig1 = (11 - sum(listad1) % 11)
            print(sum(listaCPF))
            print(dig1)
            n = 0
            mult = 11
            while n < 10:
                listad2.append(listaCPF[n] * mult)
                n += 1
                mult -= 1
            dig2 = (11 - sum(listad2) % 11)
            print(sum(listaCPF))
            print(dig2)

            if dig1 != listaCPF[9] and dig2 != listaCPF[10]:

                msg3 = "Cpf invalido"
                messagebox.showerror("Erro no CPF", msg3)
            else:
                self.conectar_bd()
                self.cursor.execute("""INSERT INTO Clientes (cod,Nome_cliente,tel,Cidade)
                     VALUES (?, ?, ?, ?) """, (self.id, self.nome, self.tel, self.cid))
                self.conn.commit()
                self.desconectar_bd()
                self.select_lista()
                self.limpar_tela()

    def select_lista(self):  # Para espelhar a lista no flame down
        self.lista_l.delete(*self.lista_l.get_children())
        # lista_l nome do comando que cria a lista de clientes no banco
        self.conectar_bd()
        listaclientes = self.cursor.execute("""SELECT  N ,cod, Nome_cliente,tel,Cidade FROM Clientes
             ORDER BY N ASC""")
        # Cliar uma lista com as informações do banco de dados
        for lcl in listaclientes:
            self.lista_l.insert("", END, values=lcl)
        self.desconectar_bd()

    def select_cliente(self, event):  # Colocar event para avisar o python sobre algum evento
        self.limpar_tela()
        self.lista_l.selection()

        for lcl2 in self.lista_l.selection():  # comando para varrer a lista
            col0, col1, col2, col3, col4 = self.lista_l.item(lcl2, "values")
            self.n_lab2.insert(END, col0)
            self.id_ent.insert(END, col1)
            self.nome_ent.insert(END, col2)
            self.tel_ent.insert(END, col3)
            self.cid_ent.insert(END, col4)

    def deletar_cl(self):
        self.n = self.n_lab2.get()
        self.id = self.id_ent.get()
        self.nome = self.nome_ent.get()
        self.tel = self.tel_ent.get()
        self.cid = self.cid_ent.get()
        self.conectar_bd()
        self.cursor.execute(""" DELETE FROM Clientes WHERE N = ? """, self.n)
        self.conn.commit()
        self.desconectar_bd()
        self.limpar_tela()
        self.select_lista()

    def alterar_cl(self):
        self.n = self.n_lab2.get()
        self.id = self.id_ent.get()
        self.nome = self.nome_ent.get().upper()
        self.tel = self.tel_ent.get()
        self.cid = self.cid_ent.get().upper()
        self.conectar_bd()
        self.cursor.execute(""" UPDATE Clientes SET Nome_cliente = ?, tel = ?,Cidade = ?, cod=?
        WHERE N =?""", (self.nome, self.tel, self.cid, self.id, self.n))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpar_tela()

    def localiza_cl(self):
        self.conectar_bd()
        self.lista_l.delete(*self.lista_l.get_children())
        # Este comando é para limpar a lista e reescrever com os novos requisitos

        self.id_ent.insert(END, '%')  # em SQL Pede a %, esse comando pé um coringa
        cpf = self.id_ent.get()  # onde vai pegar a informação
        self.cursor.execute(
            """SELECT N, cod, Nome_cliente, tel, Cidade FROM Clientes WHERE cod LIKE  '%s'  ORDER BY 
            cod ASC """ % cpf
        )  # Execussão do Banco de DADOS
        localizar_cl = self.cursor.fetchall()
        for lcl in localizar_cl:
            self.lista_l.insert("", END, values=lcl)
        self.limpar_tela()
        self.desconectar_bd()

    def calendario(self):
        self.calendario1 = Calendar(self.abas2, fg="gray75", bg="blue", Font=("Times", "9", "bold"), locale="pt_br")
        self.calendario1.place(relx=0.8, rely=0.1)
        self.calDataInicial = Button(self.abas2, text="calendario")
        self.calDataInicial.place(rely=0.1, relx=0.8, height=25, width=100)

    def print_calendario(self):
        datainicial = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, datainicial)
        self.calData.destroy()
