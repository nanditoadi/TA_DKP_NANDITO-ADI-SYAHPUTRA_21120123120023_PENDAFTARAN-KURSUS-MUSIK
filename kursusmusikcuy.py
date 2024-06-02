import tkinter as tk
from tkinter import font as tkfont, ttk
from tkcalendar import Calendar
import datetime

# MODUL 1 : VARIABEL, TIPE DATA, DAN  ARRAY
# MODUL 2 : PENGKONDISIAN
# MODUL 3 : PERULANGAN                                                                   
# MODUL 4 : FUNCTION DAN METHOD
# MODUL 5 : OOP 1 
# MODUL 8 : GUI

class MusicCourseRegistrationApp: 
    def __init__(self, master):
        # Setup window utama
        self.master = master
        self.master.title("Pendaftaran Kursus Musik")
        self.master.state('zoomed')
        
        #background
        self.background_image = tk.PhotoImage(file= "background kursus 1.png")
        background_label = tk.Label(self.master, image=self.background_image)
        background_label.place(x=0.1, y=0.1, relwidth=1, relheight=1)

        # Setup font
        self.font_style = tkfont.Font(family="Calibri", size=14)
        self.title_font = tkfont.Font(family="Calibri", size=30, weight="bold")
        self.label_font = tkfont.Font(family="Calibri", size=16)
        self.entry_font = tkfont.Font(family="Calibri", size=14)
        self.button_font = tkfont.Font(family="Calibri", size=14, weight="bold")
        
         # Harga kursus
        self.prices = { 
            "Gitar": {                     
                "4x/Bulan(SENIN)": "Rp.300.000",
                "8x/Bulan(SENIN-SELASA)": "Rp.600.000",
                "12x/Bulan(SENIN-RABU)": "Rp.900.000",
                "16x/Bulan(SENIN-KAMIS)": "Rp.1.200.000",
                "20x/Bulan(SENIN-JUMAT)": "Rp.1.500.000"
            },
            "Piano": {
                "4x/Bulan(SENIN)": "Rp.400.000",
                "8x/Bulan(SENIN-SELASA)": "Rp.700.000",
                "12x/Bulan(SENIN-RABU)": "Rp.1.000.000",
                "16x/Bulan(SENIN-KAMIS)": "Rp.1.300.000",
                "20x/Bulan(SENIN-JUMAT)": "Rp.1.600.000"
            },
            "Vocal": {
                "4x/Bulan(SENIN)": "Rp.200.000",
                "8x/Bulan(SENIN-SELASA)": "Rp.500.000",
                "12x/Bulan(SENIN-RABU)": "Rp.800.000",
                "16x/Bulan(SENIN-KAMIS)": "Rp.1.100.000",
                "20x/Bulan(SENIN-JUMAT)": "Rp.1.400.000"
            }
        }

        # Membuat komponen GUI
        self.create_widgets() 

    def create_widgets(self): 

        # Label judul
        title_label = tk.Label(self.master, text="Kursus Musik Cuy", font=self.title_font, bg='#f7f5dd')
        title_label.pack(pady=(10, 5), fill='x')
        
        # Frame tengah untuk menampung frame utama dan frame struk
        center_frame = tk.Frame(self.master, bg='#f7f5dd', padx=0.5, pady=0.5)
        center_frame.place(relx=0.5, rely=0.1, anchor='n')

        # Frame utama untuk field input
        main_frame = tk.Frame(center_frame, bg='#f7f5dd', padx=20, pady=20)
        main_frame.pack(side='left', padx=25, pady=10)

        # Frame struk untuk menampilkan ringkasan pendaftaran
        receipt_frame = tk.Frame(center_frame, bg='#f7f5dd', padx=20, pady=20)
        receipt_frame.pack(side='right', padx=25, pady=10, fill='both', expand=True)
        self.receipt_text = tk.Text(receipt_frame, font=self.label_font, bg='#E6DFD0', height=15, width=50)
        self.receipt_text.pack(expand=True, fill='both')
        self.receipt_text.config(state='disabled') 


        # Label dan field input
        labels = ["Nama:", "Usia:", "Pilih Kursus:", "Durasi Kursus (1 jam):", "Tanggal Mulai:", "Jam:", "Nomor Telepon:"] 
        for i, text in enumerate(labels):  
            label = tk.Label(main_frame, text=text, font=self.label_font, bg='#f7f5dd') 
            label.grid(row=i, column=0, sticky="w", padx=5, pady=5) 

            if text == "Nama:":                      
                entry = tk.Entry(main_frame, font=self.entry_font)
                self.name_entry = entry
            elif text == "Usia:": 
                entry = tk.Entry(main_frame, font=self.entry_font)
                self.age_entry = entry
            elif text == "Pilih Kursus:":
                self.course_var = tk.StringVar(self.master)
                entry = tk.OptionMenu(main_frame, self.course_var, *self.prices.keys())
                entry.config(font=self.entry_font)
                self.course_var.trace("w", self.update_duration_dropdown)
            elif text == "Durasi Kursus (1 jam):":
                self.duration_var = tk.StringVar(self.master)
                entry = ttk.Combobox(main_frame, textvariable=self.duration_var, font=self.entry_font, state="readonly")
                self.duration_dropdown = entry
            elif text == "Tanggal Mulai:":
                entry = tk.Button(main_frame, text="Pilih Tanggal", command=self.choose_date, font=self.button_font, bg='#5A4339', fg='white')
                self.start_date_button = entry
            elif text == "Jam:":
                self.time_var = tk.StringVar(self.master)
                entry = ttk.Combobox(main_frame, textvariable=self.time_var, font=self.entry_font, state="readonly")
                entry['values'] = [f"{hour:02d}:00" for hour in range(15, 22)]
                self.time_dropdown = entry
            elif text == "Nomor Telepon:":
                entry = tk.Entry(main_frame, font=self.entry_font)
                self.phone_entry = entry
            if entry:
                entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        # Pesan error dan tombol daftar
        self.error_text = tk.Text(main_frame, height=2, width=50, fg='red')
        self.register_button = tk.Button(main_frame, text="Daftar", command=self.register, font=self.button_font, bg='#5A4339', fg='white')
        self.register_button.grid(row=len(labels)+2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
        self.error_text.grid(row=len(labels)+3, column=0, columnspan=2, sticky="ew")
        self.error_text.config(state='disabled') 

    def choose_date(self): 

        # Membuat dialog kalender untuk memilih tanggal
        top = tk.Toplevel(self.master)
        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        cal.pack(fill="both", expand=True)
        tk.Button(top, text="Ok", command=lambda: self.set_date(cal.selection_get(), top)).pack()
        

    def set_date(self, date, top): 
    
        # Mengatur tanggal yang dipilih pada tombol
        self.start_date_button.config(text=date.strftime("%d-%m-%Y"))
        top.destroy()

    def update_duration_dropdown(self, *args): 
        # Memperbarui opsi durasi berdasarkan kursus yang dipilih
        course = self.course_var.get()
        if (course in self.prices):
            durations = [f"{duration} - {price}" for duration, price in self.prices[course].items()]
            self.duration_dropdown['values'] = durations
            if durations:
                self.duration_dropdown.set(durations[0])

    def register(self): 
        # Mengambil nilai dari form
        name = self.name_entry.get()                        
        age = self.age_entry.get()
        course_name = self.course_var.get()
        start_date_text = self.start_date_button.cget("text")
        time = self.time_var.get() 
        phone_number = self.phone_entry.get()
        duration_price = self.duration_var.get()

        # Menghapus pesan error sebelumnya
        self.error_text.config(state='normal')
        self.error_text.delete(1.0, tk.END)

        # Validasi input
        if not name or not age or not phone_number:
            self.error_text.insert(tk.END, "Error: Harap lengkapi semua kolom.")
            self.error_text.config(state='disabled')
            return

        try:
            start_date = datetime.datetime.strptime(start_date_text, "%d-%m-%Y").date()
            if start_date < datetime.date.today():
                self.error_text.insert(tk.END, "Error: Tanggal sudah kedaluwarsa.")
                self.error_text.config(state='disabled')
                return
            
        except ValueError:
            self.error_text.insert(tk.END, "Error: Format tanggal tidak valid.")
            self.error_text.config(state='disabled')
            return

        self.error_text.config(state='disabled') 
        duration, price = duration_price.split(" - ") 
        self.show_receipt_window(name, age, course_name, duration, start_date_text, time, phone_number, price)

    def show_receipt_window(self, name, age, course_name, duration, start_date, time, phone_number, price): 

        # Menampilkan struk pendaftaran
        self.receipt_text.config(state='normal')
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, "================= STRUK PENDAFTARAN =============\n")
        self.receipt_text.insert(tk.END, f"Nama : {name}\n")
        self.receipt_text.insert(tk.END, f"Usia : {age}\n")
        self.receipt_text.insert(tk.END, f"Kursus : {course_name}\n")
        self.receipt_text.insert(tk.END, f"Durasi : {duration}\n")
        self.receipt_text.insert(tk.END, f"Mulai : {start_date} {time}\n")
        self.receipt_text.insert(tk.END, f"Nomor Telepon : {phone_number}\n")
        self.receipt_text.insert(tk.END, f"Harga : {price}\n")
        self.receipt_text.insert(tk.END, "=====Terima kasih, Kami akan segera menghubungi Anda!====\n")
        self.receipt_text.config(state='disabled') 


if __name__ == "__main__": 
    root = tk.Tk()
    app = MusicCourseRegistrationApp(root)
    root.mainloop()