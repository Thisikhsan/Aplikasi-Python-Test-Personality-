print("===============================================================================================================")
print("....................................<<<< WELCOME TO MY PROGRAM >>>>............................................")
print()
print("------------------------------------<<<< QUIZ TEST KEPRIBADIAN >>>>--------------------------------------------")
print()
print("..................................>>>> INTROVERT ATAU EKSTROVERT <<<<..........................................")
print("\U0001F610   "*24)
print("===============================================================================================================")
print(" Test ini dirancang untuk mengetahui tipe kepribadianmu dan membuatmu paham akan kekuranganmu dan kelebihanmu ")
print("===============================================================================================================")
nama = str(input(" Nama             :"))
kelamin = str(input(" Jenis kelamin    :"))
tanggal = input(" Tanggal lahir    :")
umurku = int(input(" Umur             :"))
score = 0
intro = 0
ekstro = 0
print("===============================================================================================================")
print(" Pilihan jawaban hanya terdapat 2 opsi\t\t Y/y = YES\t\t N/n = NO\t\t Silahkan diisi sesuai pilihanmu")
print("===============================================================================================================")
# Introvert
while True:
    answer1 = input("1. Saya lebih suka percakapan di circle pertemanan yang kecil dengan sedikit orang saja "
                    "\n   dibandingkan circle pertemanan yang besar dengan banyak orang\n  Y/N :")
    if answer1 == "Y" or answer1 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer1 == "N" or answer1 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba Lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer2 = input("2. Bertemu dengan orang banyak dan aktivitas sosial membuatmu selalu bersemangat\n  Y/N :")
    if answer2 == "Y" or answer2 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer2 == "N" or answer2 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer3 = input("3. Menemukan dan mengembangkan ide dengan cara berdiam diri di kesuyian\n  Y/N :")
    if answer3 == "Y" or answer3 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer3 == "N" or answer3 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer4 = input("4. Energi saya terisi jika bertemu dengan sekumpulan teman dengan waktu yang lama \n  Y/N :")
    if answer4 == "Y" or answer4 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer4 == "N" or answer4 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer5 = input("5. Saya tidak suka berbasa-basi, tetapi saya senang berbicara tentang"
                    " topik yang mendalam \n  Y/N :")
    if answer5 == "Y" or answer5 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer5 == "N" or answer5 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer6 = input("6. Saya lebih suka menikmati akhir pekan dengan berkumpul bersama sahabat \n  Y/N :")
    if answer6 == "Y" or answer6 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer6 == "N" or answer6 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer7 = input("7. Orang lain menganggap saya sebagai pendengar yang baik \n  Y/N :")
    if answer7 == "Y" or answer7 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer7 == "N" or answer7 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer8 = input("8. Saya suka jika menjadi pusat perhatian orang banyak di sekitar   \n  Y/N :")
    if answer8 == "Y" or answer8 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer8 == "N" or answer8 == "n":
      score += 1
      intro += 1
      print("--------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer9 = input("9. Saya lebih suka pesta ulangtahun kecil dengan sedikit orang atau anggota"
                    " keluarga saja\n  Y/N :")
    if answer9 == "Y" or answer9 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer9 == "N" or answer9 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer10 = input("10. Saya suka berkumpul dengan teman-teman walaupun tidak tau apa yang akan dibicarakan\n  Y/N :")
    if answer10 == "Y" or answer10 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer10 == "N" or answer10 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer11 = input("11. Energi saya cukup terkuras setelah melakukan interaksi sosial dengan orang banyak \n  Y/N :")
    if answer11 == "Y" or answer11 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer11 == "N" or answer11 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer12 = input("12. Saya bisa berkonsentrasi dengan mudah walaupun di tempat keramaian \n  Y/N :")
    if answer12 == "Y" or answer12 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer12 == "N" or answer12 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer13 = input("13. Saya cukup kesulitan berinteraksi dengan lingkungan baru yang asing bagi saya \n  Y/N :")
    if answer13 == "Y" or answer13 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer13 == "N" or answer13 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer14 = input("14. Orang lain menganggap saya sebagai seseorang yang ceria dan suka banyak bicara \n  Y/N :")
    if answer14 == "Y" or answer14 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer14 == "N" or answer14 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer15 = input("15. Saya cenderung orang yang terjadwal dan selalu berpikir cukup lama dalam mengambil keputusan"
                     "\n    karena berdebat dengan diri sendiri dan tidak bisa menerima perubahan dengan cepat "
                     " \n  Y/N :")
    if answer15 == "Y" or answer15 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer15 == "N" or answer15 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer16 = input("16. Saya suka pekerjaan yang memungkinkan untuk berinteraksi sosial dengan orang banyak\n  Y/N :")
    if answer16 == "Y" or answer16 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer16 == "N" or answer16 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer17 = input("17. Saya memiliki pendirian sendiri dalam diri saya dan tidak mudah dipengaruhi"
                     " oleh orang lain \n  Y/N :")
    if answer17 == "Y" or answer17 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer17 == "N" or answer17 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer18 = input("18. Saya cenderung spontan dalam bertindak maupun berbicara \n  Y/N :")
    if answer18 == "Y" or answer18 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer18 == "N" or answer18 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer19 = input("19. Saya merasa lebih produktif jika mengerjakan tugas dengan sendiri dibandingkan berkelompok"
                     " \n  Y/N :")
    if answer19 == "Y" or answer19 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer19 == "N" or answer19 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer20 = input("20. Saya lebih suka berbicara daripada menulis \n  Y/N :")
    if answer20 == "Y" or answer20 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer20 == "N" or answer20 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer21 = input("21. Saya menyadari akan hal detail kecil yang umumnya orang lain tidak sadar \n  Y/N :")
    if answer21 == "Y" or answer21 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer21 == "N" or answer21 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer22 = input("22. Saya lebih senang menjadi pembicara dibandingkan pendengar \n  Y/N :")
    if answer22 == "Y" or answer22 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer22 == "N" or answer22 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer23 = input("23. Saya suka menganalisa karakter seseorang dan lingkungan di sekitar   \n  Y/N :")
    if answer23 == "Y" or answer23 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer23 == "N" or answer23 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer24 = input("24. Saya suka bergaul baik di dalam dunia nyata maupun di dunia maya   \n  Y/N :")
    if answer24 == "Y" or answer24 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer24 == "N" or answer24 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer25 = input("25. Ketika ada masalah, kamu lebih memilih untuk memendamnya sendiri dibandingkan"
                     "\n    menceritakannya kepada orang lain\n  Y/N :")
    if answer25 == "Y" or answer25 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer25 == "N" or answer25 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer26 = input("26. Ketika bertemu orang baru, kamu lebih memilih untuk membuka topik pembicaraan \n  Y/N :")
    if answer26 == "Y" or answer26 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer26 == "N" or answer26 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer27 = input("27. Ketika ada gosip terbaru, kamu tidak terlalu peduli karena itu bukan urusanmu  \n  Y/N :")
    if answer27 == "Y" or answer27 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer27 == "N" or answer27 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer28 = input("28. Jika bepergian kamu lebih memilih ditemani oleh teman dibandingkan sendirian   \n  Y/N :")
    if answer28 == "Y" or answer28 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer28 == "N" or answer28 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Introvert
