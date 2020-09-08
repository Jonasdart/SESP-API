### [O NOVO SESP](https://github.com/duzzsys/SESP/tree/sesp-1.0) é um sistema 'maleável' ao escopo. Direcionado às gestões de T.I. de empresas.

---

### API REFERÊNCIA

Tipo: REST
Rotas: GET, POST, DELETE, PUT, PATCH

---

## /computers/byinventory

#### GET → 

Informe um numero de inventário na URL e receberá o computador. Apenas pesquisas exatas.

#### PUT → 

Sabendo o número de inventário do computador que deseja alterar informações, passe um json no body da requisição, para executar as seguintes ações:

    1. Alterar o nome do computador, no GLPI. Ação será refletida no computador através do Agente;
    2. Agendar novo inventário e verificação SESP;
    3. Agendar um reinício do computador;
    4. Agendar o desligamento do computador;

**HEADER**

```
{
    "inventory_number": "0222",
    "computer_name"   : "HAT0222",
    "sesp_version"    : "0.0.3-DEV"
}
```



**BODY**
**_JSON:_**

```
{
    "change_name":0,
    "force_inventory": 1,
    "schedule_reboot":0,
    "schedule_shutdown":0
}
```
Nota-se que, todos campos do json são obrigatórios. Quando não desejar realizar a ação "descrita" no mesmo, utiliza-se o 0 como booleano.

---