import csv
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
akar = math.sqrt

def program():
    dataset = pd.read_csv("jumlah-penduduk-berdasarkan-agama-2018-s2.csv")

    # mengambil kolom 2 dan 3
    colum_islam = dataset.iloc[:, 2].values
    colum_kristen = dataset.iloc[:, 3].values

    def mencari_centroid_dst():
        # mengambil letak centroid pertama acak
        random1 = []
        for i in range(151):
            random1.append(i)
        hasil_random1 = random.choice(random1)

        # hasil centroid pertama acak
        cen_pertama1 = colum_islam[hasil_random1]
        cen_pertama2 = colum_kristen[hasil_random1]
    
        # mengambil letak centroid kedua acak
        random2 = []
        for j in range(151):
            random2.append(j)
        hasil_random2 = random.choice(random2)

        # hasil centroid kedua acak
        cen_kedua1 = colum_islam[hasil_random2]
        cen_kedua2 = colum_kristen[hasil_random2]
    
        if (cen_pertama1==cen_kedua1 and cen_pertama2==cen_kedua2):
            mencari_centroid_dst()
        else:

            # menghitung distance ke centroid 1 dan centroid 2
            hasil_hitung_pertama1 = []
            hasil_hitung_pertama2 = []
            hasil1 = []
            hasil2 = []
            anggota1_kiri = []
            anggota1_kanan = []
            anggota2_kanan = []
            anggota2_kiri = []
            jml_awal1 = []
            jml_awal2 = []

            for a in range(len(colum_islam)):
                for b in range(len(colum_kristen)):
                    if (a==b):
                        jarak1 = akar(((cen_pertama1 - colum_islam[a])**2) + ((cen_pertama2 - colum_kristen[a])**2))
                        jarak2 = akar(((cen_kedua1 - colum_islam[a])**2) + ((cen_kedua2 - colum_kristen[a])**2))
                        if(jarak1 < jarak2):
                            hasil1.append(jarak1)
                            anggota1_kiri.append(colum_islam[a])
                            anggota1_kanan.append(colum_kristen[a])
                            hasil_hitung_pertama1.append(jarak1)
                            jml_awal1.append(jarak1)
                            hasil_hitung_pertama2.append(jarak2)
                        else:
                            hasil2.append(jarak2)
                            anggota2_kanan.append(colum_kristen[a])
                            anggota2_kiri.append(colum_islam[a])
                            hasil_hitung_pertama2.append(jarak2)
                            jml_awal2.append(jarak2)
                            hasil_hitung_pertama1.append(jarak1)

            # menghitung rata-rata tiap kolom sebagai pusat cluster yang baru
   
            hasil1_baru = []
            hasil2_baru = []
            anggota_clus1 = []
            anggota_clus2 = []
            seluruh_kiri = []
            seluruh_kanan = []
            anggota1_kiribaru = []
            anggota1_kananbaru = []
            anggota2_kiribaru = []
            anggota2_kananbaru = []
            
            rata1_a = sum(anggota1_kiri) / len(anggota1_kiri)
            rata1_b = sum(anggota1_kanan) / len(anggota1_kanan)
            rata2_a = sum(anggota2_kiri) / len(anggota2_kiri)
            rata2_b = sum(anggota2_kanan) / len(anggota2_kanan)
            
            for j in range(len(colum_islam)):
                for k in range(len(colum_kristen)):
                    if(j==k):
                        dist1 = akar(((rata1_a - colum_islam[j])**2) + ((rata1_b - colum_kristen[j])**2))
                        dist2 = akar(((rata2_a - colum_islam[j])**2) + ((rata2_b - colum_kristen[j])**2))
                        if (dist1<dist2):
                            hasil1_baru.append(dist1)
                            seluruh_kiri.append(dist1)
                            seluruh_kanan.append(dist2)
                            anggota_clus1.append(colum_islam[j])
                            anggota1_kiribaru.append(colum_islam[j])
                            anggota1_kananbaru.append(colum_kristen[j])
                        else:
                            hasil2_baru.append(dist2)
                            seluruh_kanan.append(dist2)
                            seluruh_kiri.append(dist1)
                            anggota_clus2.append(colum_islam[j])
                            anggota2_kiribaru.append(colum_islam[j])
                            anggota2_kananbaru.append(colum_kristen[j])
                            
            if (len(hasil1)==len(hasil1_baru) and len(hasil2)==len(hasil2_baru)):
                plt.scatter(seluruh_kiri,seluruh_kanan,c='yellow')
                plt.show()

                print ("Centroid pertama = ",cen_pertama1,"dan",cen_pertama2)
                print ("Centroid kedua = ",cen_kedua1,"dan",cen_kedua2)
                print ("----------------------------------------------------------------------------------------------------------------------------------------------")                
                print ("Data cluster pertama adalah :",anggota1_kiri,anggota1_kanan)
                print ("----------------------------------------------------------------------------------------------------------------------------------------------")
                print ("Data cluster kedua adalah :",anggota2_kiri,anggota2_kanan)
            else:
                program()
                     
    mencari_centroid_dst()

program()


