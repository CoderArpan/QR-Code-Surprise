import qrcode
from PIL import Image

def generate_qr_code(message, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def display_qr_code(filename):
    img = Image.open(filename)
    img.show()

def main():
    # Customize your proposal message
    proposal_message = "Hey [Crush's Name], will you be mine? 💖"
    
    # Generate QR code with your proposal message
    generate_qr_code(proposal_message, "proposal_qr_code.png")
    print("QR code generated successfully!")
    
    # Display QR code
    display_qr_code("proposal_qr_code.png")
    print("Scan the QR code above to reveal the proposal!")

if __name__ == "__main__":
    main()
