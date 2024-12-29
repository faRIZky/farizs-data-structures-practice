'''
slicing python
how to manage and manipulates strings

start : stop : step

for example:

non-reverse: start : stop : step (same)
reverse: display from last : delete : -1

or buat reverse biar enak:
Starts at index 7, stops before index 4, and steps backward.

full:
4321olleh

start at 7 backwards --> "321olleh"
stop at 4 backwards --> do not continue "olleh"
and the result will be --> 321


ORR LEBIH ENAK LAGI KALO BUAT REVERSE YAA BISA AJA START : STOP : STEP
intinya kalo slicing with negative step index, maka pointer akan dari KANAN ke KIRI. lebih makes sense sih ini

YEAY!!

w3school:
mulai (opsional): Indeks untuk memulai irisan (inklusif). Nilai default adalah 0 jika dihilangkan.
akhir (opsional): Indeks untuk mengakhiri irisan (eksklusif). Defaultnya adalah panjang daftar jika dihilangkan.
langkah (opsional): Ukuran langkah, menentukan interval antar elemen. Nilai default adalah 1 jika dihilangkan

'''

text = "hello1234"

# print from index 0 and stop at index 2 explicitly
print(text[0:2])        # --> "he"
print(text[0:2:1])      # --> if you dont specify yaa... tetep 1 secara default. yaa stepnya pasti 1
# print(text[0:2:0])    # slice step cannot be zero!

print(text[0:-1])       # --> "hello123" 4 nya ga ikut


# print from index 0 to 4 and step 1 alphabet
print(text[0:4:2]) # hell

# how to reverse then? yaa tinggal mulai dari 0 sampe ujung dengan stepnya -1 (backwards)
print("trying reverse 1 : " + text[3::-1])                      #--> yaa intinya dibalik dulu wicis jadi 4321olleh --> terus didisplay dari 3 index kebelakang (TERMASUK index 3) --> "lleh"
print("trying reverse 1.1 : " + text[7:4:-1])
print("trying reverse 2 : " + text[1:5:1] + text[7:4:-1])       # soal: coba gimana mau ambil "ello321" --> ello + 321

'''
notes: 
hello1234 
4321olleh 
'''
