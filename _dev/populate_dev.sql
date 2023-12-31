INSERT INTO classe (nome) VALUES
	 ('Metal'),
	 ('Papel'),
	 ('Orgânico');

INSERT INTO destinacao (nome) VALUES
	 ('Reciclagem'),
	 ('Aterro'),
	 ('Incineração');

INSERT INTO fornecedor (nome, tp_fornecedor) VALUES
	 ('Eko Sustentável','Resíduos'),
	 ('Reciclar+','Resíduos'),
	 ('Incinerar & Reciclar','Resíduos'),
	 ('TerraSustentável','Resíduos'),
	 ('Lux','Eletricidade'),
	 ('SABESP','Água'),
	 ('Shell','Combustível');

INSERT INTO fornecedor_destinacao (fornecedor_id,destinacao_id) VALUES
	 (1,1),
	 (2,1),
	 (3,1),
	 (3,3),
	 (4,1),
	 (4,2),
	 (1,3);

INSERT INTO localidade (nome) VALUES
	 ('São Paulo'),
	 ('Minas Gerais');

INSERT INTO saida (data,peso,custo,n_evidencia,cdf,id_classe,id_destinacao,id_fornecedor,id_cluster,receita) VALUES
	 ('2023-01-01',15,50,'000111','000111',1,1,2,1,5),
	 ('2023-01-02',20,100,'000222','000222',3,2,3,1,0),
	 ('2023-02-01',30,15,'000333','000333',1,1,1,2,0),
	 ('2023-01-03',10,15,'000444','000444',1,1,2,1,2);

INSERT INTO entrada (data,peso,id_classe,id_cluster) VALUES
	 ('2023-01-01',50,1,1),
	 ('2023-01-01',30,1,1),
	 ('2023-01-01',50,2,2),
	 ('2023-02-01',20,1,1),
	 ('2023-02-01',10,1,1),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',20,1,2),
	 ('2023-02-01',15,1,2),
	 ('2023-04-10',500,3,1),
	 ('2023-01-01',50,1,1),
	 ('2023-01-01',30,1,1),
	 ('2023-01-01',50,2,2),
	 ('2023-02-01',20,1,1),
	 ('2023-02-01',10,1,1),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',20,1,2),
	 ('2023-02-01',15,1,2),
	 ('2023-04-10',500,3,1),
	 ('2023-01-01',50,1,1),
	 ('2023-01-01',30,1,1),
	 ('2023-01-01',50,2,2),
	 ('2023-02-01',20,1,1),
	 ('2023-02-01',10,1,1),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',20,1,2),
	 ('2023-02-01',15,1,2),
	 ('2023-04-10',500,3,1),
	 ('2023-01-01',50,1,1),
	 ('2023-01-01',30,1,1),
	 ('2023-01-01',50,2,2),
	 ('2023-02-01',20,1,1),
	 ('2023-02-01',10,1,1),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',20,1,2),
	 ('2023-02-01',15,1,2),
	 ('2023-04-10',500,3,1),
	 ('2023-01-01',50,1,1),
	 ('2023-01-01',30,1,1),
	 ('2023-01-01',50,2,2),
	 ('2023-02-01',20,1,1),
	 ('2023-02-01',10,1,1),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',10,2,2),
	 ('2023-02-01',20,1,2),
	 ('2023-02-01',15,1,2),
	 ('2023-04-10',500,3,1);