while True:
    answer29 = input("29. Jika kamu datang ke suatu acara pesta, kamu lebih memilih untuk pulang lebih awal \n  Y/N :")
    if answer29 == "Y" or answer29 == "y":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer29 == "N" or answer29 == "n":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")
# Ekstrovert
while True:
    answer30 = input("30. Dalam suatu kelompok pertemanan, kamu dianggap sebagai peramai di setiap pertemuan \n  Y/N :")
    if answer30 == "Y" or answer30 == "y":
      score += -1
      ekstro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    elif answer30 == "N" or answer30 == "n":
      score += 1
      intro += 1
      print("---------------------------------------------------------------------------------------------------------")
      break
    else:
       print("--> Opsi tidak sah, Mohon Coba lagi!!!")
       print("--------------------------------------------------------------------------------------------------------")

print()
print("===============================================================================================================")
print("---------------------------------------         HASIL TEST         --------------------------------------------")
print("===============================================================================================================")
print("Nama          :", nama)
print("Jenis kelamin :", kelamin)
print("Tanggal lahir :", tanggal)
print("Umur          :", umurku)
hasil1 = intro + ekstro
print("\nTotal         :", hasil1, "soal")
hasil2 = (100/hasil1 * intro)
hasil3 = (100/hasil1 * ekstro)
print("Introvert     :", "{:.2f}".format(hasil2), "%", "\nEkstrovert    :", "{:.2f}".format(hasil3), "%")

