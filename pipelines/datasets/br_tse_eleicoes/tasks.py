# -*- coding: utf-8 -*-
"""
Tasks for br_tse_eleicoes
"""
# pylint: disable=invalid-name
import zipfile
import os
from itertools import product

from prefect import task
from unidecode import unidecode
import pandas as pd


@task
def build_partitions_votacao_zona(anos: list, ufs: list) -> str:
    """
    Build csvs from votacao_zona zip files partitioned by uf and ano
    """
    ufs_anos = product(ufs, anos)

    for uf, ano in ufs_anos:
        dest = f"/tmp/br_tse_eleicoes/detalhes_votacao_secao/sigla_uf={uf}"
        os.system(f"mkdir -p {dest}")
        os.chdir(dest)
        curl_command = f"""
        curl 'https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/votacao_secao_{ano}_{uf}.zip' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Referer: https://dadosabertos.tse.jus.br/' -H 'Connection: keep-alive' -H 'Cookie: _ga=GA1.3.1014844896.1656363652; _gid=GA1.3.955190526.1656363652; _gat=1' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-site' -H 'Sec-Fetch-User: ?1' --output votacao_secao_{ano}_{uf}.zip
        """

        os.system(curl_command)

        with zipfile.ZipFile(f"votacao_secao_{ano}_{uf}.zip", "r") as zip_ref:
            zip_ref.extractall(dest)

        df = pd.read_csv(f"votacao_secao_{ano}_{uf}.csv", sep=";")
        df.columns = [unidecode(col) for col in df.columns]
        df.to_csv(f"votacao_secao_{ano}_{uf}.csv", sep=";", index=False)

        os.system(f"rm votacao_secao_{ano}_{uf}.zip")
        os.system("rm *pdf")

    os.system("tree /tmp/br_tse_eleicoes/detalhes_votacao_secao/")

    return "/tmp/br_tse_eleicoes/detalhes_votacao_secao/"
