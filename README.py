#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `WPS Office` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `WPS Office` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use the `WPS Office` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `WPS Office`
# 
# O `WPS Office` é uma suíte de escritório abrangente e popular, frequentemente considerada uma das principais alternativas ao Microsoft Office. Disponível para várias plataformas, incluindo `Windows`, `Linux`, `Android` e `iOS`, o `WPS Office` oferece um conjunto de ferramentas eficientes para processamento de texto, criação de planilhas e elaboração de apresentações, com compatibilidade estreita com os formatos de arquivo do `Microsoft Office`, como `DOCX`, `XLSX` e `PPTX`. A interface do usuário do `WPS Office` é notavelmente intuitiva e familiar, especialmente para usuários acostumados com o Office da Microsoft, facilitando a migração e adaptação. Além de recursos básicos, ele oferece várias funcionalidades avançadas, como tabulação de documentos, ferramentas de colaboração e a possibilidade de converter PDFs. Embora a versão gratuita do `WPS Office` seja bastante completa, ele também oferece uma versão premium com recursos adicionais, como mais templates e ferramentas de edição avançada, tornando-o uma opção versátil para uso tanto pessoal quanto profissional.
# 

# ## 1. Como configurar/instalar/usar o `WPS Office` no `Linux Ubuntu` [1]
# 
# Para configurar o `WPS Office`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Navegue até o diretório onde o arquivo `.deb` está localizado:** Use o comando cd para navegar até o diretório onde o arquivo `.deb` está localizado. Por exemplo, se o arquivo `.deb` estiver na sua pasta `Downloads`, você pode usar o seguinte comando: `cd ~/Downloads`
# 
# 4. Instale o arquivo `.deb`: Use o comando `dpkg` para instalar o arquivo `.deb`. Substitua "`<nome_do_arquivo>.deb`" pelo nome real do arquivo `.deb` que você deseja instalar: `sudo dpkg -i wps-office_8.1.0.3724~b1p2_i386.deb`
# 
#     Você precisará fornecer sua senha de administrador (`sudo`) para continuar.
# 
# 5. **Resolva as dependências (se necessário)**: Às vezes, a instalação do arquivo `.deb` pode gerar erros devido a dependências ausentes. Se isso acontecer, você pode usar o seguinte comando para tentar resolver as dependências: `sudo apt install -f`
# 
#     O comando acima tentará instalar automaticamente as dependências necessárias para o pacote `.deb` que você está instalando.
# 
# 6. **Verifique a instalação:** Após a conclusão do processo, verifique se o programa ou pacote foi instalado corretamente. Você pode fazer isso procurando o aplicativo no menu de aplicativos ou executando-o a partir do terminal com o comando: `wps`
# 
# Isso deve permitir que você instale um arquivo `.deb` no seu sistema Ubuntu. Lembre-se de que os arquivos .deb são pacotes de software específicos para distribuições baseadas no Debian, como o Ubuntu, e geralmente são seguros de usar, especialmente se você os obtiver de fontes confiáveis. No entanto, sempre esteja ciente da origem dos arquivos .deb que você baixa e evite fontes não confiáveis para garantir a segurança do seu sistema.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `WPS Office` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     cd ~/Downloads
#     sudo dpkg -i wps-office_8.1.0.3724~b1p2_i386.deb
#     sudo apt install -f
#     wps
#     ```
# 

# ## 2. Desinstalar o `WPS Office` no `Linux Ubuntu`
# 
# Para desinstalar o `WPS Office` do `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. **Abra o `Terminal Emulator`:** Pressione no teclado para abrir o `Terminal Emulator`: Ctrl + Alt + T
# 
#     Isso é onde você executará os comandos para desinstalar o `WPS Office`.
# 
# 2. **Execute o comando de desinstalação:** No terminal, execute o seguinte comando para desinstalar o `WPS Office`: `sudo apt remove wps-office`
# 
#     Este comando removerá o pacote do `WPS Office` do seu sistema `Ubuntu`.
# 
# 3. **Limpeza de pacotes não utilizados:** Para garantir que todos os pacotes relacionados ao `WPS Office` sejam removidos, execute também o comando: `sudo apt autoremove -y`
# 
#     Isso removerá quaisquer pacotes desnecessários que foram instalados como dependências do `WPS Office`.
# 
# 4. **Limpe os arquivos de configuração:** Se desejar remover também os arquivos de configuração do `WPS Office`, você pode executar o seguinte comando: `rm -rf ~/.config/Kingsoft`
# 
#     Este comando removerá o diretório de configuração do `WPS Office` para o seu usuário.
# 
# Após seguir estas etapas, o `WPS Office` deve ser completamente removido do seu sistema Ubuntu. Certifique-se de verificar se todos os vestígios do aplicativo foram removidos, como ícones do menu ou entradas de inicialização, se necessário.

# ## Referências
# 
# [1] OPENAI. ***Instalar arquivo .sh no ubuntu:*** Disponível em: <https://chat.openai.com/c/073320a8-7cc5-4590-9da0-d2bcc7093c88> (texto adaptado). ChatGPT. Acessado em: 17/10/2023 16:05.
# 
# [2] OPENAI. ***VS code: editor popular:*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 28/11/2023 11:18.
# 