if score < 0:
    print("kepribadian kamu cenderung Ekstrovert")
elif score > 0:
    print("kepribadian kamu cenderung Introvert")
else:
    print("kepribadian kamu cenderung Ambivert :")
    print("Ambivert adalah suatu kepribadian yang digambarkan sebagai sosok dengan campuran kepribadian"
          "\nintrovert dan ekstrovert. Di mana pribadi ambivert senang bersosialisasi dengan orang lain, "
          "\ntetapi terkadang suka menyendiri pada waktu lainnya")
print("===============================================================================================================")
print("----------------------------------------|          *****         |---------------------------------------------")

intj = "\nAhli Keilmuan (INTJ) " \
       "\n(Introverted, Intuitive, Thinking, dan Judging)" \
       "\nPemikir yang imajinatif dan orisinil. Memiliki motivasi tinggi untuk menjalankan ide-idenya " \
       "\nhingga mencapai tujuan. Visioner, mandiri, dan percaya diri, memiliki kemampuan menganalisa" \
       "\nyang bagus, skeptis, kritis, logis, dan kadang keras kepala."

intp = "\nPemikir (INTP) " \
       "\n(Introverted, Intuitive, Thinking, dan Prospecting)" \
       "\nMenghargai intelektualitas dan pengetahuan, lebih suka bekerja sendiri, kritis, skeptis, " \
       "\nmudah curiga dan pesimis, tidak suka memimpin, dan memiliki minat yang jelas."

infj = "\nAdvokat (INFJ) " \
       "\n(Introverted, Intuitive, Feeling, dan Judging)" \
       "\nPendiam dan mistis, tetapi idealis yang sangat menginspirasi dan tak kenal lelah. Perhatian," \
       "\ntekun, idealis, visioner. Selalu ingin memahami pola pikir orang lain."

infp = "\nMediator (INFP)" \
       "\n(Introverted, Intuitive, Feeling, dan Prospecting )" \
       "\nOrang yang puitis, baik hati dan altruisik, selalu ingin membantu aksi kebaikan. Perhatian" \
       "\ndan peka, antusias dan setia, idealis dan perfeksionis, setia kepada prinsip yang digenggam."

istj = "\nAhli Logistik (ISTJ) " \
       "\n(Introverted, Sensing, Thinking, dan Judging)" \
       "\nIndividu yang praktis dan mengutamakan fakta, yang keandalannya tidak dapat diragukan." \
       "\nSerius, senang pada fakta, tekun, pendengar yang baik, memegang aturan."

isfj = "\nPembela (ISFJ) " \
       "\n(Introverted, Sensing, Feeling, dan Judging)" \
       "\nPelindung yang sangat berdedikasi dan hangat, selalu siap membela orang yang dicintainya." \
       "\npenuh pertimbangan, serius, ramah, memiliki kemampuan mengorganisasi, detil, dan bisa diandalkan."

istp = "\nPengrajin (ISTP)" \
       "\n(Introverted, Sensing, Thinking, dan Prospecting) " \
       "\nExperimenter yang pemberani dan praktis, menguasai semua jenis alat. Tenang, cenderung kaku," \
       "\nlogis, rasional, kritis, percaya diri, pemecah masalah yang baik."

isfp = "\nPetualang (ISFP)" \
       "\n(Introverted, Sensing, Feeling, dan Prospecting) " \
       "\nSeniman yang fleksibel dan mengagumkan, selalu siap menjelajahi dan mengalami hal baru." \
       "\nBerpikiran praktis, menghindari konflik, cenderung tidak mau memimpin, santai."

entj = "\nKomandan (ENTJ)" \
       "\n(Extroverted, Intuitive, Thinking, dan Judging) " \
       "\nPemimpin yang pemberani, imajinatif, dan berambisi kuat. Selalu menemukan cara " \
       "\natau menciptakan cara melakukan sesuatu."

entp = "\nPendebat (ENTP) " \
       "\n(Extroverted, Intuitive, Thinking, dan Prospecting)" \
       "\nPemikir yang cerdas dan serius yang gatal terhadap tantangan intelektual. Sanggup memecahkan " \
       "\nmasalah yang menantang. Banyak bicara, fleksibel, dan kurang konsisten."

