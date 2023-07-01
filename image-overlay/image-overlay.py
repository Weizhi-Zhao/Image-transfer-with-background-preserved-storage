import cv2
# 导入OpenCV库

img1 = cv2.imread('./imgs/img1.jpg')
img2 = cv2.imread('./imgs/img2.jpg')
# 使用cv2.imread()函数读取两张图片

img1 = cv2.resize(img1, (1300, 700))
img2 = cv2.resize(img2, (1300, 700))
# 使用cv2.resize()函数将两张图片调整为相同大小

img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# 将第一张图片转换为灰度图像，使用cv2.cvtColor()函数，其中cv2.COLOR_BGR2GRAY表示将BGR图像转换为灰度图像

ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
# 使用cv2.threshold()函数对灰度图像进行阈值处理，得到二值化的掩膜图像，ret为阈值，mask为二值化图像

mask_inv = cv2.bitwise_not(mask)
# 对掩膜图像进行反转，使用cv2.bitwise_not()函数

img1_bg = cv2.bitwise_and(img1, img1, mask=mask)
# 对第一张图片和掩膜图像进行按位与操作，获取第一张图片中与掩膜为白色部分相交的部分，使用cv2.bitwise_and()函数

img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
# 对第二张图片和反转后的掩膜图像进行按位与操作，获取第二张图片中与反转后的掩膜为白色部分相交的部分

res = cv2.add(img1_bg, img2_fg)
# 将第一张图片中与掩膜为白色部分相交的部分与第二张图片中与反转后的掩膜为白色部分相交的部分进行相加，得到最终结果

cv2.imshow('result', res)
# 使用cv2.imshow()函数显示结果图像，窗口名称为'result'

cv2.waitKey(0)
# 等待按下任意按键

cv2.destroyAllWindows()
# 销毁所有创建的窗口
