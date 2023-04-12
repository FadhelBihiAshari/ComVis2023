judul yang saya gunakan ialah image based modeling 
tata cara 
1. Pilih Gambar Referensi: Pilih gambar yang akan dijadikan sebagai referensi untuk membuat model 3D. Gambar ini sebaiknya memiliki fitur yang kaya dan dapat dikenali dengan baik, seperti sudut-sudut tajam, tepi, atau pola unik.

2. Ambil Gambar Input: Ambil gambar-gambar lain yang ingin Anda gunakan untuk membuat model 3D. Gambar-gambar ini seharusnya mengandung objek yang sama atau memiliki tampilan yang sama dengan gambar referensi. Gambar-gambar ini akan digunakan untuk mengestimasi posisi dan orientasi objek dalam ruang 3D relatif terhadap gambar referensi.

3. Deteksi Fitur: Gunakan algoritma deteksi fitur komputer vision, seperti SIFT, SURF, atau ORB, untuk mendeteksi fitur-fitur menonjol pada gambar referensi dan input. Fitur-fitur ini akan digunakan untuk mengenali objek yang sama pada kedua gambar dan mengestimasi transformasi 3D yang diperlukan.

4. Pencocokan Fitur: Gunakan algoritma pencocokan fitur, seperti brute-force matching atau FLANN matching, untuk mencocokkan fitur-fitur antara gambar referensi dan input. Hasil pencocokan ini akan digunakan untuk mengestimasi transformasi 3D antara objek dalam ruang 3D.

5. Estimasi Homografi: Gunakan algoritma RANSAC atau metode lainnya untuk mengestimasi homografi atau transformasi perspektif antara gambar referensi dan input berdasarkan fitur-fitur yang cocok. Homografi ini akan menghubungkan koordinat fitur-fitur pada gambar referensi dengan koordinat fitur-fitur pada gambar input dalam ruang 3D.

6. Warp Gambar Input: Gunakan homografi yang telah diperoleh untuk melakukan warp (transformasi) gambar input sehingga objek pada gambar input menjadi sejajar dengan objek pada gambar referensi dalam ruang 3D. Hasil dari warp ini akan menghasilkan gambar input yang telah "diprojeksikan" ke dalam sistem koordinat 3D yang sama dengan gambar referensi.

7. Gabungkan Gambar: Gabungkan gambar referensi dan gambar input yang telah diwariskan (warped) untuk menghasilkan model 3D yang menggabungkan informasi dari kedua gambar. Anda dapat menggunakan operasi penggabungan (blending) atau operasi matematis lainnya untuk menggabungkan gambar-gambar ini.

8. Visualisasi Model 3D: Anda dapat memvisualisasikan model 3D yang dihasilkan dalam berbagai bentuk, seperti sebagai gambar 3D, model 3D interaktif, atau model 3D yang dapat diimpor ke perangkat lunak pemodelan 3D untuk analisis lebih lanjut.