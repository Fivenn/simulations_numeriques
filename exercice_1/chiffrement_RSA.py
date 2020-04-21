def chiffre(n, c, msg):
	# Conversion du message en codes ascii	
	msgAsci = [str(ord(j)) for j in msg]
	# Ajout des zéros, pour avoir une longueur fixe (3) de chaque code msgAscicii
	for i, k in enumerate(msgAsci):
		if len(k) < 4:		
			while len(k) < 4:
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

	# il faut retransformer les blocs en code ascii
	for i, s in enumerate(resultat):
		if len(s) < 4:
			while len(s) < 4:
				s = '0' + s
			resultat[i] = s

	#on refait des groupes de 3 et on les convertie directement en ascii
	g = ''.join(resultat)
	asci = ''
	d , f = 0 , 4
	while f <= len(g):
		asci = asci + chr(int(g[d:f])) #conversion ascii
		d , f = f , f + 4
	
	return asci 

def main():
	# p et q les deux nombres premier distincts
	p = 61
	q = 53

	# le module de chiffrement n = p*q
	n = p * q

	# La valeur de l'indicatrice d'Euler en n
	# indicatriceEuler = (p - 1)*(q - 1)

	# Exposant de chiffrement premier avec l'indicatrice d'euler
	e = 17

	# Exposant de dechiffrement, l'inverse de e % indicatriceEuler 
	d = 413

	# le messsage à chiffre
	msg = "message"

	msgChiffre = chiffre(n, e, msg)
	print("Message à chiffrer :")
	print(msg)

	print("Message dechiffré :")
	print(dechiffre(n, d, msgChiffre))

if __name__ == "__main__":
	main()