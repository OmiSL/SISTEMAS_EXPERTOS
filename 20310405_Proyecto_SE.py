"""
    Omar Sanchez Larios
    20310405
    
    Sistemas Expertos
    
    Proyecto:
        Sistema Experto - Healthy Body
"""

import sys
import random 


""" ------------------------------------------ Modulo del Ingeniero -------------------------------------------------- """
def ingeniero():
        AlimentoT=['Verduras y Legumbres',
                        'Carnes y Derivados',
                        'Semillas',
                        'Frutas',
                        'Cereales y Derivados',
                        'Pescados y Mariscos',
                        'Huevos',
                        'Lacteos',
                        'Dulces y Reposteria',
                        'Bebidas',
                        'Comidas Elaboradas']
        print ('Modo Ingeniero')
        print ('Adquisicion de Nuevo Conocimiento sobre Alimentos')
        nombre=input('Introduce el Nombre del Alimento>:')
        caloria=input('Introduce las calorias de %s>:' %(nombre))
        proteina=input('Introduce las proteinas de %s>:'%(nombre))
        carbohidratos=input('Introduce los Carbohidratos de %s>:'%(nombre))
        grasa=input('Introduce la grasa de %s>:'%(nombre))
        indiceglicemico=input('Introduce el IndiceGlicemico de %s>:'%(nombre))
        print ('elije un tipo>:')
        print ('1.-Verduras y Legumbres')
        print ('2.-Carnes y Derivados')
        print ('3.-Semillas')
        print ('4.-Frutas')
        print ('5.-Cereales y Derivados')
        print ('6.-Pescados y Mariscos')
        print ('7.-Huevos')
        print ('8.-Lacteos')
        print ('9.-Dulces y Reposteria')
        print ('10.-Bebidas')
        print ('11.-Comidas Elaboradas')
        tipo=input('Introduce las proteinas de %s>:'%(nombre))
        file=open('conocimiento','a')
        file.write('\n')
        file.write(nombre+'|'+str(caloria)+'|'+str(proteina)+'|'+str(carbohidratos)+'|'+str(grasa)+'|'+str(indiceglicemico)+'|'+AlimentoT[int(tipo)-1])
        file.close()
#print "Lista de argumentos: ", sys.argv


""" ------------------------------------------ Modulo del Conocimiento -------------------------------------------------- """

class Alimento(object):
        """docstring for Alimento"""
        def __init__(self, nombre, caloria, proteina, hidratos, grasa,indiceglicemico, tipo):
                super(Alimento, self).__init__()
                self.nombre = nombre
                self.caloria = caloria
                self.proteina = proteina
                self.hidratos = hidratos
                self.grasa = grasa
                self.indiceglicemico=indiceglicemico
                self.tipo = tipo
        def mostrarAlimento(self):
                print ("%s %s %s %s %s %s %s" %(self.nombre, self.caloria, self.proteina, self.hidratos, self.grasa, self.indiceglicemico, self.tipo))
Alimentos=[]
class Perfil(object):
        """docstring for Perfil"""
        def __init__(self, nombre, peso, altura, sexo):
                super(Perfil, self).__init__()
                self.nombre = nombre
                self.peso = peso
                self.altura = altura
                self.sexo = sexo
        def imc(self):
                return self.peso/pow(self.altura,2)
perfiles=[]

        
def cargaConocimientoAlimentos():
        n=0
        file = open('conocimiento','r')
        while True:
                pass
                n=n+1
                linea = file.readline()
                if not linea: break
                alim=linea.split('|')
                Alimentos.append(Alimento(alim[0], alim[1], alim[2], alim[3], alim[4], alim[5], alim[6]))