enfj = "\nProtagonis (ENFJ)" \
       "\n(Extroverted, Intuitive, Feeling, dan Judging)" \
       "\nPemimpin yang karismatik dan menginspirasi, mampu memukau pendengarnya. Kreatif, " \
       "\npeduli apa kata orang lain, pandai bergaul, menyukai tantangan, dan butuh apresiasi."

enfp = "\nJuru Kampanye (ENFP) " \
       "\n(Extroverted, Intuitive, Feeling, dan Prospecting )" \
       "\nSemangat yang antusias, kreatif dan bebas bergaul, yang selalu dapat menemukan alasan untuk tersenyum." \
       "\nRamah, imajinatif, pandai berkomunikasi, dan bisa membaca kebutuhan orang lain."

estj = "\nEksekutif (ESTJ)" \
       "\n(Extroverted, Sensing, Thinking, dan Judging)" \
       "\nAdministrator istimewa, tidak ada duanya dalam mengelola sesuatu atau orang." \
       "\nPraktis, sistematis, disiplin, dan cenderung kaku."

esfj = "\nPengasuh (ESFJ)" \
       "\n(Extroverted, Sensing, Feeling, dan Judging) " \
       "\nOrang yang sangat peduli, sosial dan populer, selalu ingin membantu. Hangat, banyak bicara," \
       "\nmembutuhkan keseimbangan, santai, sederhana, teliti, dan rajin merawat apa yang dimiliki."

estp = "\nPengusaha (ESTP) " \
       "\n(Extroverted, Sensing, Thinking, dan Prospecting)" \
       "\nOrang yang cerdas, bersemangat dan sangat tanggap, benar-benar menikmati hidup yang menantang. " \
       "\nSpontan, aktif, enerjik, ceplas-ceplos, berkarisma, mudah beradaptasi."

esfp = "\nPenghibur (ESFP) " \
       "\n(Extroverted, Sensing, Feeling, dan Prospecting)" \
       "\nOrang yang spontan, bersemangat dan antusias, hidup tidak akan membosankan saat berdekatan dengan mereka. " \
       "\nMudah berteman, ramah, menyenangkan, optimis, ceria, suka menjadi pusat perhatian, menghindari" \
       "\nkonflik, cepat, dan praktis."

introvert = "\nIntrovert adalah tipe kepribadian yang orang-orangnya memiliki ciri lebih fokus terhadap " \
            "\nperasaan internal di dalam dirinya sendiri, dibandingkan dengan stimulasi eksternal dari " \
            "\nlingkungan di sekitarnya. Orang-orang yang introvert, cenderung lebih pendiam, tenang, dan " \
            "\nlebih luwes dalam menilai dirinya sendiri (introspektif). Namun perlu diingat, kepribadian " \
            "\nintrovert tidak sama dengan pemalu atau memiliki gangguan kecemasan sosial."

ekstrovert = "\nEkstrovert adalah kebalikan dari introvert. Jika introvert lebih senang menyendiri," \
             "\nmaka seseorang extrovert lebih menyukai lingkungan yang interaktif. Mereka cukup antusias " \
             "\ndalam hal baru dan senang bergaul. Hal itu disebabkan karena seorang extrovert lebih didominasi" \
             "\ndengan sifat, kondisi atau kebiasaan yang menyenangkan dari luar diri mereka sendiri. Bagi mereka," \
             "\naktivitas sosial, berinteraksi dengan orang lain, bertukar informasi dengan banyak orang dan senang " \
             "\nbergaul adalah hal yang menyenangkan."

kerja1 = "Jenis Pekerjaan yang Cocok untuk Introvert :" \
         "\n1. Akuntan\t\t\t7.  Konselor atau terapis " \
         "\n2. Peneliti\t\t\t8.  Fotografer" \
         "\n3. Dokter hewan\t\t9.  Editor dan penulis" \
         "\n4. Mekanik\t\t\t10. Pustakawan" \
         "\n5. Programmer\t\t11. Pengembang web" \
         "\n6. Apoteker\t\t\t12. Desain interior "

