CREATE TABLE candidatos(  
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    numero INT,
    cargo TEXT,
    nome TEXT
);

INSERT INTO candidatos VALUES (null, 6969, 'Presidente', 'Travis Scott'),(null, 1010, 'Senador', 'Madonna'),(null, 1111, 'Senador', 'Michael Jackson'),(null, 1212, 'Senador', 'Batman'),(null, 1313, 'Senador', 'Naruto');

INSERT INTO candidatos VALUES (null, 6969, 'Prefeito', 'Travis Scott'),(null, 1010, 'Senador', 'Madonna'),(null, 1111, 'Senador', 'Michael Jackson'),(null, 1212, 'Senador', 'Batman'),(null, 1313, 'Senador', 'Naruto');

INSERT INTO candidatos VALUES (null, 6969, 'Governador', 'Travis Scott'),(null, 1010, 'Senador', 'Madonna'),(null, 1111, 'Senador', 'Michael Jackson'),(null, 1212, 'Senador', 'Batman'),(null, 1313, 'Senador', 'Naruto');

INSERT INTO candidatos VALUES (null, 6969, 'Senador', 'Travis Scott'),(null, 1010, 'Senador', 'Madonna'),(null, 1111, 'Senador', 'Michael Jackson'),(null, 1212, 'Senador', 'Batman'),(null, 1313, 'Senador', 'Naruto');

SELECT * from candidatos;