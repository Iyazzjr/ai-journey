import cv2, numpy as np, sys

# 1) pick an image path from command line, else default to hello_cv.png
path = sys.argv[1] if len(sys.argv) > 1 else "hello_cv.png"

print(f"🔍 Trying to open: {path}")

# 2) read the image from disk
img = cv2.imread(path)
if img is None:
    raise SystemExit(f"Could not read image: {path}")

# 3) convert to grayscale (easier for thresholding)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4) reduce noise with Gaussian blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 5) convert to black/white automatically (Otsu picks the threshold)
_, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 6) clean small specks using morphological opening
kernel = np.ones((3,3), np.uint8)
opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)

# 7) find external contours (object outlines)
cnts, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 8) print result
print("Detected objects:", len(cnts))

# 9) draw contours on a copy of the image
output = img.copy()
cv2.drawContours(output, cnts, -1, (0, 255, 0), 2)

# 10) save the result to disk
result_name = f"result_{path}"
cv2.imwrite(result_name, output)
print(f"✅ Saved result image as {result_name}")

