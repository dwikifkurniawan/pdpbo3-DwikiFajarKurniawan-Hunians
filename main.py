from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from tkinter import messagebox

hunians = []
# hunians.append(Apartemen("Saul Goodman", 3, 3))
# hunians.append(Rumah("Gustavo Fring", 5, 2))
# hunians.append(Indekos("Chuck McGill", "Howard Hamlin"))
# hunians.append(Rumah("Mike Ehrmantraut", 1, 4))

root = Tk()
root.title("TP3 DPBO Dwiki Fajar Kurniawan")

def submit(jns, pemilik, nama_penghuni, jml_penghuni, jml_kamar):
    if jns == 1:
        hunians.append(Apartemen(pemilik, jml_penghuni, jml_kamar))
    elif jns == 2:
        hunians.append(Indekos(pemilik, nama_penghuni))
    elif jns == 3:
        hunians.append(Rumah(pemilik, jml_penghuni, jml_kamar))

    messagebox.showinfo("popup", "Data telah tersimpan")


def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary3 = Label(d_frame, text="Nama Pemilik: " + hunians[index].get_nama_pemilik(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary2 = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=2, column=0, sticky="w")
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=1, column=0, sticky="w") 
    
    b_exit = Button(d_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=3, column=0)


def about():
    top = Toplevel()
    top.title("About Hunians")

    a_frame = LabelFrame(top, text="About", padx=10, pady=10)
    a_frame.pack(padx=10, pady=10)

    Label(a_frame, text="Hunians adalah aplikasi untuk mengolah data residen", anchor="w").grid(row=0, column=0, sticky="w")
    Label(a_frame, text="NIM : 1903761", anchor="w").grid(row=1, column=0, sticky="w")
    Label(a_frame, text="Nama: Dwiki Fajar Kurniawan", anchor="w").grid(row=2, column=0, sticky="w")
    Label(a_frame, text="Kelas: Ilmu Komputer C1 2019", anchor="w").grid(row=3, column=0, sticky="w")

    b_exit = Button(a_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=4, column=0)


def show():
    top = Toplevel()
    top.title("Data Dwiki")

    s_frame = LabelFrame(top, text="Data Seluruh Residen", padx=10, pady=10)
    s_frame.pack(padx=10, pady=10)

    for index, h in enumerate(hunians):
        idx = Label(s_frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(s_frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(s_frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(s_frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(s_frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    b_exit = Button(s_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=index+1, column=0)


def clear():
    response = messagebox.askyesno("?", "Apakah anda yakin ingin Menghapus Semua Data?")
    if response == 1:
        hunians.clear()
        messagebox.showinfo("popup", "Penghapusan data berhasil")
    


def popup():
    response = messagebox.askyesno("?", "Apakah anda yakin ingin keluar?")
    if response == 1:
        root.destroy()


# frame, label dan button
frame = LabelFrame(root, text="Input", padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, text="Application", padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

label1 = Label(frame2, text="HUNIANS")
label1.config(font=("Calibri", 20))
label1.grid(row=0)

label2 = Label(frame2, text="Hunians adalah aplikasi untuk mengolah data residen")
label2.config(font=("Calibri", 12))
label2.grid(row=1)

b_add = Button(frame, text="Submit", command=lambda: submit(r.get(), pemilik.get(), nama_penghuni.get(), jml_penghuni.get(), jml_kamar.get()), width=15)
b_add.grid(row=6)

b_show = Button(frame2, text="See All Submissions", command=show, width=20)
b_show.grid(row=6, column=0, pady=5)

b_del = Button(frame2, text="Clear Submissions", command=clear, width=20)
b_del.grid(row=7, column=0, pady=5)

b_exit = Button(frame2, text="Exit", command=popup, width=20)
b_exit.grid(row=10, column=0, pady=5)

b_about = Button(frame2, text="About", command=about, width=20)
b_about.grid(row=8, column=0, pady=5)


# label
Label(frame, text="Jenis Hunian :", anchor="w").grid(row=0, column=0, sticky="w")
Label(frame, text="Nama Pemilik :", anchor="w").grid(row=1, column=0, sticky="w")
Label(frame, text="Nama Penghuni :", anchor="w").grid(row=2, column=0, sticky="w")
Label(frame, text="Jumlah Penghuni :", anchor="w").grid(row=3, column=0, sticky="w")
Label(frame, text="Jumlah Kamar :", anchor="w").grid(row=4, column=0, sticky="w")

# radiobutton
r = IntVar()
Radiobutton(frame, text="Appartemen", variable=r, value=1).grid(row=0, column=1)
Radiobutton(frame, text="Indekos", variable=r, value=2).grid(row=0, column=2)
Radiobutton(frame, text="Rumah", variable=r, value=3).grid(row=0, column=3)

# input fields
pemilik = Entry(frame, width=30)
pemilik.grid(row=1, column=1, pady=5)

nama_penghuni = Entry(frame, width=30)
nama_penghuni.grid(row=2, column=1, pady=5)

jml_penghuni = Entry(frame, width=30)
jml_penghuni.grid(row=3, column=1, pady=5)

jml_kamar = Entry(frame, width=30)
jml_kamar.grid(row=4, column=1, pady=5)

root.mainloop()