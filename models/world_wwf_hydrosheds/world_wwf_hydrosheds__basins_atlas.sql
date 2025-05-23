{{
    config(
        alias="basins_atlas",
        schema="world_wwf_hydrosheds",
        materialized="table",
        cluster_by="level",
    )
}}
select
    safe_cast(level as string) level,
    safe_cast(hybas_id as string) hybas_id,
    safe_cast(next_down as string) next_down,
    safe_cast(next_sink as string) next_sink,
    safe_cast(main_bas as string) main_bas,
    safe_cast(dist_sink as float64) dist_sink,
    safe_cast(dist_main as float64) dist_main,
    safe_cast(sub_area as float64) sub_area,
    safe_cast(up_area as float64) up_area,
    safe_cast(pfaf_id as string) pfaf_id,
    safe_cast(endo as int64) endo,
    safe_cast(coast as int64) coast,
    safe_cast(order_ as string) order_,
    safe_cast(sort as int64) sort,
    safe_cast(dis_m3_pyr as float64) dis_m3_pyr,
    safe_cast(dis_m3_pmn as float64) dis_m3_pmn,
    safe_cast(dis_m3_pmx as float64) dis_m3_pmx,
    safe_cast(run_mm_syr as int64) run_mm_syr,
    safe_cast(inu_pc_smn as int64) inu_pc_smn,
    safe_cast(inu_pc_umn as int64) inu_pc_umn,
    safe_cast(inu_pc_smx as int64) inu_pc_smx,
    safe_cast(inu_pc_umx as int64) inu_pc_umx,
    safe_cast(inu_pc_slt as int64) inu_pc_slt,
    safe_cast(inu_pc_ult as int64) inu_pc_ult,
    safe_cast(lka_pc_sse as int64) lka_pc_sse,
    safe_cast(lka_pc_use as int64) lka_pc_use,
    safe_cast(lkv_mc_usu as int64) lkv_mc_usu,
    safe_cast(rev_mc_usu as int64) rev_mc_usu,
    safe_cast(dor_pc_pva as int64) dor_pc_pva,
    safe_cast(ria_ha_ssu as float64) ria_ha_ssu,
    safe_cast(ria_ha_usu as float64) ria_ha_usu,
    safe_cast(riv_tc_ssu as float64) riv_tc_ssu,
    safe_cast(riv_tc_usu as float64) riv_tc_usu,
    safe_cast(gwt_cm_sav as int64) gwt_cm_sav,
    safe_cast(ele_mt_sav as int64) ele_mt_sav,
    safe_cast(ele_mt_uav as int64) ele_mt_uav,
    safe_cast(ele_mt_smn as int64) ele_mt_smn,
    safe_cast(ele_mt_smx as int64) ele_mt_smx,
    safe_cast(slp_dg_sav as int64) slp_dg_sav,
    safe_cast(slp_dg_uav as int64) slp_dg_uav,
    safe_cast(sgr_dk_sav as int64) sgr_dk_sav,
    safe_cast(clz_cl_smj as int64) clz_cl_smj,
    safe_cast(cls_cl_smj as int64) cls_cl_smj,
    safe_cast(tmp_dc_syr as int64) tmp_dc_syr,
    safe_cast(tmp_dc_uyr as int64) tmp_dc_uyr,
    safe_cast(tmp_dc_smn as int64) tmp_dc_smn,
    safe_cast(tmp_dc_smx as int64) tmp_dc_smx,
    safe_cast(tmp_dc_s01 as int64) tmp_dc_s01,
    safe_cast(tmp_dc_s02 as int64) tmp_dc_s02,
    safe_cast(tmp_dc_s03 as int64) tmp_dc_s03,
    safe_cast(tmp_dc_s04 as int64) tmp_dc_s04,
    safe_cast(tmp_dc_s05 as int64) tmp_dc_s05,
    safe_cast(tmp_dc_s06 as int64) tmp_dc_s06,
    safe_cast(tmp_dc_s07 as int64) tmp_dc_s07,
    safe_cast(tmp_dc_s08 as int64) tmp_dc_s08,
    safe_cast(tmp_dc_s09 as int64) tmp_dc_s09,
    safe_cast(tmp_dc_s10 as int64) tmp_dc_s10,
    safe_cast(tmp_dc_s11 as int64) tmp_dc_s11,
    safe_cast(tmp_dc_s12 as int64) tmp_dc_s12,
    safe_cast(pre_mm_syr as int64) pre_mm_syr,
    safe_cast(pre_mm_uyr as int64) pre_mm_uyr,
    safe_cast(pre_mm_s01 as int64) pre_mm_s01,
    safe_cast(pre_mm_s02 as int64) pre_mm_s02,
    safe_cast(pre_mm_s03 as int64) pre_mm_s03,
    safe_cast(pre_mm_s04 as int64) pre_mm_s04,
    safe_cast(pre_mm_s05 as int64) pre_mm_s05,
    safe_cast(pre_mm_s06 as int64) pre_mm_s06,
    safe_cast(pre_mm_s07 as int64) pre_mm_s07,
    safe_cast(pre_mm_s08 as int64) pre_mm_s08,
    safe_cast(pre_mm_s09 as int64) pre_mm_s09,
    safe_cast(pre_mm_s10 as int64) pre_mm_s10,
    safe_cast(pre_mm_s11 as int64) pre_mm_s11,
    safe_cast(pre_mm_s12 as int64) pre_mm_s12,
    safe_cast(pet_mm_syr as int64) pet_mm_syr,
    safe_cast(pet_mm_uyr as int64) pet_mm_uyr,
    safe_cast(pet_mm_s01 as int64) pet_mm_s01,
    safe_cast(pet_mm_s02 as int64) pet_mm_s02,
    safe_cast(pet_mm_s03 as int64) pet_mm_s03,
    safe_cast(pet_mm_s04 as int64) pet_mm_s04,
    safe_cast(pet_mm_s05 as int64) pet_mm_s05,
    safe_cast(pet_mm_s06 as int64) pet_mm_s06,
    safe_cast(pet_mm_s07 as int64) pet_mm_s07,
    safe_cast(pet_mm_s08 as int64) pet_mm_s08,
    safe_cast(pet_mm_s09 as int64) pet_mm_s09,
    safe_cast(pet_mm_s10 as int64) pet_mm_s10,
    safe_cast(pet_mm_s11 as int64) pet_mm_s11,
    safe_cast(pet_mm_s12 as int64) pet_mm_s12,
    safe_cast(aet_mm_syr as int64) aet_mm_syr,
    safe_cast(aet_mm_uyr as int64) aet_mm_uyr,
    safe_cast(aet_mm_s01 as int64) aet_mm_s01,
    safe_cast(aet_mm_s02 as int64) aet_mm_s02,
    safe_cast(aet_mm_s03 as int64) aet_mm_s03,
    safe_cast(aet_mm_s04 as int64) aet_mm_s04,
    safe_cast(aet_mm_s05 as int64) aet_mm_s05,
    safe_cast(aet_mm_s06 as int64) aet_mm_s06,
    safe_cast(aet_mm_s07 as int64) aet_mm_s07,
    safe_cast(aet_mm_s08 as int64) aet_mm_s08,
    safe_cast(aet_mm_s09 as int64) aet_mm_s09,
    safe_cast(aet_mm_s10 as int64) aet_mm_s10,
    safe_cast(aet_mm_s11 as int64) aet_mm_s11,
    safe_cast(aet_mm_s12 as int64) aet_mm_s12,
    safe_cast(ari_ix_sav as int64) ari_ix_sav,
    safe_cast(ari_ix_uav as int64) ari_ix_uav,
    safe_cast(cmi_ix_syr as int64) cmi_ix_syr,
    safe_cast(cmi_ix_uyr as int64) cmi_ix_uyr,
    safe_cast(cmi_ix_s01 as int64) cmi_ix_s01,
    safe_cast(cmi_ix_s02 as int64) cmi_ix_s02,
    safe_cast(cmi_ix_s03 as int64) cmi_ix_s03,
    safe_cast(cmi_ix_s04 as int64) cmi_ix_s04,
    safe_cast(cmi_ix_s05 as int64) cmi_ix_s05,
    safe_cast(cmi_ix_s06 as int64) cmi_ix_s06,
    safe_cast(cmi_ix_s07 as int64) cmi_ix_s07,
    safe_cast(cmi_ix_s08 as int64) cmi_ix_s08,
    safe_cast(cmi_ix_s09 as int64) cmi_ix_s09,
    safe_cast(cmi_ix_s10 as int64) cmi_ix_s10,
    safe_cast(cmi_ix_s11 as int64) cmi_ix_s11,
    safe_cast(cmi_ix_s12 as int64) cmi_ix_s12,
    safe_cast(snw_pc_syr as int64) snw_pc_syr,
    safe_cast(snw_pc_uyr as int64) snw_pc_uyr,
    safe_cast(snw_pc_smx as int64) snw_pc_smx,
    safe_cast(snw_pc_s01 as int64) snw_pc_s01,
    safe_cast(snw_pc_s02 as int64) snw_pc_s02,
    safe_cast(snw_pc_s03 as int64) snw_pc_s03,
    safe_cast(snw_pc_s04 as int64) snw_pc_s04,
    safe_cast(snw_pc_s05 as int64) snw_pc_s05,
    safe_cast(snw_pc_s06 as int64) snw_pc_s06,
    safe_cast(snw_pc_s07 as int64) snw_pc_s07,
    safe_cast(snw_pc_s08 as int64) snw_pc_s08,
    safe_cast(snw_pc_s09 as int64) snw_pc_s09,
    safe_cast(snw_pc_s10 as int64) snw_pc_s10,
    safe_cast(snw_pc_s11 as int64) snw_pc_s11,
    safe_cast(snw_pc_s12 as int64) snw_pc_s12,
    safe_cast(glc_cl_smj as int64) glc_cl_smj,
    safe_cast(glc_pc_s01 as int64) glc_pc_s01,
    safe_cast(glc_pc_s02 as int64) glc_pc_s02,
    safe_cast(glc_pc_s03 as int64) glc_pc_s03,
    safe_cast(glc_pc_s04 as int64) glc_pc_s04,
    safe_cast(glc_pc_s05 as int64) glc_pc_s05,
    safe_cast(glc_pc_s06 as int64) glc_pc_s06,
    safe_cast(glc_pc_s07 as int64) glc_pc_s07,
    safe_cast(glc_pc_s08 as int64) glc_pc_s08,
    safe_cast(glc_pc_s09 as int64) glc_pc_s09,
    safe_cast(glc_pc_s10 as int64) glc_pc_s10,
    safe_cast(glc_pc_s11 as int64) glc_pc_s11,
    safe_cast(glc_pc_s12 as int64) glc_pc_s12,
    safe_cast(glc_pc_s13 as int64) glc_pc_s13,
    safe_cast(glc_pc_s14 as int64) glc_pc_s14,
    safe_cast(glc_pc_s15 as int64) glc_pc_s15,
    safe_cast(glc_pc_s16 as int64) glc_pc_s16,
    safe_cast(glc_pc_s17 as int64) glc_pc_s17,
    safe_cast(glc_pc_s18 as int64) glc_pc_s18,
    safe_cast(glc_pc_s19 as int64) glc_pc_s19,
    safe_cast(glc_pc_s20 as int64) glc_pc_s20,
    safe_cast(glc_pc_s21 as int64) glc_pc_s21,
    safe_cast(glc_pc_s22 as int64) glc_pc_s22,
    safe_cast(glc_pc_u01 as int64) glc_pc_u01,
    safe_cast(glc_pc_u02 as int64) glc_pc_u02,
    safe_cast(glc_pc_u03 as int64) glc_pc_u03,
    safe_cast(glc_pc_u04 as int64) glc_pc_u04,
    safe_cast(glc_pc_u05 as int64) glc_pc_u05,
    safe_cast(glc_pc_u06 as int64) glc_pc_u06,
    safe_cast(glc_pc_u07 as int64) glc_pc_u07,
    safe_cast(glc_pc_u08 as int64) glc_pc_u08,
    safe_cast(glc_pc_u09 as int64) glc_pc_u09,
    safe_cast(glc_pc_u10 as int64) glc_pc_u10,
    safe_cast(glc_pc_u11 as int64) glc_pc_u11,
    safe_cast(glc_pc_u12 as int64) glc_pc_u12,
    safe_cast(glc_pc_u13 as int64) glc_pc_u13,
    safe_cast(glc_pc_u14 as int64) glc_pc_u14,
    safe_cast(glc_pc_u15 as int64) glc_pc_u15,
    safe_cast(glc_pc_u16 as int64) glc_pc_u16,
    safe_cast(glc_pc_u17 as int64) glc_pc_u17,
    safe_cast(glc_pc_u18 as int64) glc_pc_u18,
    safe_cast(glc_pc_u19 as int64) glc_pc_u19,
    safe_cast(glc_pc_u20 as int64) glc_pc_u20,
    safe_cast(glc_pc_u21 as int64) glc_pc_u21,
    safe_cast(glc_pc_u22 as int64) glc_pc_u22,
    safe_cast(pnv_cl_smj as int64) pnv_cl_smj,
    safe_cast(pnv_pc_s01 as int64) pnv_pc_s01,
    safe_cast(pnv_pc_s02 as int64) pnv_pc_s02,
    safe_cast(pnv_pc_s03 as int64) pnv_pc_s03,
    safe_cast(pnv_pc_s04 as int64) pnv_pc_s04,
    safe_cast(pnv_pc_s05 as int64) pnv_pc_s05,
    safe_cast(pnv_pc_s06 as int64) pnv_pc_s06,
    safe_cast(pnv_pc_s07 as int64) pnv_pc_s07,
    safe_cast(pnv_pc_s08 as int64) pnv_pc_s08,
    safe_cast(pnv_pc_s09 as int64) pnv_pc_s09,
    safe_cast(pnv_pc_s10 as int64) pnv_pc_s10,
    safe_cast(pnv_pc_s11 as int64) pnv_pc_s11,
    safe_cast(pnv_pc_s12 as int64) pnv_pc_s12,
    safe_cast(pnv_pc_s13 as int64) pnv_pc_s13,
    safe_cast(pnv_pc_s14 as int64) pnv_pc_s14,
    safe_cast(pnv_pc_s15 as int64) pnv_pc_s15,
    safe_cast(pnv_pc_u01 as int64) pnv_pc_u01,
    safe_cast(pnv_pc_u02 as int64) pnv_pc_u02,
    safe_cast(pnv_pc_u03 as int64) pnv_pc_u03,
    safe_cast(pnv_pc_u04 as int64) pnv_pc_u04,
    safe_cast(pnv_pc_u05 as int64) pnv_pc_u05,
    safe_cast(pnv_pc_u06 as int64) pnv_pc_u06,
    safe_cast(pnv_pc_u07 as int64) pnv_pc_u07,
    safe_cast(pnv_pc_u08 as int64) pnv_pc_u08,
    safe_cast(pnv_pc_u09 as int64) pnv_pc_u09,
    safe_cast(pnv_pc_u10 as int64) pnv_pc_u10,
    safe_cast(pnv_pc_u11 as int64) pnv_pc_u11,
    safe_cast(pnv_pc_u12 as int64) pnv_pc_u12,
    safe_cast(pnv_pc_u13 as int64) pnv_pc_u13,
    safe_cast(pnv_pc_u14 as int64) pnv_pc_u14,
    safe_cast(pnv_pc_u15 as int64) pnv_pc_u15,
    safe_cast(wet_cl_smj as int64) wet_cl_smj,
    safe_cast(wet_pc_sg1 as int64) wet_pc_sg1,
    safe_cast(wet_pc_ug1 as int64) wet_pc_ug1,
    safe_cast(wet_pc_sg2 as int64) wet_pc_sg2,
    safe_cast(wet_pc_ug2 as int64) wet_pc_ug2,
    safe_cast(wet_pc_s01 as int64) wet_pc_s01,
    safe_cast(wet_pc_s02 as int64) wet_pc_s02,
    safe_cast(wet_pc_s03 as int64) wet_pc_s03,
    safe_cast(wet_pc_s04 as int64) wet_pc_s04,
    safe_cast(wet_pc_s05 as int64) wet_pc_s05,
    safe_cast(wet_pc_s06 as int64) wet_pc_s06,
    safe_cast(wet_pc_s07 as int64) wet_pc_s07,
    safe_cast(wet_pc_s08 as int64) wet_pc_s08,
    safe_cast(wet_pc_s09 as int64) wet_pc_s09,
    safe_cast(wet_pc_u01 as int64) wet_pc_u01,
    safe_cast(wet_pc_u02 as int64) wet_pc_u02,
    safe_cast(wet_pc_u03 as int64) wet_pc_u03,
    safe_cast(wet_pc_u04 as int64) wet_pc_u04,
    safe_cast(wet_pc_u05 as int64) wet_pc_u05,
    safe_cast(wet_pc_u06 as int64) wet_pc_u06,
    safe_cast(wet_pc_u07 as int64) wet_pc_u07,
    safe_cast(wet_pc_u08 as int64) wet_pc_u08,
    safe_cast(wet_pc_u09 as int64) wet_pc_u09,
    safe_cast(for_pc_sse as int64) for_pc_sse,
    safe_cast(for_pc_use as int64) for_pc_use,
    safe_cast(crp_pc_sse as int64) crp_pc_sse,
    safe_cast(crp_pc_use as int64) crp_pc_use,
    safe_cast(pst_pc_sse as int64) pst_pc_sse,
    safe_cast(pst_pc_use as int64) pst_pc_use,
    safe_cast(ire_pc_sse as int64) ire_pc_sse,
    safe_cast(ire_pc_use as int64) ire_pc_use,
    safe_cast(gla_pc_sse as int64) gla_pc_sse,
    safe_cast(gla_pc_use as int64) gla_pc_use,
    safe_cast(prm_pc_sse as int64) prm_pc_sse,
    safe_cast(prm_pc_use as int64) prm_pc_use,
    safe_cast(pac_pc_sse as int64) pac_pc_sse,
    safe_cast(pac_pc_use as int64) pac_pc_use,
    safe_cast(tbi_cl_smj as int64) tbi_cl_smj,
    safe_cast(tec_cl_smj as int64) tec_cl_smj,
    safe_cast(fmh_cl_smj as int64) fmh_cl_smj,
    safe_cast(fec_cl_smj as int64) fec_cl_smj,
    safe_cast(cly_pc_sav as int64) cly_pc_sav,
    safe_cast(cly_pc_uav as int64) cly_pc_uav,
    safe_cast(slt_pc_sav as int64) slt_pc_sav,
    safe_cast(slt_pc_uav as int64) slt_pc_uav,
    safe_cast(snd_pc_sav as int64) snd_pc_sav,
    safe_cast(snd_pc_uav as int64) snd_pc_uav,
    safe_cast(soc_th_sav as int64) soc_th_sav,
    safe_cast(soc_th_uav as int64) soc_th_uav,
    safe_cast(swc_pc_syr as int64) swc_pc_syr,
    safe_cast(swc_pc_uyr as int64) swc_pc_uyr,
    safe_cast(swc_pc_s01 as int64) swc_pc_s01,
    safe_cast(swc_pc_s02 as int64) swc_pc_s02,
    safe_cast(swc_pc_s03 as int64) swc_pc_s03,
    safe_cast(swc_pc_s04 as int64) swc_pc_s04,
    safe_cast(swc_pc_s05 as int64) swc_pc_s05,
    safe_cast(swc_pc_s06 as int64) swc_pc_s06,
    safe_cast(swc_pc_s07 as int64) swc_pc_s07,
    safe_cast(swc_pc_s08 as int64) swc_pc_s08,
    safe_cast(swc_pc_s09 as int64) swc_pc_s09,
    safe_cast(swc_pc_s10 as int64) swc_pc_s10,
    safe_cast(swc_pc_s11 as int64) swc_pc_s11,
    safe_cast(swc_pc_s12 as int64) swc_pc_s12,
    safe_cast(lit_cl_smj as int64) lit_cl_smj,
    safe_cast(kar_pc_sse as int64) kar_pc_sse,
    safe_cast(kar_pc_use as int64) kar_pc_use,
    safe_cast(ero_kh_sav as int64) ero_kh_sav,
    safe_cast(ero_kh_uav as int64) ero_kh_uav,
    safe_cast(pop_ct_ssu as float64) pop_ct_ssu,
    safe_cast(pop_ct_usu as float64) pop_ct_usu,
    safe_cast(ppd_pk_sav as float64) ppd_pk_sav,
    safe_cast(ppd_pk_uav as float64) ppd_pk_uav,
    safe_cast(urb_pc_sse as int64) urb_pc_sse,
    safe_cast(urb_pc_use as int64) urb_pc_use,
    safe_cast(nli_ix_sav as int64) nli_ix_sav,
    safe_cast(nli_ix_uav as int64) nli_ix_uav,
    safe_cast(rdd_mk_sav as int64) rdd_mk_sav,
    safe_cast(rdd_mk_uav as int64) rdd_mk_uav,
    safe_cast(hft_ix_s93 as int64) hft_ix_s93,
    safe_cast(hft_ix_u93 as int64) hft_ix_u93,
    safe_cast(hft_ix_s09 as int64) hft_ix_s09,
    safe_cast(hft_ix_u09 as int64) hft_ix_u09,
    safe_cast(gad_id_smj as int64) gad_id_smj,
    safe_cast(gdp_ud_sav as int64) gdp_ud_sav,
    safe_cast(gdp_ud_ssu as int64) gdp_ud_ssu,
    safe_cast(gdp_ud_usu as int64) gdp_ud_usu,
    safe_cast(hdi_ix_sav as int64) hdi_ix_sav,
    st_geogfromtext(geometry, make_valid => true) geometry
from {{ set_datalake_project("world_wwf_hydrosheds_staging.basins_atlas") }} as t
