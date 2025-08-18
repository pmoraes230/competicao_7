# Senac music hall

O Senac music hall é um sistema voltado ao gerenciamento da casa de show de mesmo nome que fica na cidade de Brasilia - DF. O sistema tem a função de cadastrar, listar, atualizar e deletar: Eventos, setores de cada evento, usuários e também somente cadastrar clientes. Além de também fazer a função de venda e emissão de ingressos para os eventos.

## Funcionalidades
- Cadastro de funcionários (Usuários)
- Separação de funcionários por perfil de acesso
- Cadastro de eventos
- Cadastro de setores por evento
- Exibição de eventos que vão acontecer
- Venda e emissão de ingressos por evento
- Validação e cancelamento de ingressos emitidos
- Dashboard administrativo com gráfico mostrando a venda de cada evento

## Screanshots
![App Screanshots](./home/static/images/image.png)

## Instalação do projeto local

Crie um ambiente virtual
```bash
    virtualenv venv
```

Ative o ambiente virtual
```bash
    venv\Scripts\activate
```

Instale o arquivo requiments.txt com os pacotes necessários para o projeto rodar
```bash
    pip install -r requiments.txt
```

Rode o sistema em sua máquina
```bash
    python manage.py runserver
```

## Váriaveis de ambiente
Para o projeto rodar corretamente, se é preciso adicionar as seguintes variáveis de ambiente no seu arquivo .env

`SECRET_KEY`

`DATABASE_NAME`

`DATABASE_USER`

`DATABASE_PASSWORD`

`DATABASE_HOST`

`DATABASE_PORT`

## Documentação
- [Prototipo Figma](https://www.figma.com/proto/z4BZ5q7jon5Jx7oXNqXEig/music-hall?node-id=1-114&t=tgCIZOHITqaYy1ti-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A114&show-proto-sidebar=1)