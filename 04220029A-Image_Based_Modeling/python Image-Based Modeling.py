import cv2
import numpy as np

# Baca gambar referensi
img_ref = cv2.imread('Sketsa-Gambar-Kartun.jpg', cv2.IMREAD_GRAYSCALE)

# Baca gambar input
img_input = cv2.imread('Sketsa-Gambar-Kartun.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi fitur (misalnya, keypoints dan descriptors) pada gambar referensi dan input
sift = cv2.xfeatures2d.SIFT_create()
kp_ref, des_ref = sift.detectAndCompute(img_ref, None)
kp_input, des_input = sift.detectAndCompute(img_input, None)

# Lakukan pencocokan fitur antara gambar referensi dan input
matcher = cv2.BFMatcher()
matches = matcher.knnMatch(des_ref, des_input, k=2)

# Filter hasil pencocokan menggunakan metode ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Ambil titik-titik keypoints yang cocok
src_pts = np.float32([kp_ref[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp_input[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Lakukan estimasi homografi
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Warp gambar input ke gambar referensi menggunakan homografi
h, w = img_ref.shape
warped_img = cv2.warpPerspective(img_input, M, (w, h))

# Gabungkan gambar referensi dan gambar input yang telah di-warp
result = cv2.addWeighted(img_ref, 0.5, warped_img, 0.5, 0)

# Tampilkan hasil
cv2.imshow('Hasil Image-Based Modeling', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
