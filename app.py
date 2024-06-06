import pyperclip
import pyautogui

# SENHAS
pass_admin = "admin"
pass_intelbras = "intelbras"
pass_new = "0x6004VNF@"
ip = "192.168.1.1"

# IP NO NAVEGADOR
pyperclip.copy(ip)
pyautogui.click(438, 50, duration=0.5)

pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')

# USUARIO E SENHA
pyperclip.copy(pass_admin)
pyautogui.click(852, 381, duration=0.5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyperclip.copy(pass_intelbras)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')

# CONFIRMAR NOVA SENHA
pyperclip.copy(pass_new)
pyautogui.click(751, 481, duration=0.5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

pyautogui.hotkey('ctrl', 'v')

pyautogui.click(706, 858, duration=0.2)
pyautogui.click(950, 925, duration=0.1)

# ACESSAR NOVAMENTE COM A NOVA SENHA
#       usuario
pyperclip.copy(pass_admin)
pyautogui.click(852, 381, duration=0.5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

#       senha
pyperclip.copy(pass_new)
pyautogui.hotkey('ctrl', 'v')

pyautogui.hotkey('enter')

pyautogui.click(852, 381, duration=0.5)

# NEGAR ATUALIZACAO DE SENHA
pyautogui.click(1444, 250, duration=0.3)

# ACESSAR CONFIGURACOES
pyautogui.click(1249, 197, duration=0.3)
pyautogui.click(606, 609, duration=0.4)
pyautogui.click(816, 337, duration=0.4)

# ENVIAR ARQUIVO QUE ESTA NO COMPUTADOR
pyautogui.click(564, 158, duration=0.5)
pyautogui.hotkey('enter')

pyautogui.click(762, 379, duration=0.5)
pyautogui.hotkey('enter')

pyautogui.click(1000, 500, duration=0.5)

# VALIDAR QUE BAIXOU


# RECARREGAR A PAGINA
# pyautogui.click(1000, 500, duration=1)
# pyautogui.hotkey('ctrl', 'r')
# pyautogui.hotkey('ctrl', 'r')

# ACESSAR ROTEADOR
#        usuario
# pyperclip.copy(pass_admin)
# pyautogui.click(852, 381, duration=1)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('tab')

#        senha
# pyperclip.copy(pass_new)
# pyautogui.hotkey('ctrl', 'v')

# pyautogui.hotkey('enter')

# pyautogui.click(852, 381, duration=0.5)

# VALIDAR QUE ATUALIZOU

# pyautogui.click(1000, 500, duration=0.5)
