import tkinter as tk            #Mengimpor library tkinter untuk membuat antarmuka grafis
from tkinter import messagebox  #Untuk menampilkan kotak pesan error

def hasil_prediksi():           #Mendefinisikan fungsi untuk memproses prediksi berdasarkan input nilai
    try:
        for entry in entries:               #Loop untuk memeriksa setiap input nilai
            nilai = int(entry.get())        #Mengambil nilai dari input entry dan mengubah jadi integer
            if not (0 <= nilai <= 100):     #Mengecek apakah nilai berada di antara 0 dan 100
                raise ValueError("Nilai harus antara 0 dan 100.")           #Jika tidak, error
            hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  #Menampilkan hasil prediksi jika input valid
    except ValueError as ve:                #Error jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")  #Menampilkan pesan error jika input tidak valid
        
root = tk.Tk()                                 #Membuat objek root
root.title("Aplikasi Prediksi Prodi Pilihan")  #Menetapkan judul untuk jendela utama
root.geometry("500x600")                       #Menetapkan ukuran jendela (lebar 500px dan tinggi 600px)
root.configure(bg="#f0f0f0")                   #Mengatur warna background jendela utama

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 12))  #Membuat label judul aplikasi
judul_label.pack(pady=20)                      #Menempatkan label judul di jendela dengan jarak atas dan bawah 20px

frame_input = tk.Frame(root, bg="#f0f0f0")     #Membuat frame untuk tempat input
frame_input.pack(pady=10)                      #Menempatkan frame di jendela dengan jarak atas dan bawah 10px

entries = []         #Membuat list kosong untuk menyimpan input nilai
for i in range(10):  #Loop untuk membuat 10 input nilai
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12))  #Membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")        #Menempatkan label dalam grid di kolom 0
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))     #Membuat entry untuk input nilai
    entry.grid(row=i, column=1, padx=10, pady=5)                    #Menempatkan entry dalam grid di kolom 1
    entries.append(entry)                                           #Menambahkan entry ke dalam list entries

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  #Membuat tombol untuk memprediksi prodi
prediksi_button.pack(pady=30)       #Menempatkan tombol di jendela dengan jarak atas dan bawah 30px

hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue")  #Membuat label untuk menampilkan hasil prediksi
hasil_label.pack(pady=20)  #Menempatkan label hasil prediksi di jendela dengan jarak atas dan bawah 20px

root.mainloop()  #Memulai aplikasi dan menjalankan loop untuk interaksi pengguna