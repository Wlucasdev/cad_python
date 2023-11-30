from BancoDados import *

# lista_l = Nome da lista de clientes no banco de dados

window = tix.Tk()  # Tk() para criar uma janela


class Validar:  # Validar entradas
    def validate_entry2(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99999999999


class Relatorio():
    def PrintCliente(self):
        webbrowser.open("CLIENTE.pdf")

    def RelatorioCliente(self):
        self.can = canvas.Canvas("CLIENTE.pdf")
        # ----------------------------Pegando Relatórios-----------------------------------
        self.n_Relatorio = self.n_lab2.get()
        self.id_Relatorio = self.id_ent.get()
        self.nome_Relatorio = self.nome_ent.get()
        self.tel_Relatorio = self.tel_ent.get()
        self.cid_Relatorio = self.cid_ent.get()
        # ---------------------------- Fonte e Titulo-------------------------------------------

        self.can.drawString(200, 790, "FICHA DO CLIENTE")
        self.can.drawString(400, 100, self.nome_Relatorio)
        # ---------------------------- Chamar e Salvar pagina----------------------------------
        self.can.showPage()
        self.can.save()
        self.PrintCliente()


class Cliente(Dados, Relatorio, Validar):

    def __init__(self):  # Tela Inicial
        self.window = window  # Indentificar a minha janela
        self.validateEntradas()
        self.configuracao_do_menu()  # importando a funçao
        self.frame_window()  # funções da flame 1 e 2
        self.abas()
        self.btc()
        self.lab()
        self.entradas()
        self.lista_clientes()
        self.bd_clientes()
        self.select_lista()
        self.Baloes_texto()
        self.menu()
        # self.adicionar_cliente()
        window.mainloop()  # Quando abrir tem que fechar a janela

    def configuracao_do_menu(self):  # Função para digner da tela
        self.window.title("Sistema De Adiministração De Materia Prima")  # Nome da tela
        self.window.config(background="#054F77")  # Cor em Hexadecimal
        self.window.geometry("800x600")  # Tamanho da janela
        self.window.resizable(True, True)  # poder controlar o tamnaho da tela
        self.window.maxsize()  # controlar o maximo de expanção da tela
        self.window.minsize(height=400, width=300)  # controlar o minimo de expanção da tela

    def frame_window(self):  # Função da Frame =  frame 1 e 2
        self.flame_up = Frame(self.window, bd=4, bg="#dfe3ee",
                              # Onde vai ficar, números de borda,cor da frame
                              # Cor das Bordas e o tamanho das Bordas
                              highlightbackground="black", highlightthickness=2)
        # inicio do frame X e Y em % , Tamanho do frame em %
        self.flame_up.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.45)
        self.flame_down = Frame(self.window, bd=4, bg="#dfe3ee",
                                # Onde vai ficar, números de borda,cor da frame
                                # Cor das Bordas e o tamanho das Bordas
                                highlightbackground="black", highlightthickness=2)
        # inicio do frame X e Y em % , Tamanho do frame em %
        self.flame_down.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.45)

    def abas(self):
        self.abass = ttk.Notebook(self.flame_up)

        # ------------Criando as abas-------------
        self.abas1 = Frame(self.abass)
        self.abas2 = Frame(self.abass)

        # ------------Cor das Abas----------------
        self.abas1.configure(background="lightgray")
        self.abas2.configure(background="lightgray")
        # ------------Adiconar as Abas-------------
        self.abass.add(self.abas1, text="A")
        self.abass.add(self.abas2, text="B")
        # -----------Local das abas----------------
        self.abass.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
        # ----------------------clendaario
        self.bt_calendario = Button(self.abas2, text="Data", command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.5)
        self.entry_data = Entry(self.abas2, width=10)
        self.entry_data.place(rely=0.2, relx=0.4)

    def btc(self):
        # ----------------------------------CANVAS ENTRE OS BOTOA LIMPAR BUSCAR ------------------------------------------------
        self.canvas_bt = Canvas(self.abas1, bd=0, bg="#4682B4", highlightbackground="black",
                                highlightthickness=1)
        self.canvas_bt.place(relx=0.293, rely=0.03, relwidth=0.18, relheight=0.19)

        # -------------------------------------- inicio dos botoes--------------------------------------------------------------

        # BOTAO LIMPAR
        self.btc_delete = Button(self.abas1, bd=6, bg="#e4edea", text="Limpar",
                                 highlightbackground="black", highlightthickness=0.2,
                                 activebackground="red", activeforeground="white",
                                 # EFEITO AO CLICAR      LETRA                   BOTÃO MUDAR AS CORER
                                 command=self.limpar_tela)
        self.btc_delete.place(relx=0.3, rely=0.05, relwidth=0.08, relheight=0.15)

        # Botão de Buscar
        self.btc_buscar = Button(self.abas1, bd=6, bg="#e4edea", text="Buscar",
                                 highlightbackground="black", highlightthickness=0.2,
                                 activebackground="white", activeforeground="#FF8C00",
                                 command=self.localiza_cl)
        self.btc_buscar.place(relx=0.385, rely=0.05, relwidth=0.08, relheight=0.15)
        # Botão de Criar novo
        self.btc_criar = Button(self.abas1, bd=6, bg="#e4edea", text="Cadastrar",
                                highlightbackground="black", highlightthickness=0.2,
                                activebackground="white", activeforeground="#228B22",
                                command=self.adicionar_cliente)
        self.btc_criar.place(relx=0.69, rely=0.05, relwidth=0.12, relheight=0.15)
        # Botão de Alterar
        self.btc_alterar = Button(self.abas1, bd=6, bg="#e4edea", text="Alterar",
                                  highlightbackground="black", highlightthickness=0.2,
                                  command=self.alterar_cl)
        self.btc_alterar.place(relx=0.9, rely=0.05, relwidth=0.08, relheight=0.15)

        # Botão de excluir

        self.btc_excluir = Button(self.abas1, bd=6, bg="#e4edea", text="Excluir",
                                  highlightbackground="black", highlightthickness=0.2,
                                  activeforeground="darkred", activebackground="white",
                                  command=self.deletar_cl)
        self.btc_excluir.place(relx=0.815, rely=0.05, relwidth=0.08, relheight=0.15)

        # Botão teste
        self.btc_teste = Button(self.abas2, bd=6, bg="green", text="New"
                                , highlightbackground="black", highlightthickness=0.2,
                                activeforeground="darkred", activebackground="white",
                                command=self.windows2)
        self.btc_teste.place(relx=0.815, rely=0.05, relwidth=0.08, relheight=0.15)

    def Baloes_texto(self):
        self.balao_criar = tix.Balloon(self.abas1)
        self.balao_criar.bind_widget(self.btc_criar, balloonmsg="""Digite os dados Primeiro e Depois em Cadastrar!""")

        self.balao_deletar = tix.Balloon(self.abas1)
        self.balao_deletar.bind_widget(self.btc_excluir, balloonmsg="Selecione o item para escluir!")

        self.balao_buscar = tix.Balloon(self.abas1)
        self.balao_buscar.bind_widget(self.btc_buscar, balloonmsg="Digite o CPF para poder Buscar")

    def lab(self):  # Criar os Texto em cima das caixas de textos
        # N
        self.n_lab = Label(self.abas1, bg="#f2f4f5", text="Num")
        self.n_lab.place(relx=0.20, rely=0.05, relheight=0.1, relwidth=0.05)
        # CPF
        self.CPF_lab = Label(self.abas1, bg="#f2f4f5", text="CPF")
        self.CPF_lab.place(relx=0.01, rely=0.05, relheight=0.1, relwidth=0.15)
        # Nome
        self.nome_lab = Label(self.abas1, bg="#f2f4f5", text="Nome")
        self.nome_lab.place(relx=0.01, rely=0.27, relheight=0.1, relwidth=0.15)
        # Telefone
        self.tel_lab = Label(self.abas1, bg="#f2f4f5", text="Telefone")
        self.tel_lab.place(relx=0.01, rely=0.5, relheight=0.1, relwidth=0.15)
        # Cidades
        self.cid_lab = Label(self.abas1, bg="#f2f4f5", text="Cidade")
        self.cid_lab.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.15)

    def entradas(self):  # caixas de textos
        #  N
        self.n_lab2 = Entry(self.abas1, bg="white")
        self.n_lab2.place(relx=0.20, rely=0.16, relwidth=0.05, relheight=0.1)
        #  cpf
        self.id_ent = Entry(self.abas1, bg="white", validate="key", validatecommand=self.entrada2)
        self.id_ent.place(relx=0.01, rely=0.16, relheight=0.1, relwidth=0.15)
        # Nome
        self.nome_ent = Entry(self.abas1, bg="white")
        self.nome_ent.place(relx=0.01, rely=0.38, relheight=0.1, relwidth=0.9)
        # Telefone
        self.tel_ent = Entry(self.abas1, bg="white")
        self.tel_ent.place(relx=0.01, rely=0.62, relheight=0.1, relwidth=0.4)
        # cidade
        self.cid_ent = Entry(self.abas1, bg="white")
        self.cid_ent.place(relx=0.5, rely=0.62, relheight=0.1, relwidth=0.4)

    def lista_clientes(self):  # Criar colunas com visualização
        self.lista_l = ttk.Treeview(self.flame_down, height=3, columns=("col0", "col1", "col2", "col3", "col4"))
        self.lista_l.place(relx=0.01, rely=0.01, relheight=0.95, relwidth=0.95)

        # Coluna 0
        self.lista_l.heading("#0", )
        self.lista_l.column("#0", width=1)
        # COLUNA 0
        self.lista_l.heading("#1", text="N")
        self.lista_l.column("#1", width=1)
        # Coluna CPF
        self.lista_l.heading("#2", text="CPF")
        self.lista_l.column("#2", width=50)
        # Coluna nome
        self.lista_l.heading("#3", text="Nome")
        self.lista_l.column("#3", width=200)
        # Coluna telefone
        self.lista_l.heading("#4", text="Tel")
        self.lista_l.column("#4", width=150)
        # Coluna Cidade
        self.lista_l.heading("#5", text="Cidade")
        self.lista_l.column("#5", width=150)

        # Rolagem da coluna
        self.scrool_lista = Scrollbar(self.flame_down, orient="vertical")
        self.lista_l.configure(yscroll=self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.07, relheight=0.85, relwidth=0.02)
        self.lista_l.bind("<Double-1>", self.select_cliente)

    def menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar)

        def Quit(): self.window.destroy()

        menubar.add_cascade(label="Opçõe", menu=menu1)
        menubar.add_cascade(label="Relatório", menu=menu2)

        menu1.add_command(label="Sair", command=Quit)

        menu2.add_command(label="Ficha do Cliente", command=self.RelatorioCliente)

    def windows2(self):
        self.windows_2 = Toplevel()
        self.windows_2.title("Teste")
        self.windows_2.configure(background="blue")
        self.windows_2.geometry("800x600")
        self.windows_2.resizable(False, False)
        self.windows_2.transient(self.window)
        self.windows_2.focus_force()

    def validateEntradas(self):
        self.entrada2 = (self.window.register(self.validate_entry2), "%P")


Cliente()
