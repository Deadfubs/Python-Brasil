from datetime import datetime, timedelta


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
                 5: "maio", 6: "junho", 7: "julho", 8: "agosto",
                 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
        return meses[self.momento_cadastro.month]

    def dia_semana(self):
        dias = ["segunda", "terça", "quarta",
                "quinta", "sexta", "sábado", "domingo"]
        return dias[self.momento_cadastro.weekday()]

    def formata_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastro(self):
        return (datetime.today()+timedelta(days=30)) - self.momento_cadastro
