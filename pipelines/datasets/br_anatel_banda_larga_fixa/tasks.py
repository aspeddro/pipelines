# -*- coding: utf-8 -*-
"""
Tasks for br_anatel_banda_larga_fixa
"""
import pandas as pd
import numpy as np
from zipfile import ZipFile
from pathlib import Path


from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from prefect import task

from pipelines.utils.utils import (
    to_partitions,
    log,
)
from pipelines.datasets.br_anatel_banda_larga_fixa.utils import (
    check_and_create_column,
    download_file,
    extract_file,
)
from pipelines.constants import constants


@task(
    max_retries=constants.TASK_MAX_RETRIES.value,
    retry_delay=timedelta(seconds=constants.TASK_RETRY_DELAY.value),
)
def treatment():
    url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"

    download_dir = "/tmp/data/input"

    download_file(url=url, download_dir=download_dir)

    anos = ["2023"]

    filepath = "/tmp/data/input/acessos_banda_larga_fixa.zip"

    # ! Abrindo o arquivo zipado
    with ZipFile(filepath) as z:
        # ! Iterando sobre a lista de anos
        for ano in anos:
            # ! Abrindo o arquivo csv dentro do zip pelo ano
            with z.open(f"Acessos_Banda_Larga_Fixa_{ano}.csv") as f:
                # ! Lendo o arquivo csv
                df = pd.read_csv(f, sep=";", encoding="utf-8")

                # ! Fazendo referencia a função criada anteriormente para verificar colunas
                df = check_and_create_column(df, "Tipo de Produto")

                # ! Renomeando as colunas
                df.rename(
                    columns={
                        "Ano": "ano",
                        "Mês": "mes",
                        "Grupo Econômico": "grupo_economico",
                        "Empresa": "empresa",
                        "CNPJ": "cnpj",
                        "Porte da Prestadora": "porte_empresa",
                        "UF": "sigla_uf",
                        "Município": "municipio",
                        "Código IBGE Município": "id_municipio",
                        "Faixa de Velocidade": "velocidade",
                        "Tecnologia": "tecnologia",
                        "Meio de Acesso": "transmissao",
                        "Acessos": "acessos",
                        "Tipo de Pessoa": "pessoa",
                        "Tipo de Produto": "produto",
                    },
                    inplace=True,
                )

                # ! organização das variáveis
                df.drop(["grupo_economico", "municipio"], axis=1, inplace=True)

                # ! Reordenando as colunas
                df = df[
                    [
                        "ano",
                        "mes",
                        "sigla_uf",
                        "id_municipio",
                        "cnpj",
                        "empresa",
                        "porte_empresa",
                        "tecnologia",
                        "transmissao",
                        "velocidade",
                        "produto",
                        "acessos",
                    ]
                ]

                # ! Classificação do DataFrame em ordem crescente
                df.sort_values(
                    [
                        "ano",
                        "mes",
                        "sigla_uf",
                        "id_municipio",
                        "cnpj",
                        "empresa",
                        "porte_empresa",
                        "tecnologia",
                        "transmissao",
                        "velocidade",
                    ],
                    inplace=True,
                )
                # ! substituindo valores nulos por vazio
                df.replace(np.nan, "", inplace=True)
                # ! Retirando os acentos da coluna "transmissao"
                df["transmissao"] = df["transmissao"].apply(
                    lambda x: x.replace("Cabo Metálico", "Cabo Metalico")
                    .replace("Satélite", "Satelite")
                    .replace("Híbrido", "Hibrido")
                    .replace("Fibra Óptica", "Fibra Optica")
                    .replace("Rádio", "Radio")
                )

                df["acessos"] = df["acessos"].apply(lambda x: str(x).replace(".0", ""))

                df["produto"] = df["produto"].apply(
                    lambda x: x.replace("LINHA_DEDICADA", "linha dedicada").lower()
                )

                savepath = "/tmp/data/microdados.csv"
                # ! Fazendo referencia a função criada anteriormente para particionar o arquivo o arquivo
                to_partitions(
                    df,
                    partition_columns=["ano", "mes", "sigla_uf"],
                    savepath=savepath,
                )

    # ! retornando o caminho do path
    return savepath


