import tkinter as tk
from tkinter import messagebox

class book:
    def __init__(self, Judul, Jenis, available=True):
        self.Judul = Judul
        self.Jenis = Jenis
        self.available = available

class Ashabooklibrary:
    def __init__(self):
        self.books = []
        self.initialize_book()

    def initialize_book(self):
        book1 = book("Di Tanah Lada", "Fiksi")
        book2 = book("Biologi Kelas X", "Non Fiksi")
        book3 = book("Jakarta Sebelum Pagi", "Fiksi")
        book4 = book("Biography Soekarno", "Non Fiksi")
        book5 = book("Dunia Sophie", "Fiksi")
        self.books = [book1, book2, book3, book4, book5]

    def check_availability(self, Judul, Jenis):
        for book in self.books:
            if book.Judul == Judul and book.Jenis == Jenis:
                return book.available
        return False

    def Pinjam_book(self, Judul, Jenis):
        for book in self.books:
            if book.Judul == Judul and book.Jenis == Jenis and book.available:
                book.available = False
                return True
        return False

    def Pengembalian_book(self, Judul, Jenis):
        for book in self.books:
            if book.Judul == Judul and book.Jenis == Jenis and not book.available:
                book.available = True
                return True
        return False

class AshaBookLibraryGUI:
    def __init__(self, Asha_book_library):
        self.Asha_book_library = Asha_book_library
        self.window = tk.Tk()
        self.window.title("ASHA'S LIBRARY")

        self.make_label = tk.Label(self.window, text="Judul:")
        self.make_label.pack()
        self.make_entry = tk.Entry(self.window)
        self.make_entry.pack()

        self.model_label = tk.Label(self.window, text="Jenis:")
        self.model_label.pack()
        self.model_entry = tk.Entry(self.window)
        self.model_entry.pack()

        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack()

        self.rent_button = tk.Button(self.window, text="Peminjaman Buku", command=self.pinjam_book)
        self.rent_button.pack()

        self.return_button = tk.Button(self.window, text="Pengembalian Buku", command=self.pengembalian_book)
        self.return_button.pack()

        self.book_details = tk.Text(self.window, width=40, height=30)
        self.book_details.pack()

    def display_book_details(self):
        self.book_details.delete("1.0", tk.END)
        for book in self.Asha_book_library.books:
            self.book_details.insert(tk.END, f"Judul: {book.Judul}\n")
            self.book_details.insert(tk.END, f"Jenis: {book.Jenis}\n")
            self.book_details.insert(tk.END, f"Status: {'Tersedia' if book.available else 'Dipinjam'}\n")
            self.book_details.insert(tk.END, "-" * 20 + "\n")

    def pinjam_book(self):
        Judul = self.make_entry.get()
        Jenis = self.model_entry.get()
        if self.Asha_book_library.Pinjam_book(Judul, Jenis):
            messagebox.showinfo("Peminjaman Buku", "Buku berhasil terdata dan terpinjam!")
        else:
            messagebox.showerror("Peminjaman Buku", "Mohon maaf, buku tidak tersedia.")
        self.display_book_details()

    def pengembalian_book(self):
        Judul = self.make_entry.get()
        Jenis = self.model_entry.get()
        if self.Asha_book_library.Pengembalian_book(Judul, Jenis):
            messagebox.showinfo("Pengembalian Buku", "Terima kasih! Buku berhasil dikembalikan.")
        else:
            messagebox.showwarning("Pengembalian Buku", "Buku sudah dikembalikan.")
        self.display_book_details()

    def run(self):
        self.display_book_details()
        self.window.mainloop()

# Main program
asha_book_library = Ashabooklibrary()
gui = AshaBookLibraryGUI(asha_book_library)
gui.run()
