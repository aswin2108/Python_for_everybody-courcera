text = "X-DSPAM-Confidence:    0.8475"
data=text.find('    ')
host=float(text[data+4:])
print(host)