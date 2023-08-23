# -*- coding: utf-8 -*-
"""
Constant values for the datasets projects
"""


from enum import Enum


class constants(Enum):  # pylint: disable=c0103
    """
    Constant values for the br_ms_cnes project
    """

    # to build paths
    PATH = [
        "/tmp/br_ms_cnes/input/",
        "/tmp/br_ms_cnes/output/",
    ]

    # to build paths
    TABLE = [
        "estabelecimento",
        "profissional",
        "equipamento",
        "leito",
        "equipe",
        "estabelecimento_ensino",
        "dados_complementares",
        "estabelecimento_filantropico",
        "gestao_metas",
        "habilitacao",
        "incentivos",
        "regra_contratual",
        "servico_especializado",
    ]

    # to download files from datasus FTP server
    DATABASE_GROUPS = {
        # group: table name
        "CNES": [
            "ST",
            "PF",
            "EQ",
            "LT",
            "EP",
            "EE",
            "DC",
            "EF",
            "GM",
            "HB",
            "IN",
            "RC",
            "SR",
        ],
    }

    COLUMNS_TO_KEEP = {
        # equipamento
        "EP": [
            "CODUFMUN",
            "CNES",
            "TIPEQUIP",
            "CODEQUIP",
            "QT_EXIST",
            "QT_USO",
            "IND_SUS",
            "IND_NSUS",
        ],
        # leito
        "LT": ["CNES", "TP_LEITO", "CODLEITO", "QT_EXIST", "QT_CONTR", "QT_SUS"],
        # equipe
        "EQ": [
            "CODUFMUN",
            "CNES",
            "ID_EQUIPE",
            "TIPO_EQP",
            "NOME_EQP",
            "ID_AREA",
            "NOMEAREA",
            "ID_SEGM",
            "DESCSEGM",
            "TIPOSEGM",
            "DT_ATIVA",
            "DT_DESAT",
            "MOTDESAT",
            "TP_DESAT",
            "QUILOMBO",
            "ASSENTAD",
            "POPGERAL",
            "ESCOLA",
            "INDIGENA",
            "PRONASCI",
        ],
        # profissional
        "PF": [
            "COMPETEN",
            "CNES",
            "UFMUNRES",
            "NOMEPROF",
            "CNS_PROF",
            "CBO",
            "REGISTRO",
            "CONSELHO",
            "TERCEIRO",
            "VINCULAC",
            "VINCUL_C",
            "VINCUL_A",
            "VINCUL_N",
            "PROF_SUS",
            "PROFNSUS",
            "HORAOUTR",
            "HORAHOSP",
            "HORA_AMB",
        ],
        # estabelecimento_ensino
        "EE": [
            "CODUFMUN",
            "CNES",
            "CMPT_INI",
            "CMPT_FIM",
            "SGRUPHAB",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # estabelecimento_filantropico
        "EF": [
            "CODUFMUN",
            "CNES",
            "CMPT_INI",
            "CMPT_FIM",
            "SGRUPHAB",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # gestao_metas
        "GM": [
            "CODUFMUN",
            "CNES",
            "CMPT_INI",
            "CMPT_FIM",
            "SGRUPHAB",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # habilitacao
        "HB": [
            "CODUFMUN",
            "CNES",
            "NAT_JUR",
            "NULEITOS",
            "SGRUPHAB",
            "CMPT_INI",
            "CMPT_FIM",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # incentivos
        "IN": [
            "CODUFMUN",
            "CNES",
            "CMPT_INI",
            "CMPT_FIM",
            "SGRUPHAB",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # regra_contratual
        "RC": [
            "CODUFMUN",
            "CNES",
            "CMPT_INI",
            "CMPT_FIM",
            "SGRUPHAB",
            "DTPORTAR",
            "PORTARIA",
            "MAPORTAR",
        ],
        # servico_especializado
        "SR": [
            "CODUFMUN",
            "CNES",
            "SERV_ESP",
            "CLASS_SR",
            "SRVUNICO",
            "CARACTER",
            "AMB_NSUS",
            "AMB_SUS",
            "HOSP_NSUS",
            "HOSP_SUS",
            "CONTSRVU",
            "CNESTERC",
        ],
        # dados complementares
        "DC": [
            "CODUFMUN",
            "CNES",
            "S_HBSAGP",
            "S_HBSAGN",
            "S_DPI",
            "S_DPAC",
            "S_REAGP",
            "S_REAGN",
            "S_REHCV",
            "MAQ_PROP",
            "MAQ_OUTR",
            "F_AREIA",
            "F_CARVAO",
            "ABRANDAD",
            "DEIONIZA",
            "OSMOSE_R",
            "OUT_TRAT",
            "CNS_NEFR",
            "DIALISE",
            "SIMUL_RD",
            "PLANJ_RD",
            "ARMAZ_FT",
            "CONF_MAS",
            "SALA_MOL",
            "BLOCOPER",
            "S_ARMAZE",
            "S_PREPAR",
            "S_QCDURA",
            "S_QLDURA",
            "S_CPFLUX",
            "S_SIMULA",
            "S_ACELL6",
            "S_ALSEME",
            "S_ALCOME",
            "ORTV1050",
            "ORV50150",
            "OV150500",
            "UN_COBAL",
            "EQBRBAIX",
            "EQBRMEDI",
            "EQBRALTA",
            "EQ_MAREA",
            "EQ_MINDI",
            "EQSISPLN",
            "EQDOSCLI",
            "EQFONSEL",
            "CNS_ADM",
            "CNS_OPED",
            "CNS_CONC",
            "CNS_OCLIN",
            "CNS_MRAD",
            "CNS_FNUC",
            "QUIMRADI",
            "S_RECEPC",
            "S_TRIHMT",
            "S_TRICLI",
            "S_COLETA",
            "S_AFERES",
            "S_PREEST",
            "S_PROCES",
            "S_ESTOQU",
            "S_DISTRI",
            "S_SOROLO",
            "S_IMUNOH",
            "S_PRETRA",
            "S_HEMOST",
            "S_CONTRQ",
            "S_BIOMOL",
            "S_IMUNFE",
            "S_TRANSF",
            "S_SGDOAD",
            "QT_CADRE",
            "QT_CENRE",
            "QT_REFSA",
            "QT_CONRA",
            "QT_EXTPL",
            "QT_FRE18",
            "QT_FRE30",
            "QT_AGIPL",
            "QT_SELAD",
            "QT_IRRHE",
            "QT_AGLTN",
            "QT_MAQAF",
            "QT_REFRE",
            "QT_REFAS",
            "QT_CAPFL",
            "CNS_HMTR",
            "CNS_HMTL",
            "CNS_CRES",
            "CNS_RTEC",
            "HEMOTERA",
        ],
        #
    }

    # generate YYYYMM to parse correct files from FTP server
    # usually the files are released with a 2 month delay. So this dict
    # maps the representative values of months to it as an int - 2
    GENERATE_MONTH_TO_PARSE = {
        # january : november
        1: "11",
        # february : december an so on
        2: "12",
        3: "01",
        4: "02",
        5: "03",
        6: "04",
        7: "05",
        8: "07",
        9: "07",
        10: "08",
        12: "09",
        11: "10",
    }
