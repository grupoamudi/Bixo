import LMK

class Bixo:

    estados = {'':,'':,'':,'':,'':} #mostra o emociona do bixo; tem impacto na interface dele

    leituras = {'Temperatura' : 0, 'Luz' : 0, 'Dist' : 0, 'Visao' : 'Nada'} #leituras feitas pelos sensores

    def funcionando():
        return True
#declaracao dos sensores
bixo = Bixo()
# visao = cv2.cap()
# sonar = SensorDist()
# luz = SensorLuz()
# temp = SensorTemp()
# ia = IA()
# interacoes = Interacao()
while (bixo.funcionando()):
    # Obter leituras dos sensores
    
    # leituras['Temperatura'] = temp.getLeitura()
    
    # leituras['Luz'] = luz.getLeitura()
    
    # leituras['Dist'] = sonar.getLeitura()

    # leituras['Visao'] = ia.Interpretar(visao.capture())

    # if(leituras == valor): bixo.mudarEstado(estados[''])

    # interacoes.acionar(leituras, estados)
