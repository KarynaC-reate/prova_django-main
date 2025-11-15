CREATE DATABASE IF NOT EXISTS prova_django;
USE prova_django;
drop database prova_django;

-- 1. Tabela GeneroTextual (Tabela Principal de Categorias)
CREATE TABLE GeneroTextual (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nome_genero VARCHAR(100) NOT NULL UNIQUE,
    descricao VARCHAR(255)
) ENGINE=InnoDB;

-- 2. Tabela TipoAssunto (Tabela de Metadados/Tags)
CREATE TABLE TipoAssunto (
    id_tipo_assunto INT AUTO_INCREMENT PRIMARY KEY,
    nome_assunto VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- 3. Tabela Documento (Tabela de Textos)
CREATE TABLE Documento (
    id_documento INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    conteudo_texto TEXT NOT NULL,
    data_publicacao DATE,
    -- Chave Estrangeira (FK) que liga o Documento ao seu Gênero
    fk_genero INT, 
    FOREIGN KEY (fk_genero) REFERENCES GeneroTextual(id_genero)
        ON DELETE RESTRICT -- Impede a exclusão de um Gênero se houver Documentos associados
        ON UPDATE CASCADE -- Atualiza a FK em Documento se a PK em GeneroTextual for alterada
) ENGINE=InnoDB;
