{{
    config(
        alias="rendimentos_outras_fontes",
        schema="br_ibge_pnadc",
        materialized="table",
        partition_by={
            "field": "ano",
            "data_type": "int64",
            "range": {"start": 2012, "end": 2025, "interval": 1},
        },
        cluster_by="sigla_uf",
    )
}}
select
    safe_cast(ano as int64) ano,
    safe_cast(trimestre as int64) trimestre,
    safe_cast(id_uf as string) id_uf,
    safe_cast(sigla_uf as string) sigla_uf,
    safe_cast(capital as string) capital,
    safe_cast(rm_ride as string) rm_ride,
    safe_cast(id_upa as string) id_upa,
    safe_cast(id_estrato as string) id_estrato,
    safe_cast(id_domicilio as string) id_domicilio,
    safe_cast(id_pessoa as string) id_pessoa,
    safe_cast(v1008 as string) v1008,
    safe_cast(v1014 as string) v1014,
    safe_cast(v1022 as string) v1022,
    safe_cast(v1023 as string) v1023,
    safe_cast(v1030 as int64) v1030,
    safe_cast(v1031 as float64) v1031,
    safe_cast(v1032 as float64) v1032,
    safe_cast(v1034 as int64) v1034,
    safe_cast(posest as string) posest,
    safe_cast(posest_sxi as string) posest_sxi,
    safe_cast(v2001 as int64) v2001,
    safe_cast(v2003 as int64) v2003,
    safe_cast(v5001 as string) v5001,
    safe_cast(v50011 as string) v50011,
    safe_cast(v500111 as float64) v500111,
    safe_cast(v5002 as string) v5002,
    safe_cast(v50021 as string) v50021,
    safe_cast(v500211 as float64) v500211,
    safe_cast(v5003 as string) v5003,
    safe_cast(v50031 as string) v50031,
    safe_cast(v500311 as float64) v500311,
    safe_cast(v5004 as string) v5004,
    safe_cast(v50041 as string) v50041,
    safe_cast(v500411 as float64) v500411,
    safe_cast(v5005 as string) v5005,
    safe_cast(v50051 as string) v50051,
    safe_cast(v500511 as float64) v500511,
    safe_cast(v5006 as string) v5006,
    safe_cast(v50061 as string) v50061,
    safe_cast(v500611 as float64) v500611,
    safe_cast(v5007 as string) v5007,
    safe_cast(v50071 as string) v50071,
    safe_cast(v500711 as float64) v500711,
    safe_cast(v5008 as string) v5008,
    safe_cast(v50081 as string) v50081,
    safe_cast(v500811 as float64) v500811,
    safe_cast(v5009 as string) v5009,
    safe_cast(v50091 as string) v50091,
    safe_cast(v500911 as float64) v500911,
    safe_cast(v5010 as string) v5010,
    safe_cast(v50101 as string) v50101,
    safe_cast(v501011 as float64) v501011,
    safe_cast(v5011 as string) v5011,
    safe_cast(v50111 as string) v50111,
    safe_cast(v501111 as float64) v501111,
    safe_cast(v5012 as string) v5012,
    safe_cast(v50121 as string) v50121,
    safe_cast(v501211 as float64) v501211,
    safe_cast(v5013 as string) v5013,
    safe_cast(v50131 as string) v50131,
    safe_cast(v501311 as float64) v501311,
    safe_cast(v5001a as string) v5001a,
    safe_cast(v5001a2 as float64) v5001a2,
    safe_cast(v5002a as string) v5002a,
    safe_cast(v5002a2 as float64) v5002a2,
    safe_cast(v5003a as string) v5003a,
    safe_cast(v5003a2 as float64) v5003a2,
    safe_cast(v5004a as string) v5004a,
    safe_cast(v5004a2 as float64) v5004a2,
    safe_cast(v5005a as string) v5005a,
    safe_cast(v5005a2 as float64) v5005a2,
    safe_cast(v5006a as string) v5006a,
    safe_cast(v5006a2 as float64) v5006a2,
    safe_cast(v5007a as string) v5007a,
    safe_cast(v5007a2 as float64) v5007a2,
    safe_cast(v5008a as string) v5008a,
    safe_cast(v5008a2 as float64) v5008a2,
    safe_cast(vd4046 as float64) vd4046,
    safe_cast(vd4047 as float64) vd4047,
    safe_cast(vd4048 as float64) vd4048,
    safe_cast(vd4052 as float64) vd4052,
    safe_cast(vd5001 as float64) vd5001,
    safe_cast(vd5002 as float64) vd5002,
    safe_cast(vd5003 as string) vd5003,
    safe_cast(vd5004 as float64) vd5004,
    safe_cast(vd5005 as float64) vd5005,
    safe_cast(vd5006 as string) vd5006,
    safe_cast(vd5007 as float64) vd5007,
    safe_cast(vd5008 as float64) vd5008,
    safe_cast(vd5009 as string) vd5009,
    safe_cast(vd5010 as float64) vd5010,
    safe_cast(vd5011 as float64) vd5011,
    safe_cast(vd5012 as string) vd5012,
    safe_cast(v1032001 as float64) v1032001,
    safe_cast(v1032002 as float64) v1032002,
    safe_cast(v1032003 as float64) v1032003,
    safe_cast(v1032004 as float64) v1032004,
    safe_cast(v1032005 as float64) v1032005,
    safe_cast(v1032006 as float64) v1032006,
    safe_cast(v1032007 as float64) v1032007,
    safe_cast(v1032008 as float64) v1032008,
    safe_cast(v1032009 as float64) v1032009,
    safe_cast(v1032010 as float64) v1032010,
    safe_cast(v1032011 as float64) v1032011,
    safe_cast(v1032012 as float64) v1032012,
    safe_cast(v1032013 as float64) v1032013,
    safe_cast(v1032014 as float64) v1032014,
    safe_cast(v1032015 as float64) v1032015,
    safe_cast(v1032016 as float64) v1032016,
    safe_cast(v1032017 as float64) v1032017,
    safe_cast(v1032018 as float64) v1032018,
    safe_cast(v1032019 as float64) v1032019,
    safe_cast(v1032020 as float64) v1032020,
    safe_cast(v1032021 as float64) v1032021,
    safe_cast(v1032022 as float64) v1032022,
    safe_cast(v1032023 as float64) v1032023,
    safe_cast(v1032024 as float64) v1032024,
    safe_cast(v1032025 as float64) v1032025,
    safe_cast(v1032026 as float64) v1032026,
    safe_cast(v1032027 as float64) v1032027,
    safe_cast(v1032028 as float64) v1032028,
    safe_cast(v1032029 as float64) v1032029,
    safe_cast(v1032030 as float64) v1032030,
    safe_cast(v1032031 as float64) v1032031,
    safe_cast(v1032032 as float64) v1032032,
    safe_cast(v1032033 as float64) v1032033,
    safe_cast(v1032034 as float64) v1032034,
    safe_cast(v1032035 as float64) v1032035,
    safe_cast(v1032036 as float64) v1032036,
    safe_cast(v1032037 as float64) v1032037,
    safe_cast(v1032038 as float64) v1032038,
    safe_cast(v1032039 as float64) v1032039,
    safe_cast(v1032040 as float64) v1032040,
    safe_cast(v1032041 as float64) v1032041,
    safe_cast(v1032042 as float64) v1032042,
    safe_cast(v1032043 as float64) v1032043,
    safe_cast(v1032044 as float64) v1032044,
    safe_cast(v1032045 as float64) v1032045,
    safe_cast(v1032046 as float64) v1032046,
    safe_cast(v1032047 as float64) v1032047,
    safe_cast(v1032048 as float64) v1032048,
    safe_cast(v1032049 as float64) v1032049,
    safe_cast(v1032050 as float64) v1032050,
    safe_cast(v1032051 as float64) v1032051,
    safe_cast(v1032052 as float64) v1032052,
    safe_cast(v1032053 as float64) v1032053,
    safe_cast(v1032054 as float64) v1032054,
    safe_cast(v1032055 as float64) v1032055,
    safe_cast(v1032056 as float64) v1032056,
    safe_cast(v1032057 as float64) v1032057,
    safe_cast(v1032058 as float64) v1032058,
    safe_cast(v1032059 as float64) v1032059,
    safe_cast(v1032060 as float64) v1032060,
    safe_cast(v1032061 as float64) v1032061,
    safe_cast(v1032062 as float64) v1032062,
    safe_cast(v1032063 as float64) v1032063,
    safe_cast(v1032064 as float64) v1032064,
    safe_cast(v1032065 as float64) v1032065,
    safe_cast(v1032066 as float64) v1032066,
    safe_cast(v1032067 as float64) v1032067,
    safe_cast(v1032068 as float64) v1032068,
    safe_cast(v1032069 as float64) v1032069,
    safe_cast(v1032070 as float64) v1032070,
    safe_cast(v1032071 as float64) v1032071,
    safe_cast(v1032072 as float64) v1032072,
    safe_cast(v1032073 as float64) v1032073,
    safe_cast(v1032074 as float64) v1032074,
    safe_cast(v1032075 as float64) v1032075,
    safe_cast(v1032076 as float64) v1032076,
    safe_cast(v1032077 as float64) v1032077,
    safe_cast(v1032078 as float64) v1032078,
    safe_cast(v1032079 as float64) v1032079,
    safe_cast(v1032080 as float64) v1032080,
    safe_cast(v1032081 as float64) v1032081,
    safe_cast(v1032082 as float64) v1032082,
    safe_cast(v1032083 as float64) v1032083,
    safe_cast(v1032084 as float64) v1032084,
    safe_cast(v1032085 as float64) v1032085,
    safe_cast(v1032086 as float64) v1032086,
    safe_cast(v1032087 as float64) v1032087,
    safe_cast(v1032088 as float64) v1032088,
    safe_cast(v1032089 as float64) v1032089,
    safe_cast(v1032090 as float64) v1032090,
    safe_cast(v1032091 as float64) v1032091,
    safe_cast(v1032092 as float64) v1032092,
    safe_cast(v1032093 as float64) v1032093,
    safe_cast(v1032094 as float64) v1032094,
    safe_cast(v1032095 as float64) v1032095,
    safe_cast(v1032096 as float64) v1032096,
    safe_cast(v1032097 as float64) v1032097,
    safe_cast(v1032098 as float64) v1032098,
    safe_cast(v1032099 as float64) v1032099,
    safe_cast(v1032100 as float64) v1032100,
    safe_cast(v1032101 as float64) v1032101,
    safe_cast(v1032102 as float64) v1032102,
    safe_cast(v1032103 as float64) v1032103,
    safe_cast(v1032104 as float64) v1032104,
    safe_cast(v1032105 as float64) v1032105,
    safe_cast(v1032106 as float64) v1032106,
    safe_cast(v1032107 as float64) v1032107,
    safe_cast(v1032108 as float64) v1032108,
    safe_cast(v1032109 as float64) v1032109,
    safe_cast(v1032110 as float64) v1032110,
    safe_cast(v1032111 as float64) v1032111,
    safe_cast(v1032112 as float64) v1032112,
    safe_cast(v1032113 as float64) v1032113,
    safe_cast(v1032114 as float64) v1032114,
    safe_cast(v1032115 as float64) v1032115,
    safe_cast(v1032116 as float64) v1032116,
    safe_cast(v1032117 as float64) v1032117,
    safe_cast(v1032118 as float64) v1032118,
    safe_cast(v1032119 as float64) v1032119,
    safe_cast(v1032120 as float64) v1032120,
    safe_cast(v1032121 as float64) v1032121,
    safe_cast(v1032122 as float64) v1032122,
    safe_cast(v1032123 as float64) v1032123,
    safe_cast(v1032124 as float64) v1032124,
    safe_cast(v1032125 as float64) v1032125,
    safe_cast(v1032126 as float64) v1032126,
    safe_cast(v1032127 as float64) v1032127,
    safe_cast(v1032128 as float64) v1032128,
    safe_cast(v1032129 as float64) v1032129,
    safe_cast(v1032130 as float64) v1032130,
    safe_cast(v1032131 as float64) v1032131,
    safe_cast(v1032132 as float64) v1032132,
    safe_cast(v1032133 as float64) v1032133,
    safe_cast(v1032134 as float64) v1032134,
    safe_cast(v1032135 as float64) v1032135,
    safe_cast(v1032136 as float64) v1032136,
    safe_cast(v1032137 as float64) v1032137,
    safe_cast(v1032138 as float64) v1032138,
    safe_cast(v1032139 as float64) v1032139,
    safe_cast(v1032140 as float64) v1032140,
    safe_cast(v1032141 as float64) v1032141,
    safe_cast(v1032142 as float64) v1032142,
    safe_cast(v1032143 as float64) v1032143,
    safe_cast(v1032144 as float64) v1032144,
    safe_cast(v1032145 as float64) v1032145,
    safe_cast(v1032146 as float64) v1032146,
    safe_cast(v1032147 as float64) v1032147,
    safe_cast(v1032148 as float64) v1032148,
    safe_cast(v1032149 as float64) v1032149,
    safe_cast(v1032150 as float64) v1032150,
    safe_cast(v1032151 as float64) v1032151,
    safe_cast(v1032152 as float64) v1032152,
    safe_cast(v1032153 as float64) v1032153,
    safe_cast(v1032154 as float64) v1032154,
    safe_cast(v1032155 as float64) v1032155,
    safe_cast(v1032156 as float64) v1032156,
    safe_cast(v1032157 as float64) v1032157,
    safe_cast(v1032158 as float64) v1032158,
    safe_cast(v1032159 as float64) v1032159,
    safe_cast(v1032160 as float64) v1032160,
    safe_cast(v1032161 as float64) v1032161,
    safe_cast(v1032162 as float64) v1032162,
    safe_cast(v1032163 as float64) v1032163,
    safe_cast(v1032164 as float64) v1032164,
    safe_cast(v1032165 as float64) v1032165,
    safe_cast(v1032166 as float64) v1032166,
    safe_cast(v1032167 as float64) v1032167,
    safe_cast(v1032168 as float64) v1032168,
    safe_cast(v1032169 as float64) v1032169,
    safe_cast(v1032170 as float64) v1032170,
    safe_cast(v1032171 as float64) v1032171,
    safe_cast(v1032172 as float64) v1032172,
    safe_cast(v1032173 as float64) v1032173,
    safe_cast(v1032174 as float64) v1032174,
    safe_cast(v1032175 as float64) v1032175,
    safe_cast(v1032176 as float64) v1032176,
    safe_cast(v1032177 as float64) v1032177,
    safe_cast(v1032178 as float64) v1032178,
    safe_cast(v1032179 as float64) v1032179,
    safe_cast(v1032180 as float64) v1032180,
    safe_cast(v1032181 as float64) v1032181,
    safe_cast(v1032182 as float64) v1032182,
    safe_cast(v1032183 as float64) v1032183,
    safe_cast(v1032184 as float64) v1032184,
    safe_cast(v1032185 as float64) v1032185,
    safe_cast(v1032186 as float64) v1032186,
    safe_cast(v1032187 as float64) v1032187,
    safe_cast(v1032188 as float64) v1032188,
    safe_cast(v1032189 as float64) v1032189,
    safe_cast(v1032190 as float64) v1032190,
    safe_cast(v1032191 as float64) v1032191,
    safe_cast(v1032192 as float64) v1032192,
    safe_cast(v1032193 as float64) v1032193,
    safe_cast(v1032194 as float64) v1032194,
    safe_cast(v1032195 as float64) v1032195,
    safe_cast(v1032196 as float64) v1032196,
    safe_cast(v1032197 as float64) v1032197,
    safe_cast(v1032198 as float64) v1032198,
    safe_cast(v1032199 as float64) v1032199,
    safe_cast(v1032200 as float64) v1032200
from {{ set_datalake_project("br_ibge_pnadc_staging.rendimentos_outras_fontes") }} as t
