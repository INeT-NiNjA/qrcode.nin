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
        from colorama import Fore
        value,a,b = reader.detectAndDecode(cv2.imread(filename))
        print()
        print(Fore.LIGHTGREEN_EX + f" Encoded data is: {value}")
    except cv2.error:
        print()
        print(Fore.RED + " The file-path you entered doesnt exist..Try checking the file or try entering the full path")

def main():
    from colorama import Fore
    clearterminal()
    print()
    print(Fore.WHITE + '     |qrcode.nin|•|INeT-NiNjA|')
    print()
    loop = True
    while loop==True:
        try:
            print()
            print(Fore.CYAN + ' What do you want to do?')
            print(Fore.CYAN + ' 1) Generate QR code')
            print(Fore.CYAN + ' 2) Read QR code')
            print()
            ch = int(input(Fore.BLUE + ' Enter number of choice => '))
            print()
            if ch == 1:
                loop = False
                data = input(Fore.CYAN + ' Enter data to be encoded => ')
                filename = input(Fore.CYAN + ' Enter name under which the image will be saved => ')
                file_name = filename + '.png'
                generate_qr(data,file_name)
            elif ch == 2:
                loop = False
                filename = input(Fore.BLUE + ' Enter the complete name/path of the qrcode image file => ')
                read_qr(filename)
            else:
                print(Fore.RED + ' Please select a valid option')
        except KeyboardInterrupt:
            print()
            print(Fore.LIGHTRED_EX + ' Exiting program')
            quit()
        except ValueError:
            print()
            print(Fore.RED + ' Please select a valid option')




try:
    import cv2
    import qrcode
    import colorama
    
except ImportError:
    print(' Please install the necessary dependencies before running the program')
    print(" Do 'pip install -r requirements.txt' ")
else:
    main()
