import easyocr
import time 

class Ocr:

	def __init__(self):
		self.reader = easyocr.Reader(['en']) 

	def ocr(self, image_filename):
		start_time = time.time()
		result = (self.reader).readtext(image_filename)
		print("--- %s seconds ---" % (time.time() - start_time))
		#print(result)
		text_string = ""
		for elem in result:
			#print(elem[1])
			text_string += elem[1] + "\n"
		return text_string

