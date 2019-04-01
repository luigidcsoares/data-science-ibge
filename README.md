# Data Science - IBGE
Repositório de Data Science volta a análise da saúde da população brasileira.

### Instalando as dependências necessárias.

#### Anaconda

  - Instale o [miniconda](https://conda.io/en/latest/miniconda.html)

  - Atualize o conda:
    ```
    $ conda update conda
    ```

  - Crie um ambiente de desenvolvimento, definindo a versão do python a ser utilizada:
    ```
    $ conda create -n env python=3.7.2

    Se preferir, pode definir um caminho customizado:
    $ conda create -p caminho/para/env python=3.7.2
    ```

  - Ative o ambiente de desenvolvimento:
    ```
    $ conda activate env

    Caso tenha definido um caminho alternativo:
    $ conda activate caminho/para/env
    ```

  - Instale as dependências utilizando o arquivo `<requirements.txt>`:
    ```
    $ conda install --yes --file requirements.txt
    ```

  - Para desativar o ambiente:
    ```
    $ conda deactivate
    ```
