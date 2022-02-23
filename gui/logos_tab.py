from tkinter import Button, Frame, Toplevel

class LogosTab(Frame):
    def __init__(self, master, option_file, w, h, appname):
        super().__init__(master,width=w,height=h)
        self.of = option_file
        self.appname = appname
        fila = 0
        columna = 0
        for i in range(len(self.of.logos_tk)):
            if columna > 9:
                columna= 0
                fila += 1
            newButton = Button(self, image=self.of.logos_tk[i], width=54, height=54, command=lambda i=i:self.on_click(i))
            newButton.grid(column=columna, row=fila)
            columna += 1

    def on_click(self,i):
        self.window = Toplevel(self)
        self.export_btn = Button(self.window, text="Export as PNG", command=self.write_png(self.of.logos_png[i].png))
        self.export_btn.pack()

    def write_png(self,img_bytes):
        with open("test.png",'wb') as img:
            img.write(img_bytes)

    def publish(self):
        pass
