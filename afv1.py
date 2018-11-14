# Naam:
# Datum:
# Versie:

from typing import List, Any, Union


def main():
    bestand = "test.fna"
    headers, seqs = lees_inhoud(bestand)
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestandsnaam):
    try:
        bestand = open(bestandsnaam)
    except FileNotFoundError:
        print("\nBestand niet gevonden.\n\nWeet je zeker dat het bestand '", bestandsnaam, "' in dezelfde folder zit?")
        quit()
    headers = []
    seqs: List[Union[str, Any]] = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    try:
        bestand = open(alpaca_seq)
    except FileNotFoundError:
        print("\nBestand niet gevonden.\n\nWeet je zeker dat het bestand '", alpaca-seq, "' in dezelfde folder zit?")
        quit()
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^", "")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


main()
