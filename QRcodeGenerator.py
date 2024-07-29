import qrcode
import urllib.parse

# Taking UPI id as input
upi_id = input("Enter your UPI id: ")

# Defining recipient details
recipient_name = "Recipient Name"  # Replace with actual recipient name
amount = "1.00"  # Amount to be paid
currency = "INR"  # Currency
transaction_note = "Payment"  # Transaction note

# URL encoding for recipient name and transaction note
recipient_name_encoded = urllib.parse.quote(recipient_name)
transaction_note_encoded = urllib.parse.quote(transaction_note)

# Generating UPI URLs for different platforms
phonepe_url = f'upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&cu={currency}&tn={transaction_note_encoded}'
paytm_url = f'upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&cu={currency}&tn={transaction_note_encoded}'
google_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&cu={currency}&tn={transaction_note_encoded}'
amazon_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name_encoded}&am={amount}&cu={currency}&tn={transaction_note_encoded}'

# Generating QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
amazon_pay_qr = qrcode.make(amazon_pay_url)

# User input to choose the QR code to display
n = input("Choose the QR code:\n paytm\n google pay\n phonepe\n amazon pay\n")
match n.lower():
    case 'paytm':
        print("Paytm QR Code")
        paytm_qr.show()
    case 'google pay':
        print("Google Pay QR Code")
        google_pay_qr.show()
    case 'phonepe':
        print("PhonePe QR Code")
        phonepe_qr.show()
    case 'amazon pay':
        print("Amazon Pay QR Code")
        amazon_pay_qr.show()
    case _:
        print("Invalid Option You Choose")