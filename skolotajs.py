class Skolotajs:
    def __init__(self, uzvards, stundu_sk, tips):
        self.uzvards = uzvards
        self.stundu_sk = stundu_sk
        self.tips = tips

    def izdrukat(self):
        pass


class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, stundu_sk):
        super().__init__(uzvards, stundu_sk, 1)
        self.klase = klase

    def izdrukat(self):
        print(f"Sākumskolas (tips – {self.tips}) skolotājs {self.uzvards} māca {self.stundu_sk} stundas {self.klase} klasē.")

        
    
class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, pirmais_prieksmets, otrais_prieksmets, pirmais_stundu_sk, otrais_stundu_sk):
        kopskaits = pirmais_stundu_sk + otrais_stundu_sk
        super().__init__(uzvards, kopskaits, 3)
        self.pirmais_prieksmets = pirmais_prieksmets
        self.otrais_prieksmets = otrais_prieksmets

    def izdrukat(self):
        print(f"Vidusskolas (tips – {self.tips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.pirmais_prieksmets} un {self.otrais_prieksmets}, kopā {self.stundu_sk} stundas.")


def main():
    ssk_uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase = input("Ievadiet skolotāja klasi: ")
    ssk_stundu_sk = int(input("Ievadiet skolotāja stundu skaitu: "))
        
    vsk_uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    pirmais_prieksmets = input("Ievadiet pirmo pasniegto priekšmetu: ")
    pirmais_stundu_sk = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    otrais_prieksmets = input("Ievadiet otro pasniegto priekšmetu: ")
    otrais_stundu_sk = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))


    ssk_skolotajs = SakumskolasSkolotajs(ssk_uzvards, klase, ssk_stundu_sk)
    vsk_skolotajs = VidusskolasSkolotajs(vsk_uzvards, pirmais_prieksmets, otrais_prieksmets, pirmais_stundu_sk, otrais_stundu_sk)

    ssk_skolotajs.izdrukat()
    vsk_skolotajs.izdrukat()


if __name__ == "__main__":
    main()