cargaConocimientoAlimentos()
def cargaConocimientoPerfiles():
        file=open ('Perfiles','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                per=linea.split('|')
                perfiles.append(Perfil(per[0], float(per[1]), float(per[2]), per[3]))
cargaConocimientoPerfiles()


def OAV():
        OAV = open('OAV','w')
        file = open('conocimiento','r')
        while True:
                pass
                linea = file.readline()
                if not linea: break
                alim=linea.split('|')
                OAV.write('Objeto               Atributo                        Valor')
                OAV.write('\nAlimento   Nombre                          '+alim[0])
                OAV.write('\nAlimento   Calorias                        '+alim[1])
                OAV.write('\nAlimento   Proteinas                       '+alim[2])
                OAV.write('\nAlimento   Carbohidratos           '+alim[3])
                OAV.write('\nAlimento   Grasas                          '+alim[4])
                OAV.write('\nAlimento   Indice Glicemico        '+alim[5])
                OAV.write('\nAlimento   Tipo                            '+alim[6])
                OAV.write('\n\n\n')
        OAV.close()
        file.close()
OAV()
def Recordar(nombre,peso,altura,sexo):
        file= open('Perfiles','a')
        file.write('\n')
        file.write(str(nombre)+'|'+str(peso)+'|'+str(altura)+'|'+str(sexo))
        file.close()
        
        
""" ------------------------------------------ Modulo de Inferencia -------------------------------------------------- """
def pesoIdeal(sexo, altura):
    if ('hombre' in sexo):
        return (((altura*100) - 150)* 0.75)+50
    elif ('mujer' in sexo):
        return (((altura*100) - 150)* 0.6)+50
def Desconocido(nombre):
        for x in range(len(perfiles)):
                pass
                if (nombre==perfiles[x].nombre):
                        return perfiles[x]
                elif (x==len(perfiles) and nombre!=perfiles[x].nombre):
                        return False
def alimento(dias,numerodia,semana,tipoalimento):
        #tipo_comida=['desayuno', 'media mañana', 'comida', 'merienda', 'cena']
        diasl=int(dias)*7
        reposteria=[]
        pescados=[]
        carnes_huevos=[]
        frutas_verduras_cereales=[]
        comidas_elaboradas=[]
        frutas=[]
        semillas=[]
        for x in range(len(Alimentos)):
                pass
                if ('Dulces y Reposteria' in Alimentos[x].tipo):
                        pass
                        reposteria.append(Alimentos[x])
                if ('Pescados y Mariscos' in Alimentos[x].tipo):
                        pass
                        pescados.append(Alimentos[x])
                if ('Carnes y Derivados' in Alimentos[x].tipo or 'Huevos' in Alimentos[x].tipo):
                        pass
                        carnes_huevos.append(Alimentos[x])
                if ('Verduras y Legumbres' in Alimentos[x].tipo or 'Frutas' in Alimentos[x].tipo) or 'Cereales y Derivados' in Alimentos[x].tipo:
                        pass
                        frutas_verduras_cereales.append(Alimentos[x])
                if ('Comidas Elaboradas' in Alimentos[x].tipo):
                        pass
                        comidas_elaboradas.append(Alimentos[x])
                if ('Frutas' in Alimentos[x].tipo):
                        pass
                        frutas.append(Alimentos[x])
                if ('Semillas' in Alimentos[x].tipo):
                        pass
                        semillas.append(Alimentos[x])
        if (tipoalimento=='desayuno'):
                pass
                return random.choice(frutas_verduras_cereales)
        elif(tipoalimento=='media mañana'):
                return random.choice(semillas)
        elif(tipoalimento=='merienda'):
                return random.choice(frutas)
        elif(tipoalimento=='cena'):
                return random.choice(frutas_verduras_cereales)
        elif(tipoalimento=='comida'):
                if (numerodia<=4):
                        semana=pescados+carnes_huevos
                        return random.choice(pescados)
                elif (numerodia>=5 and numerodia<7):
                        return random.choice(carnes_huevos)
                elif (numerodia==30):
                        return random.choice(comidas_elaboradas)
                else:
                        return random.choice(carnes_huevos)

        
def actividad(calorias):
        porcentaje=(calorias*20)/100
        print ('Usted debe quemar %s calorias'%(calorias+porcentaje))
        print ('%s calorias consumidas mas el 20 porciento  recomendable para perder peso' %(calorias))
        #http://enforma.salud180.com/nutricion-y-ejercicio/10-de-ejercicios-que-queman-mas-calorias
        tiempo=((calorias+porcentaje)/450)*8
        print ('Actividad correr por %s minutos'%(tiempo))
        print ('______________________________________________________________________________')


ndia=0

def semana(perfil):
        global ndia
        caloriasdiarias=0
        print (int(perfil.peso-pesoIdeal(perfil.sexo, perfil.altura)))
        dias=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
        tipo_comida=['desayuno', 'media mañana', 'comida', 'merienda', 'cena']



        if (perfil.imc()<=18):
                for x in range (int(pesoIdeal(perfil.sexo, perfil.altura)-perfil.peso)):
                        print ('###############################################################')
                        print ('SEMANA %s                                                     #' %(x+1))
                        print ('###############################################################')
                        for z in range(len(dias)):
                                pass
                                print (dias[z])
                                for y in range(5):
                                        pass
                                        ndia=ndia+1
                                        alim=alimento(pesoIdeal(perfil.sexo, perfil.altura)-perfil.peso,ndia,x,tipo_comida[y])
                                        print (tipo_comida[y]+' '+alim.nombre)
                                print ('______________________________________________________________________________')
        else:

                for x in range (int(perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))):
                        print ('###############################################################')
                        print ('SEMANA %s                                                     #' %(x+1))
                        print ('###############################################################')
                        for z in range(len(dias)):
                                pass
                                print (dias[z])
                                for y in range(5):
                                        pass
                                        ndia=ndia+1
                                        alim=alimento(perfil.peso-pesoIdeal(perfil.sexo, perfil.altura),ndia,x,tipo_comida[y])
                                        print (tipo_comida[y]+' '+alim.nombre)
                                        caloriasdiarias=caloriasdiarias+int(alim.caloria)
                                #print '\n'
                                actividad(caloriasdiarias)
                                caloriasdiarias=0


