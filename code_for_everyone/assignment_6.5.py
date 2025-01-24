text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find(":")

piece = text[atpos+5:]
value = float(piece)
print(value)

