# Importa o bot Desktop padrão da BotCity e o tipo de backend para interação com a interface
from botcity.core import DesktopBot, Backend

# Importa a integração com o Maestro, caso queira usar controle centralizado (não utilizado neste script)
from botcity.maestro import *

# Instancia o bot desktop
bot = DesktopBot()

# Caminho para o executável do aplicativo MyCRM
path = r'C:\Users\vmate\PyCharmMiscProject\Automação-MyCRM\MyCRM\app\MyCRM.exe'

# Executa o aplicativo
bot.execute(path)

# Aguarda 1 segundo (1000 milissegundos) para o app abrir
bot.wait(1000)

# Conecta o robô à aplicação utilizando o backend UI Automation (UIA)
bot.connect_to_app(backend=Backend.UIA, path=path)

# Localiza a janela principal da aplicação com o título "My CRM (Sample App)"
janela_principal = bot.find_app_window(title='My CRM (Sample App)')

# Usa o menu para limpar os campos do formulário
janela_principal.menu_select('File -> Clear Fields')

# Preenche o campo "First Name" com "Victor" usando Alt+T (%{t})
janela_principal.type_keys('%{t} Victor')

# Preenche o campo "Last Name" com "Matheus" usando Alt+L (%{l})
janela_principal.type_keys('%{l} Matheus')

# Preenche o campo de cidade (campo identificado como Edit10)
janela_principal.Edit10.type_keys('Uberladia')

# Seleciona a opção de gênero "Masculino"
janela_principal.Male.click()

# Seleciona várias categorias/checkboxes
janela_principal.Company.select()
janela_principal.Other.select()
janela_principal.People.select()

# Acessa o menu "File -> Open" para abrir a busca de clientes
janela_principal.menu_select('File -> Open')

# Preenche os campos de busca no popup de busca por cliente
# janela_principal.CustomerLookup.print_control_identifiers()  # (Descomente para debugar os controles dessa janela)
janela_principal.CustomerLookup.Edit2.type_keys('Victor')
janela_principal.CustomerLookup.Edit3.type_keys('Matheus')

# Clica no botão "OK" da janela de busca
janela_principal.CustomerLookup.OK.click()

# Fecha a janela principal
janela_principal.Fechar.click()