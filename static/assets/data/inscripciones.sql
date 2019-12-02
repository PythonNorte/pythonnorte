
CREATE TABLE IF NOT EXISTS Talleres (
  Codigo VARCHAR(100) UNIQUE,
  Nombre VARCHAR(200),
  PRIMARY KEY (Codigo)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS Inscripciones (
  Id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  CodigoTaller VARCHAR(100) NULL,
  Nombre VARCHAR(200),
  Apellido VARCHAR(200),
  DNI VARCHAR(20),
  Institucion VARCHAR(250),
  Profesion VARCHAR(250),
  Email VARCHAR(250),
  Telefono VARCHAR(16),
  Created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (Id),
  CONSTRAINT fk_Codigo_Talleres
    FOREIGN KEY (CodigoTaller)
    REFERENCES Talleres (Codigo)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE = InnoDB;


INSERT INTO Inscripciones (CodigoTaller, Nombre, Apellido, DNI, Institucion, Profesion, Email, Telefono) VALUES (?, ?, ?, ?, ?, ?, ?, ?)

-- Talleres
INSERT INTO Talleres (Codigo, Nombre) VALUES ('INTRO_PYTHON_CIENTIFICO_HMAYO', 'Introdución a Python Cientifico: Jupyter Notebook y Pandas'),
('INTRO_REDES_NEURONALES_ACURIALE', 'Introdución a Redes Neuronales');

INSERT INTO Talleres (Codigo, Nombre) VALUES ('PYTHON_CIENTIFICO_HMAYO', 'Taller Python Cientifico');


INSERT INTO Talleres (Codigo, Nombre) VALUES ('BIB_OPEN_SOURCE_PANDAS_SASHA_UNSA', 'Taller de Programación con Bibliotecas Open Source');
INSERT INTO Talleres (Codigo, Nombre) VALUES ('BIB_OPEN_SOURCE_PANDAS_SASHA_ZUVIRIA', 'Taller de Programación con Bibliotecas Open Source');
