# Rispar Teste

### Requisitoes para executar a aplicação:
    - Para executar localmente é necessario a versão do python 3.6+
    - Para executar com docker é necessario o docker e o docker-compose

### Como Executar
Para executar localmente.

```sh
$ python3 rispartest.py contas.csv transacoes.csv
```

Para executar com docker

```sh
$ docker-compose run risparteste python rispartest.py contas.csv transacoes.csv
```
