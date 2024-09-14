import cv2

name = "Corvin Terzo"

image = cv2.imread('nycTaxi.jpg')

def lsb(image, data):
    i = 0
    binary = ''.join(format(ord(char), '08b') for char in data)
    length = len(binary)

    for row in image:
        for pixel in row:
            for channel in range(3):
                if i < length:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary[i], 2)
                    i += 1
                else:
                    break
    return image

def msb(image, data):
    i = 0
    binary = ''.join(format(ord(char), '08b') for char in data)
    length = len(binary)

    for row in image:
        for pixel in row:
            for channel in range(3):
                if i < length:
                    pixel[channel] = int(binary[i] + format(pixel[channel], '08b')[1:], 2)
                    i += 1
                else:
                    break
    return image

lsb_stego_image = lsb(image, name)
cv2.imwrite('lsb_stego_image.bmp', lsb_stego_image)

msb_stego_image = msb(image, name)
cv2.imwrite('msb_stego_image.bmp', msb_stego_image)

print("Done!")

# Questions and Answers 

# Since the stego key for my images is just the first pixels from the top left of the image moving right for the 
# length of the binary data, the difference between the LSB and MSB stego images can be seen there. The top left 
# of the LSB image is almost identical to the original image but the top left of the MSB image is clearly not a 
# part of the original image since it had its color values modified to the highest degree possible during the 
# steganography process. This results in a line of purple, blue, red, green, and other brightly colored pixels that 
# look like an error in the top left of the image. 