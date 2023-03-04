import ttkbootstrap
from tkinter import filedialog
from tkinter.filedialog import askdirectory

MainWindow = ttkbootstrap.Window(title="Python-be-GUI", themename="superhero")
MainWindow.iconbitmap('./images/ico.ico')
MainWindow.place_window_center()
Big_Label = ttkbootstrap.Label(MainWindow, text="Python-be-GUI", font=("Serif", 40))
Big_Label.grid(row=1, column=0)
Little_Label = ttkbootstrap.Label(MainWindow, text="图形化应用生成系统", font=("楷体", 20))
Little_Label.grid(row=2, column=0)
lf1 = ttkbootstrap.Labelframe(text="操作区：")
lf1.grid(row=3, column=0)


def make_work():
    ttkbootstrap.Style("superhero")
    make_work_window = ttkbootstrap.Toplevel(title="新建项目")
    make_work_window.iconbitmap('./images/ico.ico')
    make_work_window.place_window_center()
    make_work_window.wm_attributes('-topmost', 1)
    make_work_lf1 = ttkbootstrap.Labelframe(make_work_window, text="参数：")
    make_work_lf1.grid(row=1, column=0)
    make_work_lf1_Label1 = ttkbootstrap.Label(make_work_lf1, text="项目名称：", font=("楷体", 10))
    make_work_lf1_e1_content = ttkbootstrap.StringVar()
    make_work_lf1_e1 = ttkbootstrap.Entry(make_work_lf1, width=50, textvariable=make_work_lf1_e1_content)
    make_work_lf1_Label1.grid(row=1, column=0)
    make_work_lf1_e1.grid(row=1, column=1)
    make_work_lf1_Label2 = ttkbootstrap.Label(make_work_lf1, text="项目位置：", font=("楷体", 10))

    def get_path():
        path_in_make_work = askdirectory(title='请选择文件夹', )
        entry_text.set(path_in_make_work)

    make_work_lf1_b1 = ttkbootstrap.Button(make_work_lf1, text="点击选择", command=get_path)
    entry_text = ttkbootstrap.StringVar()
    make_work_lf1_e2 = ttkbootstrap.Entry(make_work_lf1, width=50, textvariable=entry_text)
    make_work_lf1_Label2.grid(row=2, column=0)
    make_work_lf1_e2.grid(row=2, column=1)
    make_work_lf1_b1.grid(row=2, column=2)


def open_work():
    open_work_path = filedialog.askopenfilename(title='请选择项目文件',
                                                filetypes=[('此程序的项目文件', '.PythonGUIWork')])


new = ttkbootstrap.Button(lf1, text="新建项目", command=make_work, width=50)
new.grid(row=1, column=0)
open = ttkbootstrap.Button(lf1, text="打开项目", command=open_work, width=50)
open.grid(row=2, column=0)
MainWindow.mainloop()
