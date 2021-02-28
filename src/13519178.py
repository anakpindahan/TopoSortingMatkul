# Membaca file yang diberikan dan menjadikannya dalam format yang dapat diselesaikan
def bacaMatkul(inFile):
    inF = open(inFile, 'r')

    # Memuat semua matkul beserta prasyaratnya [[Matkul1,MatkulPrasyarat1...], [Matkul2,MatkulPrasyarat2...] ...]
    listUrutanMatkul = [] 
    
    # Memuat semua matkul yang ada
    listMatkul = [] 
    
    # Memuat semua matkul yang ada beserta berapa banyak prasyrat yang perlu diambil 
    dictMatkul = {}
    
    # Membaca masukan
    for line in inF:
        strLine = line.rstrip('\n.')
        listLine = strLine.split(', ')
        listUrutanMatkul.append(listLine)
        for matkul in listLine:
            if not matkul in listMatkul:
                listMatkul.append(matkul)

    inF.close()
    
    for matkul in listMatkul:
        prereq = 0
        for urutanMatkul in listUrutanMatkul:
            if(matkul in urutanMatkul and matkul == urutanMatkul[0]):
                prereq = len(urutanMatkul) - 1
        dictMatkul[matkul] = prereq
    return listMatkul, listUrutanMatkul, dictMatkul

# Menuliskan matkul yang dapat diambil setiap semesternya
def tulisMatkul(matkulTerurut):
    i = 1
    for matkulSemIni in matkulTerurut:
        print(f'Semester {i}: ', end = '')
        for matkul in matkulSemIni:
            print(matkul, end = ' ')
        print()
        i += 1
            
# Mengurutkan matkul-matkul yang ada
def urutkanMatkul(listMatkul, listUrutanMatkul, dictMatkul, matkulTerurut):
    # Selama masih ada matkul, lanjut
    if(len(listMatkul) > 0):

        # Matkul yang dapat diambil semster ini
        matkulSemIni = []

        # Matkul yang tidak dapat diambil semster ini karena prasyaratnya diambil semester ini
        matkulNanti = []
        
        i = 0
        while i < len(listMatkul):
            # Memilih matkul pertama yang ada di daftar
            matkul = listMatkul[i]

            if(dictMatkul[matkul]== 0 and not matkul in matkulNanti):
                # Jika prasyarat matkul tidak ada/sudah diambil semua, 
                # ambil matkul tersebut dan hapus prasyarat matkul yang  matkul prasyaratnya adalah
                # matkul yang diambil ini
                matkulSemIni.append(matkul)
                hapusMatkulBerprasyarat(matkul, listUrutanMatkul, dictMatkul, matkulNanti)
                listMatkul.remove(matkul)
                del dictMatkul[matkul]
                i -= 1
            i += 1

        matkulTerurut.append(matkulSemIni)

        # Decrease and Conquer

        if(len(matkulSemIni) > 0):
            urutkanMatkul(listMatkul, listUrutanMatkul, dictMatkul, matkulTerurut)
        else:
            print('Situasi ini tidak mungkin. Mohon masukkan dengan benar atau tanyakan ke pihak kampus')

# Menghapus prasyarat matkul-matkul yang matkul prasyaratnya sudah diambil
def hapusMatkulBerprasyarat(matkul, listUrutanMatkul, dictMatkul, matkulNanti):
    j = 0
    while j < len(listUrutanMatkul):
        urutanMatkul = listUrutanMatkul[j]

        # Untuk setiap matkul yang prasyaratnya adalah matkul yang diambil, hapuslah matkul
        # yang sudah diambil tersebut dari daftar matkul yang perlu diambil

        if(matkul in urutanMatkul and matkul == urutanMatkul[0]):
            listUrutanMatkul.remove(urutanMatkul)
            j -= 1
        elif(matkul in urutanMatkul):
            dictMatkul[urutanMatkul[0]] -= 1
            matkulNanti.append(urutanMatkul[0])
            urutanMatkul.remove(matkul)
            j -= 1
        j += 1

# Kode utama
print("Program Sorting Matkul e yokoso~")
while(True):
    print("Silahkan masukkan nama file yang berisi nama matkul yang ingin diurutkan...")
    fileMasukan = input()
    listMatkul, listUrutanMatkul, dictMatkul = bacaMatkul(fileMasukan)
    matkulTerurut = []
    urutkanMatkul(listMatkul, listUrutanMatkul, dictMatkul, matkulTerurut)
    tulisMatkul(matkulTerurut)
    print("Apakah ada lagi matkul yang ingin diurutkan?? (Y/n)")
    yn = input()
    if(yn == 'n' or yn == 'N'):
        break
print("Terima kasih telah mengurutkan matkul bersama kami...")
print("I want to make a pun about sorting algorithms but I need to sort myself out first...")