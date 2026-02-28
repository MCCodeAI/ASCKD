




WMX3 User Manual: CompensationApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
CompensationApi.h File Reference 

| Classes | |
| --- | --- |
| class | [CompensationErrorCode](classwmx3_api_1_1_compensation_error_code.html) |
|  | This enumerator class enumerates the WMX3 compensation library error codes. [More...](classwmx3_api_1_1_compensation_error_code.html#details) |
|  | |
| class | [PitchErrorCompensationOriginPositionType](classwmx3_api_1_1_pitch_error_compensation_origin_position_type.html) |
|  | This enumerator class enumerates the types of origin positions that are specified for pitch error compensation. [More...](classwmx3_api_1_1_pitch_error_compensation_origin_position_type.html#details) |
|  | |
| class | [PitchErrorCompensationAlignmentType](classwmx3_api_1_1_pitch_error_compensation_alignment_type.html) |
|  | This enumerator class enumerates the types of alignments for the pitch error compensation points. [More...](classwmx3_api_1_1_pitch_error_compensation_alignment_type.html#details) |
|  | |
| class | [PitchErrorCompensationOptions](classwmx3_api_1_1_pitch_error_compensation_options.html) |
|  | This class contains options for pitch error compensation. [More...](classwmx3_api_1_1_pitch_error_compensation_options.html#details) |
|  | |
| class | [PitchErrorCompensationData](classwmx3_api_1_1_pitch_error_compensation_data.html) |
|  | This class contains data for pitch error compensation for an axis. Also see [Parameters](_w_m_x_d_o_c__f_u_n_c__c_m_p__p_e__p_a_r_a_m_e_t_e_r.html). [More...](classwmx3_api_1_1_pitch_error_compensation_data.html#details) |
|  | |
| class | [PitchErrorCompensationFreePositionData](classwmx3_api_1_1_pitch_error_compensation_free_position_data.html) |
|  | This class contains data for free position mode pitch error compensation for an axis. Also see [Free Position Mode Parameters](_w_m_x_d_o_c__f_u_n_c__c_m_p__p_e__p_a_r_a_m_e_t_e_r.html#WMXDOC_FUNC_CMP_PE_PARAMETER_FREE_POSITION). [More...](classwmx3_api_1_1_pitch_error_compensation_free_position_data.html#details) |
|  | |
| class | [TwoDPitchErrorCompensationData](classwmx3_api_1_1_two_d_pitch_error_compensation_data.html) |
|  | This class contains data for two-dimensional pitch error compensation. Also see [Parameters](_w_m_x_d_o_c__f_u_n_c__c_m_p_2_d_p_e__p_a_r_a_m_e_t_e_r.html). [More...](classwmx3_api_1_1_two_d_pitch_error_compensation_data.html#details) |
|  | |
| class | [TwoDPitchErrorCompensationFreePositionData](classwmx3_api_1_1_two_d_pitch_error_compensation_free_position_data.html) |
|  | This class contains data for free position mode two-dimensional pitch error compensation. Also see [Free Position Mode Parameters](_w_m_x_d_o_c__f_u_n_c__c_m_p_2_d_p_e__p_a_r_a_m_e_t_e_r.html#WMXDOC_FUNC_CMP_2DPE_PARAMETER_FREE_POSITION). [More...](classwmx3_api_1_1_two_d_pitch_error_compensation_free_position_data.html#details) |
|  | |
| class | [BacklashCompensationData](classwmx3_api_1_1_backlash_compensation_data.html) |
|  | This class contains data for backlash compensation for an axis. Also see [Parameters](_w_m_x_d_o_c__f_u_n_c__c_m_p__b_l__p_a_r_a_m_e_t_e_r.html). [More...](classwmx3_api_1_1_backlash_compensation_data.html#details) |
|  | |
| class | [Compensation](classwmx3_api_1_1_compensation.html) |
|  | **This class contains compensation functions.**  [More...](classwmx3_api_1_1_compensation.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxPitchErrorCompPoints](namespacewmx3_api_1_1constants.html#abeb51dc060f076e2bd4c34bff40ce20a) = 1024 |
|  | The maximum number of pitch error compensation points per axis (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |
| static const int | [maxPitchErrorCompFreePositionRangeMultiplier](namespacewmx3_api_1_1constants.html#aaa0c16803bb925a0183319974dc2950c) = 40000 |
|  | The maximum range in free position mode of pitch error compensation as a multiple of the two closest pitch positions (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |
| static const int | [max2dPitchErrorCompPoints](namespacewmx3_api_1_1constants.html#af6be40875a73aa3f6ffc7e19946fdab8) = 512 |
|  | The maximum number of two-dimensional pitch error compensation points per axis (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |
| static const int | [max2dPitchErrorCompChannel](namespacewmx3_api_1_1constants.html#af69bca9ac2544a8b3b51ff9b83d9408a) = 32 |
|  | The maximum number of two-dimensional pitch error compensation channels (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |
| static const int | [max2dPitchErrorCompFreePositionRangeMultiplier](namespacewmx3_api_1_1constants.html#ae15ab260088e85a3032cae2520390831) = 40000 |
|  | The maximum range in free position mode of two-dimensional pitch error compensation as a multiple of the two closest pitch positions (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |
| static const int | [maxSizeSet2dPitchErrorCompValue](namespacewmx3_api_1_1constants.html#a2dc1227b5c88ecb8c1e10674e36d6c23) = 62 |
|  | Reserved (also see [Compensation Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_m_p_e_n_s_a_t_i_o_n.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [CompensationApi.h](_compensation_api_8h.html)