@task(
    max_retries=constants.TASK_MAX_RETRIES.value,
    retry_delay=timedelta(seconds=constants.TASK_RETRY_DELAY.value),
)
def treatment_br():
    # ! Baixando a pasta zipada no diretório "/tmp/data/input"
    url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"
    download_dir = "/tmp/data/input"
    download_file(url=url, download_dir=download_dir)

    # ! Extrair o arquivo zipado no diretório "/tmp/data/input"
    filepath = "/tmp/data/input/acessos_banda_larga_fixa.zip"
    extract_dir = "/tmp/data/input"
    extract_file(filepath=filepath, extract_dir=extract_dir)

    # ! Abrindo o arquivo csv
    file = "/tmp/data/input/Densidade_Banda_Larga_Fixa.csv"
    df = pd.read_csv(file, sep=";", encoding="utf-8")

    # ! Tratando o csv
    df.rename(columns={"Nível Geográfico Densidade": "Geografia"}, inplace=True)
    df_brasil = df[df["Geografia"] == "Brasil"]
    df_brasil = df_brasil.drop(["UF", "Município", "Geografia", "Código IBGE"], axis=1)
    df_brasil["Densidade"] = df_brasil["Densidade"].apply(
        lambda x: float(x.replace(",", "."))
    )
    df_brasil.rename(
        columns={"Ano": "ano", "Mês": "mes", "Densidade": "densidade"},
        inplace=True,
    )

    # ! Salvando o csv tratado
    path = "/tmp/data/densidade_brasil.csv"
    df_brasil.to_csv(path, sep=",", index=False, encoding="utf-8")

    return path


@task(
    max_retries=constants.TASK_MAX_RETRIES.value,
    retry_delay=timedelta(seconds=constants.TASK_RETRY_DELAY.value),
)
def treatment_uf():
    # ! Baixando a pasta zipada no diretório "/tmp/data/input"
    url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"
    download_dir = "/tmp/data/input"
    download_file(url=url, download_dir=download_dir)

    # ! Extrair o arquivo zipado no diretório "/tmp/data/input"

    filepath = "/tmp/data/input/acessos_banda_larga_fixa.zip"
    extract_dir = "/tmp/data/input"
    extract_file(filepath=filepath, extract_dir=extract_dir)

    # ! Abrindo o arquivo csv
    file = "/tmp/data/input/Densidade_Banda_Larga_Fixa.csv"
    df = pd.read_csv(file, sep=";", encoding="utf-8")
    df.rename(columns={"Nível Geográfico Densidade": "Geografia"}, inplace=True)
    df_uf = df[df["Geografia"] == "UF"]
    df_uf.drop(["Município", "Código IBGE", "Geografia"], axis=1, inplace=True)
    df_uf["Densidade"] = df_uf["Densidade"].apply(lambda x: float(x.replace(",", ".")))
    df_uf.rename(
        columns={
            "Ano": "ano",
            "Mês": "mes",
            "UF": "sigla_uf",
            "Densidade": "densidade",
        },
        inplace=True,
    )

    # ! Salvando o csv tratado
    path = "/tmp/data/densidade_brasil.csv"
    df_uf.to_csv(path, sep=",", index=False, encoding="utf-8")

    return path


@task(
    max_retries=constants.TASK_MAX_RETRIES.value,
    retry_delay=timedelta(seconds=constants.TASK_RETRY_DELAY.value),
)
def treatment_municipio():
    # ! Baixando a pasta zipada no diretório "/tmp/data/input"
    url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"
    download_dir = "/tmp/data/input"
    download_file(url=url, download_dir=download_dir)

    # ! Extrair o arquivo zipado no diretório "/tmp/data/input"
    filepath = "/tmp/data/input/acessos_banda_larga_fixa.zip"
    extract_dir = "/tmp/data/input"
    extract_file(filepath=filepath, extract_dir=extract_dir)

    # ! Abrindo o arquivo csv
    file = "/tmp/data/input/Densidade_Banda_Larga_Fixa.csv"
    df = pd.read_csv(file, sep=";", encoding="utf-8")

    # ! Tratando o csv
    df.rename(columns={"Nível Geográfico Densidade": "Geografia"}, inplace=True)
    df_municipio = df[df["Geografia"] == "Municipio"]
    df_municipio.drop(["Município", "Geografia"], axis=1, inplace=True)
    df_municipio["Densidade"] = df_municipio["Densidade"].apply(
        lambda x: float(x.replace(",", "."))
    )
    df_municipio.rename(
        columns={
            "Ano": "ano",
            "Mês": "mes",
            "UF": "sigla_uf",
            "Código IBGE": "id_municipio",
            "Densidade": "densidade",
        },
        inplace=True,
    )
    savepath = "/tmp/data/microdados.csv"

    # ! Fazendo referencia a função criada anteriormente para particionar o arquivo o arquivo
    to_partitions(
        df_municipio,
        partition_columns=["ano", "mes", "sigla_uf"],
        savepath=savepath,
    )

    return savepath