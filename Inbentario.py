class Inbentario:

    izena = ""
    kantitatea = 0
    salneurria = 0

    def __init__(self,i_izena,i_kantitatea,i_salneurria):
        self.izena = i_izena
        self.kantitatea = i_kantitatea
        self.salneurria = i_salneurria

    def kalkulatu(self,i_zenbat):
        precio_total = i_zenbat * self.salneurria
        if(i_zenbat >= 5 and i_zenbat <10):
            prezio_finala = precio_total-(precio_total * 0.10)
            print(str(i_zenbat)+" "+self.izena+" erosi dituzu "+str(prezio_finala)+"€ gatik, 10%-eko deskontuarekin.")
            self.erosi(i_zenbat)
        if(i_zenbat >= 10):
            prezio_finala = precio_total - (precio_total * 0.15)
            print(str(i_zenbat)+" "+self.izena+" erosi dituzu "+str(prezio_finala)+"€ gatik, 15%-eko deskontuarekin.")
            self.erosi(i_zenbat)
        if(i_zenbat < 5):
            prezio_finala = precio_total
            print(str(i_zenbat)+" "+self.izena+" erosi dituzu "+str(prezio_finala)+"€ gatik, deskonturik gabe.")
            self.erosi(i_zenbat)

    def erosi(self,i_zenbat):
        self.kantitatea = self.kantitatea - i_zenbat
        print("Stock "+self.izena+" : "+str(self.kantitatea))