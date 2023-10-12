print('\n\n\nWelkom bij de quiz over Impressionisme')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de quiz beginnen!!\n\n')

    antwoord=input('Vraag 1: Wat is een van de bekenste Nederlandse Impressonisten? ')
    if antwoord.lower()=='Van gogh':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 2: Wanneer is het Impressionisme onstaan? ')
    if antwoord.lower()=='1874':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: Waar komt het Impressionisme vandaan a: Nederland b: Frankrijk')
    antwoord=input('a: Nederland')
    antwoord=input('b: Frankrijk')
    antwoord=input('c: Duitsland')
    antwoord=input('d: Engeland')
    if antwoord.lower()=='b' or antwoord.lower()=='B':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 4: Waar staat het Impressionisme om bekend ')
    if antwoord.lower()=='onrust en dynamiek, expresie van emotie en groten contrasten':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 5: Welke van deze schilderijen is Impressionisme ')
    antwoord=input('a: Mona Lisa')
    antwoord=input('b: Meisje met de parel')
    antwoord=input('c: De Nachtwacht')
    antwoord=input('d: De sterrennacht')

    if antwoord.lower()=='d' or antwoord.lower()=='D':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 6: Wanneer eindigt het Impressionisme? ')
    if antwoord.lower()=='1914':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 7: Kwam Expressionsme voor of na Impressionisme? ')
    if antwoord.lower()=='er voor':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 8: Wat is een tweede stroming die nog wel onder het Impressionisme valt? ')
    if antwoord.lower()=='Neo Impressionisme':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 9: Wat is een bekende Impressionisme schilder uit Frankrijk? ')
    if antwoord.lower()=='Claude Monet':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 10: Wat voor materiaal gebruikten Impressionisten? ')
    antwoord=input('A: Waterverf ')
    antwoord=input('B: Acryl ')
    antwoord=input('C: Olieverf ')
    if antwoord.lower()=='C':
        punten += 1
        print('goed')
    else:
        print('fout')

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor dit project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')