import tkinter as tk
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="skyblue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.config.side + 150, width=self.config.side, bg="skyblue")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio - 60),int(image_h//ratio//2 - 60)))

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(pady=5)

		self.label_username = tk.Label(self.main_frame, text="username", font=("Arial", 18, "bold"), bg="yellow", fg="black")
		self.label_username.pack(pady=5)

		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.var_username)
		self.entry_username.pack(pady=5)

		self.label_password = tk.Label(self.main_frame, text="password", font=("Arial", 18, "bold"), bg="yellow", fg="black")
		self.label_password.pack(pady=5)

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="PLAY GAME", font=("Arial", 18, "bold"), command=lambda:self.game.auth_login())
		self.btn_login.pack(pady=5)

		self.btn_register = tk.Button(self.main_frame, text = "Register", font = ("Arial", 18, "bold"), command = self.game.register)
		self.btn_register.pack(pady = 5)

		self.success_register = tk.Label(self.main_frame, text = "Register success, please re-enter username and password", font = ('Arial', 14))

		self.false_msg = tk.Label(self.main_frame, text = "WRONG PASSWORD / USERNAME", font = ("Arial", 12, "bold"), bg="yellow", fg="black")