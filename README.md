# Automação MyCRM com BotCity

Este projeto realiza a automação de uma aplicação desktop chamada **My CRM (Sample App)** utilizando o framework **BotCity**.

## 🧰 Tecnologias utilizadas

- Python 3.x
- BotCity Core
- BotCity Maestro (opcional)
- UI Automation (UIA Backend)

## 📦 Requisitos

- [BotCity Studio](https://botcity.dev) instalado
- Dependências do projeto instaladas:
  ```
  pip install botcity-core
  pip install botcity-maestro-sdk
  ```

- Aplicação `MyCRM.exe` localizada em:
  ```
  C:\Users\vmate\PyCharmMiscProject\Automação-MyCRM\MyCRM\app\MyCRM.exe
  ```

## 🚀 Como usar

1. **Abra o terminal** ou execute via PyCharm.
2. Execute o script principal:

```bash
python nome_do_arquivo.py
```

3. O robô realizará as seguintes ações:
   - Abrirá o aplicativo MyCRM.
   - Preencherá os campos com nome, sobrenome e cidade.
   - Selecionará o gênero e opções do formulário.
   - Fará uma busca por cliente com os dados fornecidos.
   - Fechará a aplicação.

## 🔧 Estrutura do Código

- `bot.execute(path)`: Abre a aplicação.
- `connect_to_app`: Conecta a janela ao backend UIA.
- `menu_select` e `type_keys`: Usados para simular interações humanas.
- `Edit`, `click`, `select`: Identificadores de elementos da interface.

## 📝 Observações

- Certifique-se de que o título da janela do app não tenha mudado.
- Pode ser necessário ajustar os identificadores (`Edit10`, `CustomerLookup`, etc.) conforme a versão da aplicação.
- Descomente `print_control_identifiers()` para descobrir os nomes dos elementos caso tenha problemas.

---

Feito com ❤️ usando BotCity.
