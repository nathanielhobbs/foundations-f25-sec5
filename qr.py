import qrcode, sys

img = qrcode.make(sys.argv[1] if len(sys.argv) > 1 else 'https://rutgers.edu')
img.save("qr.png")

print('Saved qr.png')
