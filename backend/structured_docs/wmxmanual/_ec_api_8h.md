


WMX3 User Manual: EcApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Macros](#define-members) |
[Typedefs](#typedef-members) |
[Variables](#var-members) 
EcApi.h File Reference 

| Classes | |
| --- | --- |
| class | [EcStateMachine](classwmx3_api_1_1ec_api_1_1_ec_state_machine.html) |
|  | This enumerator class enumerates the Master or Slave states. [More...](classwmx3_api_1_1ec_api_1_1_ec_state_machine.html#details) |
|  | |
| class | [EcSdoType](classwmx3_api_1_1ec_api_1_1_ec_sdo_type.html) |
|  | This enumerator class enumerates the SDO types. [More...](classwmx3_api_1_1ec_api_1_1_ec_sdo_type.html#details) |
|  | |
| class | [EcObjectDescriptionListType](classwmx3_api_1_1ec_api_1_1_ec_object_description_list_type.html) |
|  | This enumerator class enumerates the OD (Object Description) list types. [More...](classwmx3_api_1_1ec_api_1_1_ec_object_description_list_type.html#details) |
|  | |
| class | [EcHotconnectState](classwmx3_api_1_1ec_api_1_1_ec_hotconnect_state.html) |
|  | This enumerator class enumerates the hot connect states. [More...](classwmx3_api_1_1ec_api_1_1_ec_hotconnect_state.html#details) |
|  | |
| class | [EcHotconnectAbortCode](classwmx3_api_1_1ec_api_1_1_ec_hotconnect_abort_code.html) |
|  | This enumerator class enumerates the error codes of when hot connect has been aborted. [More...](classwmx3_api_1_1ec_api_1_1_ec_hotconnect_abort_code.html#details) |
|  | |
| class | [EcDiagnosisScanState](classwmx3_api_1_1ec_api_1_1_ec_diagnosis_scan_state.html) |
|  | This enumerator class enumerates the states of diagnosis scan. [More...](classwmx3_api_1_1ec_api_1_1_ec_diagnosis_scan_state.html#details) |
|  | |
| class | [EcOperationMode](classwmx3_api_1_1ec_api_1_1_ec_operation_mode.html) |
|  | This enumerator class enumerates the servo slave operation modes. [More...](classwmx3_api_1_1ec_api_1_1_ec_operation_mode.html#details) |
|  | |
| class | [EcMasterMode](classwmx3_api_1_1ec_api_1_1_ec_master_mode.html) |
|  | This enumerator class enumerates the master operation modes. [More...](classwmx3_api_1_1ec_api_1_1_ec_master_mode.html#details) |
|  | |
| class | [EcErrorCode](classwmx3_api_1_1ec_api_1_1_ec_error_code.html) |
|  | This enumerator class enumerates the Ec library error codes. [More...](classwmx3_api_1_1ec_api_1_1_ec_error_code.html#details) |
|  | |
| class | [EcLogInputPdo](classwmx3_api_1_1ec_api_1_1_ec_log_input_pdo.html) |
|  | This class specifies the info of pdo whose data to be collected. [More...](classwmx3_api_1_1ec_api_1_1_ec_log_input_pdo.html#details) |
|  | |
| class | [EcLogInput](classwmx3_api_1_1ec_api_1_1_ec_log_input.html) |
|  | This class specifies the pdo to be collected by the EcPlatform module. [More...](classwmx3_api_1_1ec_api_1_1_ec_log_input.html#details) |
|  | |
| class | [EcLogOutputPdo](classwmx3_api_1_1ec_api_1_1_ec_log_output_pdo.html) |
|  | This class defines log output of one pdo. [More...](classwmx3_api_1_1ec_api_1_1_ec_log_output_pdo.html#details) |
|  | |
| class | [EcLogOutputData](classwmx3_api_1_1ec_api_1_1_ec_log_output_data.html) |
|  | This class defines the output datas in one cycle. [More...](classwmx3_api_1_1ec_api_1_1_ec_log_output_data.html#details) |
|  | |
| class | [EcLogOutput](classwmx3_api_1_1ec_api_1_1_ec_log_output.html) |
|  | This class specifies the output datas collected by the EcPlatform module. [More...](classwmx3_api_1_1ec_api_1_1_ec_log_output.html#details) |
|  | |
| class | [EcAoESender](classwmx3_api_1_1ec_api_1_1_ec_ao_e_sender.html) |
|  | This class describes the data for AoE sender. [More...](classwmx3_api_1_1ec_api_1_1_ec_ao_e_sender.html#details) |
|  | |
| class | [EcSlaveSdoInfoObjectDescription](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_object_description.html) |
|  | This class describes the Object Description in OD list. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_object_description.html#details) |
|  | |
| class | [EcSlaveSdoInfoObjectDescriptionList](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_object_description_list.html) |
|  | This class describes the Object Description List. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_object_description_list.html#details) |
|  | |
| class | [EcSlaveSdoInfoEntryDescription](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_entry_description.html) |
|  | This class describes the Entry Description in ED list. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_entry_description.html#details) |
|  | |
| class | [EcSlaveSdoInfoEntryDescriptionList](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_entry_description_list.html) |
|  | This class describes the Entry Description List. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_sdo_info_entry_description_list.html#details) |
|  | |
| class | [EcSlavePdo](classwmx3_api_1_1ec_api_1_1_ec_slave_pdo.html) |
|  | This class describes the Slave PDO data. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_pdo.html#details) |
|  | |
| class | [EcSlavePdoInfo](classwmx3_api_1_1ec_api_1_1_ec_slave_pdo_info.html) |
|  | This class describes the various PDO information in Slave. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_pdo_info.html#details) |
|  | |
| class | [EcSlaveAxisInfo](classwmx3_api_1_1ec_api_1_1_ec_slave_axis_info.html) |
|  | This class describes the axis information in Slave. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_axis_info.html#details) |
|  | |
| class | [EcSlaveInfo](classwmx3_api_1_1ec_api_1_1_ec_slave_info.html) |
|  | This class describes the Slave information. [More...](classwmx3_api_1_1ec_api_1_1_ec_slave_info.html#details) |
|  | |
| class | [EcMasterStatisticsInfo](classwmx3_api_1_1ec_api_1_1_ec_master_statistics_info.html) |
|  | This class describes the Master statistics information. [More...](classwmx3_api_1_1ec_api_1_1_ec_master_statistics_info.html#details) |
|  | |
| class | [EcMasterInfo](classwmx3_api_1_1ec_api_1_1_ec_master_info.html) |
|  | This class describes the Master information. [More...](classwmx3_api_1_1ec_api_1_1_ec_master_info.html#details) |
|  | |
| class | [EcMasterInfoList](classwmx3_api_1_1ec_api_1_1_ec_master_info_list.html) |
|  | This class describes the Master information list. [More...](classwmx3_api_1_1ec_api_1_1_ec_master_info_list.html#details) |
|  | |
| class | [Ecat](classwmx3_api_1_1ec_api_1_1_ecat.html) |
|  | **This class contains Ec API functions.**  [More...](classwmx3_api_1_1ec_api_1_1_ecat.html#details) |
|  | |

| Macros | |
| --- | --- |
| #define | **ECAPIFUNC**   HRESULT |
|  | |

| Typedefs | |
| --- | --- |
| typedef int(\* | [EcSdoDownloadCallBack](namespacewmx3_api_1_1ec_api.html#af134992a4fc82e888d1ac0c9c452e538)) (int result, int masterid, int slaveid, int index, int subindex, EcSdoType::T sdoType, int len, unsigned char \*data, unsigned int errorCode) |
|  | Callback function for the [SdoDownload](classwmx3_api_1_1ec_api_1_1_ecat.html#a79963c0ec3f0b0cde9ff5c240891fbd6) function. [More...](namespacewmx3_api_1_1ec_api.html#af134992a4fc82e888d1ac0c9c452e538) |
|  | |
| typedef int(\* | [EcSdoUploadCallBack](namespacewmx3_api_1_1ec_api.html#a6a34e4b55dc2cc16e97ff634d7606f97)) (int result, int masterid, int slaveid, int index, int subindex, EcSdoType::T sdoType, int len, unsigned char \*data, unsigned int errorCode) |
|  | Callback function for the [SdoUpload](classwmx3_api_1_1ec_api_1_1_ecat.html#a6c0393c3fa59432294b44e7fd014af12) function. [More...](namespacewmx3_api_1_1ec_api.html#a6a34e4b55dc2cc16e97ff634d7606f97) |
|  | |
| typedef int(\* | [EcRegisterWriteCallBack](namespacewmx3_api_1_1ec_api.html#a870c9568e93034a8213176867dc4c504)) (int result, int masterid, int slaveid, int off, int len, unsigned char \*data) |
|  | Callback function for the [RegisterWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#aaa9d9a890f92780b34f1849f814d56a2) function. [More...](namespacewmx3_api_1_1ec_api.html#a870c9568e93034a8213176867dc4c504) |
|  | |
| typedef int(\* | [EcRegisterReadCallBack](namespacewmx3_api_1_1ec_api.html#ac251d62d4b3020e8ce45cb8857f62cff)) (int result, int masterid, int slaveid, int off, int len, unsigned char \*data) |
|  | Callback function for the [RegisterRead](classwmx3_api_1_1ec_api_1_1_ecat.html#ad354040fa7d8ab09b91af43891948691) function. [More...](namespacewmx3_api_1_1ec_api.html#ac251d62d4b3020e8ce45cb8857f62cff) |
|  | |
| typedef int(\* | [EcRegisterBroadcastWriteCallBack](namespacewmx3_api_1_1ec_api.html#a7391b529a1982692ea377e78205c4d65)) (int result, int masterid, int off, int len, unsigned char \*data, int wkc) |
|  | Callback function for the [RegisterBroadcastWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#a5c3f17d584f9ee740b3bc854134d4776) function. [More...](namespacewmx3_api_1_1ec_api.html#a7391b529a1982692ea377e78205c4d65) |
|  | |
| typedef int(\* | [EcRegisterBroadcastReadCallBack](namespacewmx3_api_1_1ec_api.html#abf84c6a6d6b9b84bae074b23662c8568)) (int result, int masterid, int off, int len, unsigned char \*data, int wkc) |
|  | Callback function for the [RegisterBroadcastRead](classwmx3_api_1_1ec_api_1_1_ecat.html#a1ece3b832d046ae2b9b36d078b791893) function. [More...](namespacewmx3_api_1_1ec_api.html#abf84c6a6d6b9b84bae074b23662c8568) |
|  | |
| typedef int(\* | [EcSdoInfoGetODListCallBack](namespacewmx3_api_1_1ec_api.html#ad20d73389d4251646110b488ebd2431b)) (int result, int masterid, int slaveid, EcObjectDescriptionListType::T type, EcSlaveSdoInfoObjectDescriptionList \*list) |
|  | Callback function for the [GetSdoInfoODList](classwmx3_api_1_1ec_api_1_1_ecat.html#a69a56557ac7c66f1a62ae1ae190a2b1d) function. [More...](namespacewmx3_api_1_1ec_api.html#ad20d73389d4251646110b488ebd2431b) |
|  | |
| typedef int(\* | [EcSdoInfoGetEDListCallBack](namespacewmx3_api_1_1ec_api.html#a15a2382712e289247524aa8b3a4ad4d9)) (int result, int masterid, int slaveid, int index, EcSlaveSdoInfoEntryDescriptionList \*list) |
|  | Callback function for the [GetSdoInfoEDList](classwmx3_api_1_1ec_api_1_1_ecat.html#abf7f58c8b7755aff5f6f561716f0e47a) function. [More...](namespacewmx3_api_1_1ec_api.html#a15a2382712e289247524aa8b3a4ad4d9) |
|  | |
| typedef int(\* | [EcFoEReadCallBack](namespacewmx3_api_1_1ec_api.html#aa00f07a296d89f35072cfb132fa1b27c)) (int result, int masterid, int slaveId, wchar\_t \*filePath, char \*fileName, unsigned int password, unsigned int errorCode) |
|  | Callback function for the [FoERead](classwmx3_api_1_1ec_api_1_1_ecat.html#a463f351ebea80dfb98dab9ddda2f3a28) function. [More...](namespacewmx3_api_1_1ec_api.html#aa00f07a296d89f35072cfb132fa1b27c) |
|  | |
| typedef int(\* | [EcFoEWriteCallBack](namespacewmx3_api_1_1ec_api.html#a6581cdda41e7bfd961819a9b7c6ccefc)) (int result, int masterid, int slaveId, wchar\_t \*filePath, char \*fileName, unsigned int password, unsigned int errorCode) |
|  | Callback function for the [FoEWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#abce4f5f68a3303e5493aaa95a626e6d7) function. [More...](namespacewmx3_api_1_1ec_api.html#a6581cdda41e7bfd961819a9b7c6ccefc) |
|  | |
| typedef int(\* | [EcSIIWriteCallBack](namespacewmx3_api_1_1ec_api.html#a1e36b98120b32ece7d47593c2a335037)) (int result, int masterid, int slaveid, int addr, int len, unsigned char \*data) |
|  | Callback function for the [SIIWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#a831668e881055d38a24e3f59c49eac1f) function. [More...](namespacewmx3_api_1_1ec_api.html#a1e36b98120b32ece7d47593c2a335037) |
|  | |
| typedef int(\* | [EcSIIReadCallBack](namespacewmx3_api_1_1ec_api.html#a7897f6a2030e13ae696d170a31d9e74d)) (int result, int masterid, int slaveid, int addr, int len, unsigned char \*data) |
|  | Callback function for the [SIIRead](classwmx3_api_1_1ec_api_1_1_ecat.html#ae1d5bf8612d78851090c2f7a01e3ffff) function. [More...](namespacewmx3_api_1_1ec_api.html#a7897f6a2030e13ae696d170a31d9e74d) |
|  | |
| typedef int(\* | [EcAoEReadCallBack](namespacewmx3_api_1_1ec_api.html#aa925bd1694d968b685c663802f54412d)) (int result, int masterid, int slaveId, unsigned char targetNetId[6], unsigned short targetPort, unsigned char senderNetId[6], unsigned short senderPort, unsigned int indexGroup, unsigned int indexOffset, unsigned int readLength, unsigned char \*aoeBuff, unsigned int errorCode) |
|  | Callback function for the [AoERead](classwmx3_api_1_1ec_api_1_1_ecat.html#ab6c57522d0498633fdd8cdf937f65ba4) function. [More...](namespacewmx3_api_1_1ec_api.html#aa925bd1694d968b685c663802f54412d) |
|  | |
| typedef int(\* | [EcAoEWriteCallBack](namespacewmx3_api_1_1ec_api.html#a51595de45cab9ca3cbd05a04d8a4104d)) (int result, int masterid, int slaveId, unsigned char targetNetId[6], unsigned short targetPort, unsigned char senderNetId[6], unsigned short senderPort, unsigned int indexGroup, unsigned int indexOffset, unsigned int writeLength, unsigned char \*aoeData, unsigned int errorCode) |
|  | Callback function for the [AoEWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#a804827e4d2fa2c98b30ccdd337ff4032) function. [More...](namespacewmx3_api_1_1ec_api.html#a51595de45cab9ca3cbd05a04d8a4104d) |
|  | |
| typedef int(\* | [EcAoEWriteControlCallBack](namespacewmx3_api_1_1ec_api.html#a6286a3f2b18e41e642b41e3478c3a117)) (int result, int masterid, int slaveId, unsigned char targetNetId[6], unsigned short targetPort, unsigned char senderNetId[6], unsigned short senderPort, unsigned short aoeState, unsigned short deviceState, unsigned int writeLength, unsigned char \*aoeData, unsigned int errorCode) |
|  | Callback function for the [AoEWriteControl](classwmx3_api_1_1ec_api_1_1_ecat.html#a4db1afd22e5e1ee0003102e7da5fdb1e) function. [More...](namespacewmx3_api_1_1ec_api.html#a6286a3f2b18e41e642b41e3478c3a117) |
|  | |
| typedef int(\* | [EcSoEReadCallBack](namespacewmx3_api_1_1ec_api.html#a9ae5400d7fcaf82368f6df5d4b67d87c)) (int result, int masterid, int slaveId, unsigned char driveNo, unsigned char elementFlags, unsigned short idn, unsigned int buffSize, unsigned char \*readSoEBuffer, unsigned int errorCode) |
|  | Callback function for the [SoERead](classwmx3_api_1_1ec_api_1_1_ecat.html#a334f3f3b4ece7f44a14912ee99e0396b) function. [More...](namespacewmx3_api_1_1ec_api.html#a9ae5400d7fcaf82368f6df5d4b67d87c) |
|  | |
| typedef int(\* | [EcSoEWriteCallBack](namespacewmx3_api_1_1ec_api.html#ab0c5ce150259962c50b5772a0701ceda)) (int result, int masterid, int slaveId, unsigned char driveNo, unsigned char elementFlags, unsigned short idn, unsigned int dataSize, unsigned char \*writeSoEData, unsigned int errorCode) |
|  | Callback function for the [SoEWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#a73d0901af69d1006adcf92743702960e) function. [More...](namespacewmx3_api_1_1ec_api.html#ab0c5ce150259962c50b5772a0701ceda) |
|  | |
| typedef int(\* | [EcVoEReadCallBack](namespacewmx3_api_1_1ec_api.html#a3eb7771cf17d9d939e8fd604b4e1d76d)) (int result, int masterid, int slaveId, unsigned int vendorId, unsigned short vendorType, unsigned int readDataSize, unsigned char \*readVoEBuffer) |
|  | Callback function for the [VoERead](classwmx3_api_1_1ec_api_1_1_ecat.html#a9252f1e61598e56dc6a870390b5093ae) function. [More...](namespacewmx3_api_1_1ec_api.html#a3eb7771cf17d9d939e8fd604b4e1d76d) |
|  | |
| typedef int(\* | [EcVoEWriteCallBack](namespacewmx3_api_1_1ec_api.html#aa96f53709c52cd41997d3797a25c0203)) (int result, int masterid, int slaveId, unsigned int vendorId, unsigned short vendorType, unsigned int writeDataSize, unsigned char \*writeAoEData) |
|  | Callback function for the [VoEWrite](classwmx3_api_1_1ec_api_1_1_ecat.html#a810d3bb77e7fcdc250850a4cbf6fe4d1) function. [More...](namespacewmx3_api_1_1ec_api.html#aa96f53709c52cd41997d3797a25c0203) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxMasters](namespacewmx3_api_1_1ec_api_1_1constants.html#aa96d6ef663c97168b2418f7c8b3e5a86) = 2 |
|  | The maximum number of masters that are held by EcMasterInfoList. |
|  | |
| static const int | [maxSlaves](namespacewmx3_api_1_1ec_api_1_1constants.html#aee4109b420bd4c70b4a9151a2a8efc86) = 256 |
|  | The maximum number of slaves that are held by MasterInfo. |
|  | |
| static const int | [maxSlaveAxes](namespacewmx3_api_1_1ec_api_1_1constants.html#a9cf5e8816bcce31f03d471a4c6cae238) = 16 |
|  | The maximum number of axes that are held by SlaveInfo. |
|  | |
| static const int | [maxEniFilePathLen](namespacewmx3_api_1_1ec_api_1_1constants.html#ad5d6af703933bc40af6babc4edaac701) = 256 |
|  | The maximum number of characters that are used to specify the ENI file path. |
|  | |
| static const int | [maxFoEFilePathLen](namespacewmx3_api_1_1ec_api_1_1constants.html#a929a58e87c05b218d76ae48e12e9ed9b) = 256 |
|  | The maximum number of characters that are used to specify the FoE file path. |
|  | |
| static const int | [maxFoEFileNameLen](namespacewmx3_api_1_1ec_api_1_1constants.html#a09a2ce707d09eaf343fcb9b6f2ae1960) = 64 |
|  | The maximum number of characters that are used to specify the FoE name. |
|  | |
| static const int | [maxSdoInfoNameLen](namespacewmx3_api_1_1ec_api_1_1constants.html#a68c7d9cf36cc113216b234e187428b43) = 64 |
|  | The maximum number of characters that are used to specify the OD (Object Description) name in SDO info. |
|  | |
| static const int | [maxSdoInfoODListSize](namespacewmx3_api_1_1ec_api_1_1constants.html#acf74541f4f13caa847d01beb162b6da9) = 450 |
|  | The maximum size of the OD (Object Description) list. |
|  | |
| static const int | [maxSdoInfoEDListSize](namespacewmx3_api_1_1ec_api_1_1constants.html#abeec7cce2f31c1c52fbffb3dd512cd3d) = 256 |
|  | The maximum size of the ED (Entry Description) list. |
|  | |
| static const int | [maxLogPdoSize](namespacewmx3_api_1_1ec_api_1_1constants.html#a0f004a6a6e71968a513c7145fef6640d) = 256 |
|  | The maximum size of the pdo size which could be logged. |
|  | |
| static const int | [maxLogPdoDataSize](namespacewmx3_api_1_1ec_api_1_1constants.html#a839ba7dc8c67ccc33b8b3d6d9c60c9a2) = 8 |
|  | The maximum size of the pdo data size which could be logged. |
|  | |
| static const int | [maxMappedRxPdo](namespacewmx3_api_1_1ec_api_1_1constants.html#ac8934c4ac06531ce06dbcad8c460babd) = 128 |
|  | The maximum size of rx pdo to be mapped. |
|  | |
| static const int | [maxMappedTxPdo](namespacewmx3_api_1_1ec_api_1_1constants.html#a9b09884b60866af864a010b5a77ee0fa) = 128 |
|  | The maximum size of tx pdo to be mapped. |
|  | |




* [ec](dir_b356fbe7affd4119806fd5928bc121f5.html)
* [include](dir_4daffc0dc7a68dc07bfac276859666c8.html)
* [EcApi.h](_ec_api_8h.html)



