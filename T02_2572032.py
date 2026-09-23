## Definisi Kelas ##
## Definisi Kelas ADTArray
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032
## Definisi Atribut:
# Nmax  : kapasitas maksimum array data (integer)
# items : array/list untuk menyimpan elemen 
#         data bertipe integer (array of integer)
# N     : banyaknya elemen dalam array yang 
#           sudah terisi (integer)
class ADTArray:
    def __init__(self, size):
        self.Nmax = size
        self.items = [None] * size
        self.N = 0
    def isFull(self):
        return self.N == self.Nmax
    def isEmpty(self):
        return self.N == 0
    def addArray(self):
        NN = int(input("Masukkan berapa angka yang akan di input: "))
        while NN > self.Nmax or NN <= 0:
            print("Input tidak valid, silahkan input ulang")
            NN = int(input("Masukkan berapa angka yang akan di input: "))

        for i in range(NN):
            self.items[i] = int(input(f"Masukkan nilai-{i+1}: "))
        self.N = NN
    def printArray(self):
        if self.isEmpty():
            print("Tabel masih kosong")
        else:
            out_str = ""
            for i in range(self.N):
                if i == 0:
                    out_str += str(self.items[i])
                elif i == self.N - 1:
                    out_str += f", dan {self.items[i]}"
                else:
                    out_str += f", {self.items[i]}"
            print(out_str)
    def search(self, X):
        for i in range(self.N):
            if self.items[i] == X:
                return i
        return -1
    def addElFirst(self, X):
        if self.search(X) != -1:
            print("Data sudah ada!")
            self.printArray()
            return
        if self.isFull():
            print("Data Sudah Penuh")
            return
        for i in range(self.N, 0, -1):
            self.items[i] = self.items[i - 1]
        self.items[0] = X
        self.N += 1
        self.printArray()
    def delete(self, X):
        posisi = self.search(X)
        if posisi == -1:
            print("Data tidak ditemukan")
            return
        for i in range(posisi, self.N - 1):
            self.items[i] = self.items[i + 1]  
        self.items[self.N - 1] = None
        self.N -= 1
    def inverse(self):
        left = 0
        right = self.N - 1
        while left < right:
            self.items[left], self.items[right] = self.items[right], self.items[left]
            left += 1
            right -= 1
# Kamus Data (Main Program):
#   x          : objek instance dari kelas 
#                ADTArray dengan kapasitas 
#                10 (ADTArray)
#   cari       : nilai integer yang ingin 
#               dicari posisinya di dalam 
#               array (integer)
#   tambahData : nilai integer baru yang 
#               akan ditambahkan ke awal 
#               array (integer)
#   hapusData  : nilai integer yang ingin 
#               dihapus dari array (integer)
def main():
    x = ADTArray(10)
    x.addArray()
    x.printArray()
    cari = int(input("Masukkan angka yang ingin dicari: "))
    pos = x.search(cari)
    if pos < 0:
        print("Data tidak ditemukan")
    else:
        print(f"Data {cari} ditemukan pada index ke-{pos}.")
    while not x.isFull():
        tambahData = int(input("Masukkan angka baru untuk ditambahkan: "))
        x.addElFirst(tambahData)
        if x.isFull():
            break
    hapusData = int(input("Masukkan angka yang ingin dihapus: "))
    x.delete(hapusData)
    x.printArray()
    print("Inverse array:")
    x.inverse()
    x.printArray()
if __name__ == '__main__':
    main()