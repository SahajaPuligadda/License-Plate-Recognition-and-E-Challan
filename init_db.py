import sqlite3

connection = sqlite3.connect('vehicledatabase.db')

with open('vehicledetails.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
names = ['Sahaja','Vishnupriya','Sindhu','Liam','Emma', 'Noah','Olivia','William',
         'Ava','James','Isabella','Oliver','Sophia','Benjamin','Charlotte','Elijah',
         'Mia','Lucas','Amelia','Mason','Harper','Logan','Evelyn','Alexander',
         'Abigail','Ethan','Emily','Jacob','Elizabeth','Michael','Mila','Daniel',
         'Ella','Henry','Avery','Jackson','Sofia','Sebastian','Camila','Aiden',
         'Aria','Matthew','Scarlett','Samuel','Victoria','David','Madison','Joseph',
         'Luna','Carter','Grace','Owen','Chloe','Wyatt','Penelope','John','Layla',
         'Jack','Riley','Luke','Zoey','Jayden','Nora','Dylan','Lily','Grayson',
         'Eleanor','Levi','Hannah','Isaac','Lillian','Gabriel','Addison','Julian',
         'Aubrey','Mateo','Ellie','Anthony','Stella','Jaxon','Natalie','Lincoln',
         'Zoe','Joshua','Leah','Christopher','Hazel','Andrew','Violet','Theodore',
         'Aurora','Caleb','Savannah','Ryan','Audrey','Asher','Brooklyn','Nathan',
         'Bella','Thomas']
mails = ['1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in','1602-18-735-120@vce.ac.in','1602-18-735-077@vce.ac.in',
         '1602-18-735-092@vce.ac.in']

plate_numbers = ['PZ65BYV','YD63LB','MH01AV8866','25GFJX','TI9LBS','M771276','73LTG4','JA62UAR','06ZRZZ','B2228HM',
                 'BAD231','P3RVP','KA1SER','695299','15LK10898','9TBZ74','RP524X','ZH175G','V971KZ','11SZSR',
                 'GSDS79','82TGLP','HL821D','172TMJ','4940TD53','8XRJ16','HR26DA0471','PGMN112','TN07BU5427', '7ZBG58',
                 'GJW115A1138','21XHLR','700V','MH12JC2813','KL01BT2525','ZG169D','J389NLT','85SLX2','DAN54P','V554JT',
                 'PJC4903','PJH0957','MH20DV2362','FZJ55T','HR26DK0830','PJI5396','PJU2207','PJU2853','6ZWF846','1T43213',
                 'HR26BP3543','RK906AJ','RK892AE','KL55R2473','1B80338','BZM2227','4BO4979','1B19839','4B40262','2T40211',
                 '4B39376','3B29485','RK959AF','RK641AL','RK959AD','LM169AM','4PCI264','9185914','EAZ6913','HH9G5W',
                 'NZP8292','M5XSX','627WWI','PJG0783','HB8X9J','HR26DA2330','RK828AG','MH02CT2727','RK248AH','RK161AG',
                 'TN87TC111','DL8CAF5030','DL3CAM0857','64XJRK','84ZRZB','KL01KLKL01','TN07BV5200','KA031351','MH46Z8892','MH20CS9817',
                 'MH20EE7601','MH20EE7598','HR696969','HR26DK6475','KA29Z999','KL10AV6633','256D259','DL8CX4850','HR26BR9044','ASM28965']

for i in range(100):
    cur.execute("INSERT INTO vehicledetails (ownername, carnumber, email) VALUES (?, ?, ?)",
                (names[i], plate_numbers[i], mails[i]))

print(cur.execute("SELECT * FROM vehicledetails").fetchall())

connection.commit()
connection.close()
