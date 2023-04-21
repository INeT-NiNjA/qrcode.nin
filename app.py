def clearterminal():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generate_qr(data,filename):
    import qrcode
    qr = qrcode.QRCode(version=3, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filename)

def read_qr(filename):
    import cv2
    reader = cv2.QRCodeDetector()
    try:
        value,a,b = reader.detectAndDecode(cv2.imread(filename))
        print()
        print(f" Encoded data is: {value}")
    except cv2.error:
        print()
        print(" The file-path you entered doesnt exist..Try checking the file or try entering the full path")

def main():
    clearterminal()
    print()
    print('     |qrcode.nin|•|INeT-NiNjA|')
    print()
    loop = True
    while loop==True:
        try:
            print()
            print(' What do you want to do?')
            print(' 1) Generate QR code')
            print(' 2) Read QR code')
            print()
            ch = int(input(' Enter number of choice => '))
            print()
            if ch == 1:
                loop = False
                data = input(' Enter data to be encoded => ')
                filename = input(' Enter name under which the image will be saved => ')
                file_name = filename + '.png'
                generate_qr(data,file_name)
            elif ch == 2:
                loop = False
                filename = input(' Enter the complete name/path of the qrcode image file => ')
                read_qr(filename)
            else:
                print(' Please select a valid option')
        except KeyboardInterrupt:
            print()
            print(' Exiting program')
            quit()
        except ValueError:
            print()
            print(' Please select a valid option')




try:
    import cv2
    import qrcode
    
except ImportError:
    print(' Please install the necessary dependencies before running the program')
    print(" Do 'pip install -r requirements.txt' ")
else:
    main()
