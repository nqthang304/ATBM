dict_Apha = {
                0: "A",
                1: "B",
                2: "C",
                3: "D",
                4: "E",
                5: "F",
                6: "G",
                7: "H",
                8: "I",
                9: "J",
                10: "K",
                11: "L",
                12: "M",
                13: "N",
                14: "O",
                15: "P",
                16: "Q",
                17: "R",
                18: "S",
                19: "T",
                20: "U",
                21: "V",
                22: "W", 
                23: "X",
                24: "Y",
                25: "Z"
            }
             
k=6
Plaintext="Nguyen Quoc Thang"
Ciphertext=""

for i in Plaintext.upper():
    if i==" ":
        Ciphertext+=" "
    else:
        for j in dict_Apha:
            if i==dict_Apha[j]:
                if j+k>25:
                    Ciphertext+=dict_Apha[(j+k)%26]
                else:
                    Ciphertext+=dict_Apha[j+k] 
print(Ciphertext)