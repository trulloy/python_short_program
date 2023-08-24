import tkinter as tk
#import webbrowser

from tkinter import Canvas


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("shapes App")
        bg_color = "black"  # Hex color code for dark gray
        self.root.configure(bg=bg_color)
        
        # Set initial geometry (widthxheight+X+Y)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Calculate the x and y coordinates for centering the window
        x_coordinate = (screen_width - 1100) // 2
        y_coordinate = (screen_height - 550) // 2
        # Set initial geometry and position the window
        self.root.geometry(f"1100x550+{x_coordinate}+{y_coordinate}")
        self.root.resizable(False,False)
        
        can1 = Canvas(width=100, height=100, bg="black", highlightthickness=0)
        can1.place(x=0,y=0)
        shape1={'bounds': [0, 100, 0, 0, 100, 0], 'kind': 'tri', 'fill': True}
        can1.create_polygon(list(shape1.values())[0],fill='green',outline='black')

        can3 = Canvas(width=100, height=100, bg="black", highlightthickness=0)
        can3.place(x=0,y=446)
        shape3={'bounds': [0, 0, 100, 100, 0, 100], 'kind': 'tri', 'fill': True}
        can3.create_polygon(list(shape3.values())[0],fill='green',outline='black')
        
        can2 = Canvas(width=100, height=100,bg="black", highlightthickness=0)
        can2.place(x=996,y=0)
        shape2={'bounds': [100,100, 0,0, 100,0], 'kind': 'tri', 'fill': True}
        can2.create_polygon(list(shape2.values())[0],fill='green',outline='black')
        
        can4 = Canvas(width=100, height=100, bg="black", highlightthickness=0)
        can4.place(x=996,y=446)
        shape4={'bounds': [100, 0, 100, 100, 0, 100], 'kind': 'tri', 'fill': True}
        can4.create_polygon(list(shape4.values())[0],fill='green',outline='black')
        #webbrowser.open("https://www.trulloy.com/")
        

def main():
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
