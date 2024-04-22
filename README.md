# Loja Online com Flask e SQLAlchemy

Bem-vindo ao repositório da Loja Online! Aqui você encontrará informações relacionadas ao projeto, tecnologias utilizadas e instruções para explorar o conteúdo.

## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-blue)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-20.0.29-green)](https://www.sqlalchemy.org/)

## Sobre o Projeto

Este repositório contém o projeto de uma loja online desenvolvida com Flask, Python, e SQLAlchemy para a gestão do banco de dados. O projeto visa criar um sistema de e-commerce básico para aprendizado e exploração de tecnologias web.

## Estrutura do Repositório

- **app**: Contém os arquivos principais do aplicativo Flask.
- **models**: Contém os modelos de dados para o SQLAlchemy.
- **static**: Arquivos estáticos como imagens e CSS.
- **templates**: Arquivos de template para renderização do Flask.

## Instruções

1. Clone este repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/maxwelldeveloper7/loja.git
   ```

2. Navegue até o diretório principal do projeto da Loja Online.

   ```bash
   cd loja
   ```

3. Instale as dependências necessárias.

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados no arquivo de configuração do Flask (por exemplo, `config.py`).

5. Execute o servidor Flask para iniciar a aplicação.

   ```bash
   python app.py
   ```

6. Acesse a loja online no seu navegador em `http://127.0.0.1:5000/listar_produtos`.

## Contribuindo

Contribuições são bem-vindas! Se encontrar problemas ou tiver sugestões para melhorias, por favor, abra uma issue neste repositório.

## Notas Importantes

- Certifique-se de ter o Python, Flask, e SQLAlchemy instalados no seu sistema.
- É recomendado o uso de ambientes virtuais para evitar conflitos de dependências.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.