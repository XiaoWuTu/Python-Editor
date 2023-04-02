import ttkbootstrap as tk
import pyglet as pgt

Main = tk.Window(themename="cosmo", title="Python-Editor-初始页面", size=(480, 270))
pgt.font.add_file("./fonts/1.ttf")
l_main = tk.Label(text="Python-Editor-2023", bootstyle="primary", font=("锐字锐线梦想黑简1.0", 20))
l_main.grid(row=0, column=0)
img = tk.PhotoImage(file="./images/ico-small.png")
l_img = tk.Label(image=img)
l_img.grid(row=0, column=1)
tk.Separator(bootstyle="warning").grid(sticky="EW", row=1, column=0)
lf_this = tk.Labelframe(text="本地：", width=240, height=100, bootstyle="primary")
lf_this.grid(row=2, column=0)
lf_air = tk.Labelframe(text="从Internet抓取（git）", width=240, height=100, bootstyle="primary")
lf_air.grid(row=3, column=0)
Main.mainloop()
