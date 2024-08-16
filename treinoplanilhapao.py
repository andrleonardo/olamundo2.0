cucaf=int(input('Quantidade Cuca Farofa? ')).strip()
if cucaf <=20:
    print('Quantidade Normal!! Apenas {}' .format(cucaf))
else:
    print('Ativou o modo doente')
somarf= cucaf * 0.498
cucar=int(input('Quantidade Cuca Recheada? ')).strip()

if cucar <=20:
    sabor1=str(input('Qual Sabor 1? ')).strip()
    sabor2=str(input('Qual Sabor 2? ')).strip()
    sabores = [sabor1,sabor2]
    somar= cucar * 0.347
    somat= somar /2
    print('='*10,'Relatorio','='*10)
    print('Cuca {:.4s}:   {:.3f}Kg  '.format(sabor1.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor2.capitalize(),somat))
    print('='*10,'Relatorio','='*10)
elif cucar <=30:
    sabor1=str(input('Qual Sabor 1? ')).strip()
    sabor2=str(input('Qual Sabor 2? ')).strip()
    sabor3=str(input('Qual Sabor 3? ')).strip()
    sabores = [sabor1,sabor2,sabor3]
    somar= cucar * 0.340
    somat= somar /3
    print('='*10,'Relatorio','='*10)
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor1.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor2.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor3.capitalize(),somat))
    print('='*10,'Relatorio','='*10)
elif cucar <=40:
    sabor1=str(input('Qual Sabor 1? ')).strip()
    sabor2=str(input('Qual Sabor 2? ')).strip()
    sabor3=str(input('Qual Sabor 3? ')).strip()
    sabor4=str(input('Qual Sabor 4? ')).strip()
    sabores = [sabor1,sabor2,sabor3,sabor4]
    somar= cucar * 0.335
    somat= somar /4
    print('='*10,'Relatorio','='*10)
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor1.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor2.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor3.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor4.capitalize(),somat))
    print('='*10,'Relatorio','='*10)
else:
    sabor1=str(input('Qual Sabor 1? ')).strip()
    sabor2=str(input('Qual Sabor 2? ')).strip()
    sabor3=str(input('Qual Sabor 3? ')).strip()
    sabor4=str(input('Qual Sabor 4? ')).strip()
    sabor5=str(input('Qual Sabor 5? ')).strip()
    sabores = [sabor1,sabor2,sabor3,sabor4,sabor5]
    somar= cucar * 0.330
    somat= somar /5
    print('='*10,'Relatorio','='*10)
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor1.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor2.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor3.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor4.capitalize(),somat))
    print('Cuca {:.4s}:   {:.3f}kg  '.format(sabor5.capitalize(),somat))
    print('='*10,'Relatorio','='*10)