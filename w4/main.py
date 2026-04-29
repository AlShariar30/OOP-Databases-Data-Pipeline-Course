from tkinter import Tk, Toplevel, ttk


class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading = ttk.Label(master=self._root, text="W4 App")

        matrix_button = ttk.Button(
            master=self._root,
            text="Matrix Calculator",
            command=self._open_matrix
        )

        data_button = ttk.Button(
            master=self._root,
            text="Data Analysis",
            command=self._open_data_analysis
        )

        heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        matrix_button.grid(row=1, column=0, padx=10, pady=10)
        data_button.grid(row=1, column=1, padx=10, pady=10)

    def _open_matrix(self):
        matrix_window = Toplevel(self._root)
        matrix_window.title("Matrix Calculator")

        label_a = ttk.Label(master=matrix_window, text="Matrix A")
        label_a.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.a1 = ttk.Entry(master=matrix_window, width=5)
        self.a2 = ttk.Entry(master=matrix_window, width=5)
        self.a3 = ttk.Entry(master=matrix_window, width=5)
        self.a4 = ttk.Entry(master=matrix_window, width=5)

        self.a1.grid(row=1, column=0, padx=5, pady=5)
        self.a2.grid(row=1, column=1, padx=5, pady=5)
        self.a3.grid(row=2, column=0, padx=5, pady=5)
        self.a4.grid(row=2, column=1, padx=5, pady=5)

        label_b = ttk.Label(master=matrix_window, text="Matrix B")
        label_b.grid(row=0, column=3, columnspan=2, padx=5, pady=5)

        self.b1 = ttk.Entry(master=matrix_window, width=5)
        self.b2 = ttk.Entry(master=matrix_window, width=5)
        self.b3 = ttk.Entry(master=matrix_window, width=5)
        self.b4 = ttk.Entry(master=matrix_window, width=5)

        self.b1.grid(row=1, column=3, padx=5, pady=5)
        self.b2.grid(row=1, column=4, padx=5, pady=5)
        self.b3.grid(row=2, column=3, padx=5, pady=5)
        self.b4.grid(row=2, column=4, padx=5, pady=5)

        add_button = ttk.Button(
            master=matrix_window,
            text="Add",
            command=self._add_matrices
        )
        add_button.grid(row=3, column=0, padx=5, pady=10)

        subtract_button = ttk.Button(
            master=matrix_window,
            text="Subtract",
            command=self._subtract_matrices
        )
        subtract_button.grid(row=3, column=1, columnspan=2, padx=5, pady=10)

        multiply_button = ttk.Button(
            master=matrix_window,
            text="Multiply",
            command=self._multiply_matrices
        )
        multiply_button.grid(row=3, column=3, columnspan=2, padx=5, pady=10)

        self.result_label = ttk.Label(master=matrix_window, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=5, padx=5, pady=10)

    def _get_matrix_values(self):
        a11 = int(self.a1.get())
        a12 = int(self.a2.get())
        a21 = int(self.a3.get())
        a22 = int(self.a4.get())

        b11 = int(self.b1.get())
        b12 = int(self.b2.get())
        b21 = int(self.b3.get())
        b22 = int(self.b4.get())

        return a11, a12, a21, a22, b11, b12, b21, b22

    def _add_matrices(self):
        a11, a12, a21, a22, b11, b12, b21, b22 = self._get_matrix_values()

        r11 = a11 + b11
        r12 = a12 + b12
        r21 = a21 + b21
        r22 = a22 + b22

        self.result_label.config(text=f"Result: [[{r11}, {r12}], [{r21}, {r22}]]")

    def _subtract_matrices(self):
        a11, a12, a21, a22, b11, b12, b21, b22 = self._get_matrix_values()

        r11 = a11 - b11
        r12 = a12 - b12
        r21 = a21 - b21
        r22 = a22 - b22

        self.result_label.config(text=f"Result: [[{r11}, {r12}], [{r21}, {r22}]]")

    def _multiply_matrices(self):
        a11, a12, a21, a22, b11, b12, b21, b22 = self._get_matrix_values()

        r11 = (a11 * b11) + (a12 * b21)
        r12 = (a11 * b12) + (a12 * b22)
        r21 = (a21 * b11) + (a22 * b21)
        r22 = (a21 * b12) + (a22 * b22)

        self.result_label.config(text=f"Result: [[{r11}, {r12}], [{r21}, {r22}]]")

    def _open_data_analysis(self):
        data_window = Toplevel(self._root)
        data_window.title("Data Analysis")
        label = ttk.Label(master=data_window, text="Data Analysis View")
        label.pack(padx=20, pady=20)


window = Tk()
window.title("W4 App")

ui = UI(window)
ui.start()

window.mainloop()