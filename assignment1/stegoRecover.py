import cv2

stego_image = cv2.imread('lsb_stego_image.bmp')
stego_image_msb = cv2.imread('msb_stego_image.bmp')
name = "BorBin Berzo"

def extract_data(image, data_len):
    binary_data = ''
    data_index = 0

    for row in image:
        for pixel in row:
            for channel in range(3):  # Iterate over RGB channels
                if data_index < data_len * 8:
                    binary_data += format(pixel[channel], '08b')[-1]
                    data_index += 1
                else:
                    break
        if data_index >= data_len * 8:
            break

    data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return data

def extract_data_msb(image, data_len):
    binary_data = ''
    data_index = 0

    for row in image:
        for pixel in row:
            for channel in range(3):  # Iterate over RGB channels
                if data_index < data_len * 8:
                    binary_data += format(pixel[channel], '08b')[0]
                    data_index += 1
                else:
                    break
        if data_index >= data_len * 8:
            break

    data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    return data

extracted_name = extract_data(stego_image, len(name))
msb_name = extract_data_msb(stego_image_msb, len(name))
print("LSB Extracted Name:", extracted_name)
print("MSB Extracted Name:", msb_name)