def dieta(perfil):
        #peso Insuficiente
        if (perfil.imc()<=18):
                print ('Mi recomendacion para ti:')
                semana(perfil)
     
        #peso Normal                                                                                                                                                                                     #
        ##########################################################################################################
        elif(perfil.imc()>18 and perfil.imc() <=24.9):
                reposteria=[]
                pescados=[]
                carnes_huevos=[]
                frutas_verduras_cereales=[]
                for x in range(len(Alimentos)):
                        pass
                        #print Alimentos[x].tipo
                        if ('Dulces y Reposteria' in Alimentos[x].tipo):
                                pass
                                reposteria.append(Alimentos[x].nombre)
                        if ('Pescados y Mariscos' in Alimentos[x].tipo):
                                pass
                                pescados.append(Alimentos[x].nombre)
                        if ('Carnes y Derivados' in Alimentos[x].tipo or 'Huevos' in Alimentos[x].tipo):
                                pass
                                carnes_huevos.append(Alimentos[x].nombre)
                        if ('Verduras y Legumbres' in Alimentos[x].tipo or 'Frutas' in Alimentos[x].tipo) or 'Cereales y Derivados' in Alimentos[x].tipo:
                                pass
                                frutas_verduras_cereales.append(Alimentos[x].nombre)

                print ('Mi recomendacion para ti:')
                print ("""Usted puede alimentarse alguna vez al mes:""")
                for x in range(len(reposteria)):
                        pass
                        print (reposteria[x])
                print ('(en pequeñas cantidades usted puede consumir mas frecuentemente)')
                print ("""Usted puede alimentarse alguna vez ala semana:""")
                for x in range(len(carnes_huevos)):
                        pass
                        print (carnes_huevos[x])
                print ("""Usted puede alimentarse alguna vez 3 o 4 veces a la semana:""")
                for x in range(len(pescados)):
                        pass
                        print (pescados[x])
                print ('usted puede consumir todos los dias:')
                for x in range(len(frutas_verduras_cereales)):
                        pass
                        print (frutas_verduras_cereales[x]              )


        #Sobrepeso I
        ##########################################################################################################      
        elif (perfil.imc()>=25 and perfil.imc()<=26.9):
                print ('Mi recomendacion para ti:')
                semana(perfil)
        #Sobrepeso II
        elif (perfil.imc()>=27 and perfil.imc()<=29.9):
                print ('Mi recomendacion para ti:')
                semana(perfil)
        #Obesidad Tipo I
        elif (perfil.imc()>=30 and perfil.imc()<= 34.9):
                print ('Mi recomendacion para ti:')
                semana(perfil)
        #Obesidad Tipo II
        elif (perfil.imc()>=35 and perfil.imc()<=39.9):
                print ('Mi recomendacion para ti:')
                semana(perfil)
        #Obesidad Tipo III
        elif (perfil.imc()>=40 and perfil.imc() <= 49.9):
                print ('Mi recomendacion para ti:')
                semana(perfil)
        #Obesidad Extrema
        elif (perfil.imc()>=50):
                print ('Mi recomendacion para ti:')
                semana(perfil)

                