kerja2 = "Jenis Pekerjaan yang Cocok untuk Ekstrovert :" \
         "\n1. Customer Service\t\t7.  Sales " \
         "\n2. Pengacara\t\t\t8.  Psikolog" \
         "\n3. Tour Guide\t\t\t9.  Selebriti" \
         "\n4. Guru\t\t\t\t\t10. Perencana Perkotaan" \
         "\n5. Presenter\t\t\t11. Perawat" \
         "\n6. Event Planner\t\t12. Project Manager "

tokoh1 = "Tokoh/Public Figure yang memiliki kepribadian Introvert :" \
         "\n1. Irene Redvelvet\t\t7.  Dita Karang" \
         "\n2. Emma Watson\t\t\t8.  Mahatma Gandhi" \
         "\n3. Tom Cruise\t\t\t9.  Albert Einstein" \
         "\n4. J.K. Rowling\t\t\t10. Mina Sharon Myoi" \
         "\n5. Bill Gates\t\t\t11. Raditya Dika" \
         "\n6. Min Yoon-gi\t\t\t12. David Gadgetin "

tokoh2 = "Tokoh/Public Figure yang memiliki kepribadian Ekstrovert :" \
         "\n1. Donald Trump\t\t\t\t 7.  William Jefferson Clinton" \
         "\n2. Ria Ricis\t\t\t\t 8.  Steven Paul/Steve Jobs" \
         "\n3. Erpan1140\t\t\t\t 9.  Oprah Gail Winfrey" \
         "\n4. Ivan Gunawan Putra\t\t 10. Kim Se-jeong" \
         "\n5. Martin Luther King Jr.\t 11. Lisa Blackpink" \
         "\n6. Beyoncé Giselle Knowles\t 12. Roy Purdy "
print("---------------------------------------------------------------------------------------------------------------")
while True:
    response = input("\nApa itu yang dimaksud :\nA. Introvert\nB. Ekstrovert\nC. Tampilkan Semua\nD. Next/Skip"
                     "\n Pilih :")
    if response == "a" or response == "A":
        print("\n", introvert)
        print("-------------------------------------------------------------------------------------------------------")
        while True:
            introv = input("\nTipe Introvert berdasarkan MBTI (Myers-Briggs Type Indicator)"
                           "\n1. Ahli Keilmuan (INTJ)\t\t6. Pembela (ISFJ) "
                           "\n2. Pemikir (INTP)\t\t\t7. Pengrajin (ISTP)"
                           "\n3. Advokat (INFJ)\t\t\t8. Petualang (ISFP)"
                           "\n4. Mediator (INFP)\t\t\t9. Tampilkan Semua"
                           "\n5. Ahli Logistik (ISTJ)\t\t10. Back/Skip"
                           "\nPilih nomor :")
            if introv == "1":
                print(intj)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "2":
                print(intp)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "3":
                print(infj)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "4":
                print(infp)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "5":
                print(istj)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "6":
                print(isfj)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "7":
                print(istp)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "8":
                print(isfp)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "9":
                print(intj)
                print("-----------------------------------------------------------------------------------------------")
                print(intp)
                print("-----------------------------------------------------------------------------------------------")
                print(infj)
                print("-----------------------------------------------------------------------------------------------")
                print(infp)
                print("-----------------------------------------------------------------------------------------------")
                print(istj)
                print("-----------------------------------------------------------------------------------------------")
                print(isfj)
                print("-----------------------------------------------------------------------------------------------")
                print(istp)
                print("-----------------------------------------------------------------------------------------------")
                print(isfp)
                print("-----------------------------------------------------------------------------------------------")
            elif introv == "10":
                print("-----------------------------------------------------------------------------------------------")
                break
            else:
                print("\n---> Opsi tidak sah, Mohon Coba lagi!!!")
                print("-----------------------------------------------------------------------------------------------")

    elif response == "b" or response == "B":
        print("\n", ekstrovert)
        print("-------------------------------------------------------------------------------------------------------")
        while True:
            extrov = input("\nTipe Ekstrovert berdasarkan MBTI (Myers-Briggs Type Indicator)"
                           "\n1. Komandan (ENTJ)\t\t\t6. Pengasuh (ESFJ) "
                           "\n2. Pendebat (ENTP)\t\t\t7. Pengusaha (ESTP)"
                           "\n3. Protagonis (ENFJ)\t\t8. Penghibur (ESFP)"
                           "\n4. Juru Kampanye (ENFP)\t\t9. Tampilkan Semua"
                           "\n5. Eksekutif (ESTJ)\t\t\t10. Back/Skip"
                           "\nPilih nomor :")
            if extrov == "1":
                print(entj)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "2":
                print(entp)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "3":
                print(enfj)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "4":
                print(enfp)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "5":
                print(estj)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "6":
                print(esfj)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "7":
                print(estp)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "8":
                print(esfp)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "9":
                print(entj)
                print("-----------------------------------------------------------------------------------------------")
                print(entp)
                print("-----------------------------------------------------------------------------------------------")
                print(enfj)
                print("-----------------------------------------------------------------------------------------------")
                print(enfp)
                print("-----------------------------------------------------------------------------------------------")
                print(estj)
                print("-----------------------------------------------------------------------------------------------")
                print(esfj)
                print("-----------------------------------------------------------------------------------------------")
                print(estp)
                print("-----------------------------------------------------------------------------------------------")
                print(esfp)
                print("-----------------------------------------------------------------------------------------------")
            elif extrov == "10":
                print("-----------------------------------------------------------------------------------------------")
                break
            else:
                print("\n---> Opsi tidak sah, Mohon Coba lagi!!!")
                print("-----------------------------------------------------------------------------------------------")

    elif response == "C" or response == "c":
        print("\n", introvert)
        print("-------------------------------------------------------------------------------------------------------")
        print("\n", ekstrovert)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "d" or response == "D":
        print("-------------------------------------------------------------------------------------------------------")
        break
    else:
        print("\n---> Opsi tidak sah, Mohon Coba lagi!!!")
        print("-------------------------------------------------------------------------------------------------------")

