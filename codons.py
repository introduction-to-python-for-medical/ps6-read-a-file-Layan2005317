def create_codon_dict(file_path):
    path = "data/codons.txt"
    file =open(path)
    rows = file.readlines()
    file.close()
    amino_acids = {}
    for row in rows:
        row = row.strip().split('\t')
        codon = row[0]
        amino_acid = row[2]
        amino_acids[codon] = amino_acid
    return amino_acids


