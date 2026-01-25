# Automação de Cadastro de Produtos
Projeto de automação desenvolvido em Python para realizar o cadastro automático de produtos em um sistema web, utilizando interação direta com a interface gráfica do sistema.

![Interface de cadastro](https://i.postimg.cc/gJPsNJpk/data-automacao-Cadastrar.webp)

---

*Sobre o Projeto*

Esta automação foi criada para eliminar o cadastro manual de produtos, tornando o processo mais rápido, confiável e escalável.

A automação realiza:
- Acesso ao sistema via navegador
- Login automático com e-mail e senha
- Leitura de uma base de dados com 264 produtos
- Cadastro completo de cada produto no sistema

Cada produto contém as seguintes informações:
- Código do produto
- Marca
- Tipo
- Preço unitário
- Custo
- Observação

*Tecnologias Utilizadas*
- Python
- PyAutoGUI
- Pandas

*Instalação das Dependências*

``pip install pyautogui pandas``

*Execução*

Pré-requisitos:
- Python 3.x instalado
- Sistema operacional com interface gráfica
- Navegador configurado
- Resolução de tela compatível com a automação

Instale os arquivos e rode a aplicação.

***Importante***: Não utilize o computador durante a execução da automação.

*Observações Importantes*
- O PyAutoGUI depende da posição dos elementos na tela
- Alterações no layout do sistema podem exigir ajustes no código
``pyautogui.click(x=411, y=257)``
- Recomenda-se executar em um ambiente controlado



*Licença*

Este projeto é de uso educacional e pode ser adaptado conforme a necessidade.

