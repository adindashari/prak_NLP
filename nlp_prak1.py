import re

String = "Pemrosesan Bahasa Alami merupakan matakuliah pilihan di Jurusan Teknik Informatika yang"\
      "dapat diprogram mahasiswa semester 6. Peserta matakuliah Pemrosesan Bahasa Alami sesuai"\
      "yang terdapat pada siakadu terdaftar dengan email :"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "abastian.18027@mhs.unesa.ac.id, adinda.20118@mhs.unesa.ac.id, khusnul.20117@mhs.unesa.ac.id ,tony.20116@mhs.unesa.ac.id,"\
      "Dosen Pengampu matakuliah : Anita Qoiriah (anitaqoiriah@unesa.ac.id)"\
      "dan Naim Rochmawati (naimrochmawati@unesa.ac.id)"
#print( re.sub(emailPattern, '*', txt) )

Nama = "Someone"
NIM = "N/A"
NIMleft = "N/A"
NIMright = "N/A"

searchEmail = re.compile(r'[a-z]+[.]\d{5}[@][h-s]+[.][a-z]+[.][a-c]+[.][d-i]+')
emailResult = searchEmail.findall(String)

searchName = re.compile(r'[a-z]+')
searchNim = re.compile(r'\d+')

print(String)
print("")

for i in range (len(emailResult)):
    Nama = searchName.search(emailResult[i])
    NIM = searchNim.search(emailResult[i])
    NIMleft = NIM.group()[0:2]
    NIMright = NIM.group()[2:5]
    NIM = NIMleft + "051204" + NIMright
    print(str(i + 1) + "Nama :" + Nama.group().capitalize() + " - NIM : " + NIM + "Email : " + emailResult[i])