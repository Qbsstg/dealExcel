from tkinter import *

options = ["数世数据", "原始数据"]


def show_listbox_dialog():
    # 创建窗口
    window = Tk()

    # 设置窗口大小
    # window.geometry("100x100")

    # 设置窗口标题
    window.title("选择数据来源")

    # 创建Listbox组件
    listbox = Listbox(window, height=len(options) + 2, justify=CENTER, width=30)

    # 往Listbox组件中添加选项
    for option in options:
        listbox.insert(END, option)

    # 创建确定按钮,并水平排列
    confirm_btn = Button(window, text="确定", command=lambda: [on_confirm(listbox), window.destroy()], width=5)

    # 创建取消按钮
    cancel_btn = Button(window, text="取消", command=lambda: window.destroy(), width=5)

    # 将Listbox组件和按钮添加到窗口中
    listbox.pack(pady=5)
    confirm_btn.pack(side=LEFT, padx=50, pady=10)
    cancel_btn.pack(side=RIGHT, padx=50, pady=10)

    # 让窗口处于屏幕中央
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

    # 运行窗口
    window.mainloop()


def on_confirm(listbox):
    # 获取选中的选项索引
    curselection = listbox.curselection()
    if curselection:
        listbox_get = listbox.get(curselection[0])
        print("You selected index: ", listbox_get)
    else:
        print("You didn't select any option")
        return


# 显示单选框对话框
show_listbox_dialog()
