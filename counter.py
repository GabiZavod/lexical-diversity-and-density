from collections import Counter

text = "Vstupte do magického světa plného dobrodružství přátelství a nečekaných obratů v novém filmu Králík a Liška Ve starobylém lesním království se setkávají dva zdánlivě odlišní hrdinové skromný Králík a statečná Liška Když tajemný kámen s magickými schopnostmi ohrožuje rovnováhu lesa musí společně překonat všechny překážky a zachránit svůj domov Během své cesty objevují starodávná tajemství potkávají se s nástrahami a objevují sílu pravého přátelství Příběh který zahřeje srdce a je inspirovaný kouzlem přírody je vhodný pro celou rodinu"
lemmatized = "vstupit do magický svět plný dobrodružství přátelství a čekaný obrat v nový film králík a liška v starobilý lesní království se setkávat dva zdánlivě odlišný hrdina skromný králík a statečný liška když tajemný kámen s magický schopnost ohrožovat rovnováha les muset společně překonat všechen překážka a zachránit svůj domov během svůj cesta objevovat starodávný tajemství potkávat se s nástraha a objevovat síla pravý přátelství příběh který zahřát srdce a být inspirovaný kouzlo příroda být vhodný pro celý rodina"
pos = "VERB ADP ADJ NOUN ADJ NOUN NOUN CCONJ ADJ NOUN ADP ADJ NOUN NOUN CCONJ NOUN ADP ADJ ADJ NOUN PRON VERB NUM ADV ADJ NOUN ADJ NOUN CCONJ ADJ NOUN SCONJ ADJ NOUN ADP ADJ NOUN VERB NOUN NOUN VERB ADV VERB DET NOUN CCONJ VERB DET NOUN ADP DET NOUN VERB ADJ NOUN VERB PRON ADP NOUN CCONJ VERB NOUN ADJ NOUN NOUN DET VERB NOUN CCONJ AUX ADJ NOUN NOUN AUX ADJ ADP ADJ NOUN"
lexical = {"NOUN", "VERB", "ADJ", "ADV"}
words = text.lower().split()
lemmas = lemmatized.split()
poses = pos.split()
print(f"Number of tokens: {len(words)}")

lexical_words = Counter([words[i] for i in range(len(poses)) if poses[i] in lexical])
lexical_lemmas = Counter([lemmas[i] for i in range(len(poses)) if poses[i] in lexical])
print(f"Number of lexical words: {len(lexical_words.items())}")
print(f"Number of lexical lemmas: {len(lexical_lemmas.items())}")

unique_words = Counter(words)
print(f"Number of types: {len(unique_words.items())}")

unique_lemmas = Counter(lemmas)
print(f"Number of lemmatized types: {len(unique_lemmas.items())}")

print("---------- MEASURES ----------")
print(f"lexical density: {len(lexical_words.items())/len(words)}")
print(f"TTR: {len(unique_lemmas.items())/len(words)}")

i, j = 0, 49
s = 0
while i<29 and j<len(lemmas):
    d = Counter(lemmas[i:j])
    l_num = len(d.items())
    TTR = l_num/50
    print(f"{i+1} number of lemmas: {l_num}, TTR: {TTR}")
    s += TTR
    i += 1
    j += 1
print(s/29)