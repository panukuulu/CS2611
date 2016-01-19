subtotal,gratuity = input("Enter the subtotal (example 100) and gratuity rate (for example 12) separated by a comma: ").split(',')
subtotal = float(subtotal)
grt = float(gratuity) * subtotal / 100
tot = grt + subtotal
print('The gratuity is {:f} and the total is {:f}'.format(grt,tot))
