CREATE DATABASE dbBid;
USE dbBid;

CREATE TABLE tblTime(
	idTime INT PRIMARY KEY AUTO_INCREMENT,
	nomeTime VARCHAR(40)
);

CREATE TABLE tblJogador(
	idJogador INT PRIMARY KEY AUTO_INCREMENT,
	numeroJogador INT,
	nomeJogador VARCHAR(40),
	posicao CHAR(3),
	fkTime INT,
	FOREIGN KEY(fkTime) REFERENCES tblTime(idTime)
);

INSERT INTO tblTime VALUES(NULL, 'São Paulo FC'),
						  (NULL, 'Santos FC'),
						  (NULL, 'Fortaleza EC'),
						  (NULL, 'CR Vasco da Gama');
