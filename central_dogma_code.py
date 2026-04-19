import pandas as pd

f = open("/content/DNA.txt", "r")
DNA=f.readlines()
#print(DNA)
seq = "".join([x.strip() for x in DNA])
#print(seq)
#dna = "".join(seq)   # DNA sequence
print("DNA sequence:", seq)

rna = seq.replace("T","U")    # DNA to RNA Conversion
print("mRNA sequence:", rna)

#genetic_code = open("/content/genetic_code.txt","r")

files = pd.read_csv("/content/genetic_code.txt", sep="\t")
df = pd.DataFrame(files)
#print(df)


##-----------mRNA to Protein Converison------------

#result_dict = dict(zip(df['AminoAcid'], df['Codon']))
#print(result_dict)

#creating dictionary of gentic code
genetic_code_dict = {}

for k, v in zip(df['AminoAcid'], df['Codon']):
    if k in genetic_code_dict:
        genetic_code_dict[k].append(v)
    else:
        genetic_code_dict[k] = [v]

#print(genetic_code_dict)

protein = ""

stop_translation= False   # condition to run and stop the loop when the stop codon present

# Find start codon position
start_index = rna.find("AUG")

if start_index != -1:
    for i in range(start_index, len(rna), 3):
        codon = rna[i:i+3]

        for key, values in genetic_code_dict.items():
            if codon in values:
                if key == "Stop":
                    stop_translation = True
                    break
                else:
                  protein += key
                break
        if stop_translation:
         break
print("Protein sequence:", protein)