""" ------------------------------------------ Modulo de Explicación -------------------------------------------------- """
def valoracion(perfil):
        #print pesoIdeal(perfil.sexo, perfil.altura)
        if (perfil.imc()<=18):
                return """Tu peso es insuficiente
Bajo Peso
Ello quiere decir que tu peso %s es insuficiente del recomendado para tu estatura %s debido a que tu indice de masa corporal es de %s
por lo que debererías seguir un plan encaminado a obtener un peso apto para ti y una correcta nutrición.
tu peso ideal deberia ser %s"""%(perfil.peso,perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura))
        elif(perfil.imc()>18 and perfil.imc() <=24.9):
            return """En este momento te encuentras en una situacion de Normal de Peso
                                Tu peso %s es adecuado u optimo para tu estatura %s debido a que usted tiene un indice de masa corporal de %s.""" %(perfil.peso,perfil.altura, perfil.imc())
        elif (perfil.imc()>=25 and perfil.imc()<=26.9):
            return """
                                        En este momento te encuentras en una situación de
                        Sobrepeso I
                        
                        Ello quiere decir que tu peso está por encima del recomendado para tu estatura %s y debido a tu indice de masa corporar %s. Accede cuanto antes a inciciar tu plan y verás qué sencillo te resulta.
                        Tu peso ideal deberia ser %s.
                        por lo que estas pasado por %f kilos"""%(perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        elif (perfil.imc()>=27 and perfil.imc()<=29.9):
            return """
                                        En este momento te encuentras en una situación de
                        Sobrepeso II
                        
                        p>Pre-obesidad. Ello quiere decir que tu peso %s está por encima del recomendado para tu estatura %s tu indice de masa corporal es de %s. Accede cuanto antes a inciciar tu plan y verás qué sencillo te resulta.
                        Tu peso ideal deberia ser %s por lo que estas pasado por %f kilos"""%(perfil.peso,perfil.altura, perfil.imc(),pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        elif (perfil.imc()>=30 and perfil.imc()<= 34.9):
            return """
                                        En este momento te encuentras en una situación de
                        Obesidad Tipo I
                        
                        Ello significa que tu peso %s está por encima del recomendado para tu estatura %s debido a que usted tiene un indice de masa corporal de %s, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
                        Tu peso ideal deberia ser %s por lo que estas pasado por %f kilos"""%(perfil.peso,perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        elif (perfil.imc()>=35 and perfil.imc()<=39.9):
            return """
                                        En este momento te encuentras en una situación de
                        Obesidad Tipo II
                        
                        Ello significa que tu peso %s está por encima del recomendado para tu estatura %s debido a que usted tiene un indice de masa corporal de %s, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
                        Tu peso ideal deberia ser %s por lo que estas pasado por %f kilos"""%(perfil.peso,perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        elif (perfil.imc()>=40 and perfil.imc() <= 49.9):
            return """
                                        En este momento te encuentras en una situación de
                        Obesidad Tipo III
                        
                        Ello significa que tu peso %s está por encima del recomendado para tu estatura %s debido a que usted tiene un indice de masa corporal de %s, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
                        Tu peso ideal deberia ser %s por lo que estas pasado por %f kilos"""%(perfil.peso,perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        elif (perfil.imc()>=50):
            return """
                                        En este momento te encuentras en una situación de
                        Obesidad Extrema
                        
                        Ello significa que tu peso %s está por encima del recomendado para tu estatura %s debido a que usted tiene un indice de masa corporal de %s, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
                        Tu peso ideal deberia ser %s por lo que estas pasado por %f kilos"""%(perfil.peso,perfil.altura, perfil.imc(), pesoIdeal(perfil.sexo, perfil.altura),perfil.peso-pesoIdeal(perfil.sexo, perfil.altura))
        
def main():
        print ("##############################################################")
        print ("#                           Healthy Body                                         #")
        print ("##############################################################")
        print ("Hola antes de empezar porfavor contastame unas preguntas")
        nombre=input('Cual es tu Nombre>:')
        conosco=Desconocido(nombre)
        if (conosco):
                print ('Hola %s como has estado'%(conosco.nombre))
                peso_new=input('dime %s cuanto pesas ahora>:'%(conosco.nombre))
                print ('muy bien')
                conosco.peso=float(peso_new)
                print ("%s %s" %(conosco.nombre,valoracion(conosco)))
                dieta(conosco)
                #print conosco
        else:
                peso=input('Cual es tu Peso en kilogramos>:')
                altura=input('Cual es tu altura en metros>:')
                sexo=input('Cual es tu sexo (hombre/mujer)>:')

                perfiles.append(Perfil(nombre, float(peso), float(altura), sexo))
                Recordar(nombre, float(peso), float(altura), sexo)
                print ("%s %s" %(nombre,valoracion(perfiles[len(perfiles)-1])))
                dieta(perfiles[len(perfiles)-1])


if __name__ == '__main__':
        #print sys.argv
        if (len(sys.argv)>=2 and sys.argv[1]=='--ingeniero'):
                ingeniero()
        else:
                main()