while True:
    response = input("\nSaran jenis pekerjaan yang cocok untuk :\nA. Introvert\nB. Ekstrovert\nC. Tampilkan Semua"
                     "\nD. Next/Skip \n Pilih :")
    if response == "a" or response == "A":
        print("\n", kerja1)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "b" or response == "B":
        print("\n", kerja2)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "c" or response == "C":
        print("\n", kerja1)
        print("-------------------------------------------------------------------------------------------------------")
        print("\n", kerja2)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "d" or response == "D":
        print("-------------------------------------------------------------------------------------------------------")
        break
    else:
        print("\n---> Opsi tidak sah, Mohon Coba lagi!!!")
        print("-------------------------------------------------------------------------------------------------------")

while True:
    response = input("\nTokoh/Public Figure yang memiliki kepribadian : \nA. Introvert\nB. Ekstrovert"
                     "\nC. Tampilkan Semua \nD. Next/End\n Pilih :")
    if response == "a" or response == "A":
        print("\n", tokoh1)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "b" or response == "B":
        print("\n", tokoh2)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "c" or response == "C":
        print("\n", tokoh1)
        print("-------------------------------------------------------------------------------------------------------")
        print("\n", tokoh2)
        print("-------------------------------------------------------------------------------------------------------")
    elif response == "d" or response == "D":
        print("-------------------------------------------------------------------------------------------------------")
        break
    else:
        print("\n---> Opsi tidak sah, Mohon Coba lagi!!!")
        print("-------------------------------------------------------------------------------------------------------")

print("Selesai, Terima kasih sudah mencoba")
print("===============================================================================================================")
print("-----------------------------------------|        *****        |-----------------------------------------------")
print("-----------------------------------------   DASAR PEMROGRAMAN   -----------------------------------------------")
print("------------------------------------------- ANGGOTA KELOMPOK --------------------------------------------------")
print("\nFATNICO FAPRILIYANDO\t		( 19200538 )"
      "\nFIRDA AMALIA\t\t			( 19200333 )"
      "\nGEOVALEN IMANUEL\t\t		( 19200823 )"
      "\nHASBY ASSHIDDIQY\t\t		( 19200596 )"
      "\nIKHSAN NUR MAJID\t\t 		( 19200889 )")
print()
print("===============================================================================================================")
print("-------------------------------------------    THANK YOU    ---------------------------------------------------")
print("----------------------------------------       KELOMPOK 4      ------------------------------------------------")
print("------------------------------------------- SISTEM INFORMASI --------------------------------------------------")
print("------------------------------------------      19.1A.27      -------------------------------------------------")
print("===============================================================================================================")
