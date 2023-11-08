import numpy as np
import cv2

def mean_filter(image, k):
    height, width = image.shape
    output = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(k, height-k):
        for j in range(k, width-k):
            sum = 0
            for x in range(-k, k+1):
                for y in range(-k, k+1):
                    sum += image[i+x, j+y]
            output[i, j] = sum // ((2*k+1)**2)
    
    return output

def median_filter(image, k):
    height, width = image.shape
    output = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(k, height-k):
        for j in range(k, width-k):
            neighborhood = []
            for x in range(-k, k+1):
                for y in range(-k, k+1):
                    neighborhood.append(image[i+x, j+y])
            output[i, j] = np.median(neighborhood)
    
    return output

image = cv2.imread("./output_image/Noise_Lenna.jpg", cv2.IMREAD_GRAYSCALE)
filtered_image_mean = mean_filter(image, 3)
filtered_image_median = median_filter(image, 3)


cv2.imshow("Mean Filtered Image", filtered_image_mean)
cv2.imshow("Median Filtered Image", filtered_image_median)

cv2.imwrite("./output_image/mean-filter_Lenna.jpg", filtered_image_mean)
cv2.imwrite("./output_image/median-filter_Lenna.jpg", filtered_image_median)

cv2.waitKey(0)
cv2.destroyAllWindows()