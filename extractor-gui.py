import instaloader
import time
from tkinter import *

class Application:
	def __init__(self, master=None):
		self.fontePadrao = ("Arial", "10")
		self.primeiroContainer = Frame(master)
		self.primeiroContainer['pady'] = 20
		self.primeiroContainer['pady'] = 5
		self.primeiroContainer.pack()

		self.segundoContainer = Frame(master)
		self.segundoContainer['padx'] = 20
		self.segundoContainer['pady'] = 5
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer['padx'] = 20
		self.terceiroContainer['pady'] = 5
		self.terceiroContainer.pack()

		self.quartoContainer = Frame(master)
		self.quartoContainer['padx'] = 20
		self.quartoContainer['pady'] = 5
		self.quartoContainer.pack()

		self.quintoContainer = Frame(master)
		self.quintoContainer['padx'] = 20
		self.quintoContainer['pady'] = 5
		self.quintoContainer.pack()

		self.sextoContainer = Frame(master)
		self.sextoContainer['pady'] = 20
		self.sextoContainer.pack()

		self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
		self.titulo['font'] = ("Arial", "10", "bold")
		self.titulo.pack()

		self.nomeLabel = Label(self.segundoContainer, text="Username", font=self.fontePadrao)
		self.nomeLabel["width"] = 10
		self.nomeLabel.pack(side=LEFT)

		self.nome = Entry(self.segundoContainer)
		self.nome['width'] = 25
		self.nome['font'] = self.fontePadrao
		self.nome.pack(side=LEFT)

		self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
		self.senhaLabel["width"] = 10
		self.senhaLabel.pack(side=LEFT)

		self.senha = Entry(self.terceiroContainer)
		self.senha['width'] = 25
		self.senha['font'] = self.fontePadrao
		self.senha['show'] = "*"
		self.senha.pack(side=LEFT)

		self.perfilLabel = Label(self.quartoContainer, text="Perfil", font=self.fontePadrao)
		self.perfilLabel["width"] = 10
		self.perfilLabel.pack(side=LEFT)

		self.perfil = Entry(self.quartoContainer)
		self.perfil['width'] = 25
		self.perfil['font'] = self.fontePadrao
		self.perfil.pack(side=RIGHT)

		self.quantidadeLabel = Label(self.quintoContainer, text="Quantidade", font=self.fontePadrao)
		self.quantidadeLabel["width"] = 10
		self.quantidadeLabel.pack(side=LEFT)

		self.quantidade = Entry(self.quintoContainer)
		self.quantidade['width'] = 25
		self.quantidade['font'] = self.fontePadrao
		self.quantidade.pack(side=RIGHT)

		self.autenticar = Button(self.sextoContainer)
		self.autenticar["text"] = "Buscar"
		self.autenticar["font"] = ("Calibri", "8")
		self.autenticar["width"] = 12
		self.autenticar["command"] = self.search
		self.autenticar.pack(side=LEFT)

		self.mensagem = Label(self.sextoContainer, text="Bora lá!", font=self.fontePadrao)
		self.mensagem.pack(side=RIGHT)

	def search(self):
		username = self.nome.get()
		password = self.senha.get()
		search = self.perfil.get()
		max_posts = int(self.quantidade.get())

		L = instaloader.Instaloader()
		L.login(username,password)
		profile = instaloader.Profile.from_username(L.context, search)

		likes = set()
		likes_all = list()
		self.mensagem['text'] = "extraindo likes dos posts do perfil {}".format(search)
		time.sleep(3)
		for k,post in enumerate(profile.get_posts()):
			if k < max_posts:
				new = post.get_likes()
				likes_all.extend(list(new))
				likes = likes | set(post.get_likes())
		self.mensagem['text'] = "extraindo seguidores do perfil {}".format(search)
		# followers = set(profile.get_followers())

		self.mensagem['text'] = "Armazenando perfis ativos..."
		with open("likes_unicos_ultimos_{}_posts_de_{}.txt".format(str(max_posts), search), 'w') as f:
			for k,like in enumerate(likes):
				print(like.username, file=f)
		self.mensagem['text'] = "Armazenando todos os likes..."
		with open("likes_todos_ultimos_{}_posts_de_{}.txt".format(str(max_posts), search), 'w') as f:
			for k,like in enumerate(likes_all):
				print(like.username, file=f)
		self.mensagem['text'] = "Finalizado! Arquivos foram salvos."

root = Tk()
Application(root)
root.mainloop()

#if __name__=="__main__":
	# main()
