import pikepdf, time
from pwinput import pwinput
from tkinter import filedialog

#taking the file
file_path = filedialog.askopenfile(
                    title="Select a file",
                    filetypes=([("PDF Files", "*.pdf")]),
                )
m = str(file_path).split()
m.remove("<_io.TextIOWrapper")
m.remove("encoding='cp1252'>")
m.remove("mode='r'")
n = " ".join(m)
pdf_loc = n.split("=")[1]
pdf_loc = pdf_loc.replace("'", "")
pdf_loc = pdf_loc.strip()

pdf_pass = pwinput('Enter PDF Password: ')

pdf = pikepdf.open(pdf_loc, password=pdf_pass)

#getting the new location
pdf_new_loc = pdf_loc.split('/')
poped = pdf_new_loc.pop()
poped = poped.split('.')
poped[0] = str(poped[0]) + ' (unlocked)'
poped = '.'.join(poped)
pdf_new_loc = "/".join(pdf_new_loc)
pdf_new_loc = pdf_new_loc + "\ " +poped
pdf.save(pdf_new_loc)
 
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

notcomplete = True

i = 0

while notcomplete:
    print(animation[i % len(animation)], end='\r')
    time.sleep(.2)
    i += 1
    if i == 0.8*10:
        break
print("The password successfully removed from the PDF.")