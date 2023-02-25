from barcode.ean import EAN13
import random
generated_user_ID =''

for element in range(1,14):
    generated_user_ID = generated_user_ID + str(random.randint(0,10))
    "Random digit have been generated for each element of object ID 13 elements"
    
    
"Generate a barcode from User ID and save as svg "
user_barcode = EAN13(generated_user_ID)
user_barcode.save("new_code")
    
    
    
