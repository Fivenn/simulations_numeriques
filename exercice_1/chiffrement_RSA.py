def chiffre(n, c, msg):
	# Conversion du message en codes ascii	
	msgAsci = [str(ord(j)) for j in msg]
	# Ajout des zéros, pour avoir une longueur fixe (3) de chaque code msgAscicii
	for i, k in enumerate(msgAsci):
		if len(k) < 3:		
			while len(k) < 3:
				k = '0' + k
			msgAsci[i] = k

	msgAsci = ''.join(msgAsci)
	d , f = 0 , 4

	#on s'assure que la longeur de msgAsci soit un multiple de f 
	while len(msgAsci)%f != 0: 
		msgAsci = msgAsci + '0'

	# on regroupe les nombres (les codes ascii) en groupe de 4
	blocks = []
	while f <= len(msgAsci):
		blocks.append(msgAsci[d:f])
		d , f = f , f + 4
	
	msgChiffre = []

	#chiffrement des groupes
	for i in blocks:
		msgChiffre.append(str(((int(i)**c)%n)))
	
	return msgChiffre
	
def dechiffre(n, d, msgChiffre):
	"""*crypt est une liste des blocks à déchiffrer"""
	
	#dechiffrage des blocs
	resultat = []
	for i in msgChiffre:
		resultat.append(str(((int(i)**d)%n)))

	print(resultat)
	# il faut retransformer les blocs en code ascii
	return ""

def main():
	# p et q les deux nombres premier distincts
	p = 3
	q = 11

	# le module de chiffrement n = p*q
	n = p * q

	# La valeur de l'indicatrice d'Euler en n
	# indicatriceEuler = (p - 1)*(q - 1)

	# Exposant de chiffrement premier avec l'indicatrice d'euler
	e = 3

	# Exposant de dechiffrement, l'inverse de l'inverse de e % indicatriceEuler 
	d = 7 

	# le messsage à chiffre
	msg = "message"

	msgChiffre = chiffre(n, e, msg)
	print(msgChiffre)
	print(dechiffre(n, d, msgChiffre))

if __name__ == "__main__":
	main()