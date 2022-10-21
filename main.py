import qrcode

data = 'https://joelmahougnon.com'

gen = qrcode.make(data)
gen.save('save.png')
