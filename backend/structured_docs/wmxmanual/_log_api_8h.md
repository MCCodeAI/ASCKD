




WMX3 User Manual: LogApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
LogApi.h File Reference 

| Classes | |
| --- | --- |
| class | [LogErrorCode](classwmx3_api_1_1_log_error_code.html) |
|  | This enumerator class enumerates the WMX3 log library error codes. [More...](classwmx3_api_1_1_log_error_code.html#details) |
|  | |
| class | [LogState](classwmx3_api_1_1_log_state.html) |
|  | This enumerator class enumerates the states of data logging channels. Also see [Log Statuses](_w_m_x_d_o_c__f_u_n_c__l_o_g__s_t_a_t_u_s.html). [More...](classwmx3_api_1_1_log_state.html#details) |
|  | |
| class | [LogStatus](classwmx3_api_1_1_log_status.html) |
|  | This class contains the status of a data logging operation. Also see [Log Statuses](_w_m_x_d_o_c__f_u_n_c__l_o_g__s_t_a_t_u_s.html). [More...](classwmx3_api_1_1_log_status.html#details) |
|  | |
| class | [LogOptions](classwmx3_api_1_1_log_options.html) |
|  | This class contains options that specify the data to collect during a data logging operation. [More...](classwmx3_api_1_1_log_options.html#details) |
|  | |
| class | [IOLogFormat](classwmx3_api_1_1_i_o_log_format.html) |
|  | This class contains options that specify a region of I/O to log during a data logging operation. [More...](classwmx3_api_1_1_i_o_log_format.html#details) |
|  | |
| class | [MLogFormat](classwmx3_api_1_1_m_log_format.html) |
|  | This class contains options that specify a region of user memory to log during a data logging operation. [More...](classwmx3_api_1_1_m_log_format.html#details) |
|  | |
| class | [MemoryLogStatus](classwmx3_api_1_1_memory_log_status.html) |
|  | This class contains the status of a memory log operation. [More...](classwmx3_api_1_1_memory_log_status.html#details) |
|  | |
| class | [MemoryLogAxisData](classwmx3_api_1_1_memory_log_axis_data.html) |
|  | This class contains axis data that has been recorded by a memory log operation. [More...](classwmx3_api_1_1_memory_log_axis_data.html#details) |
|  | |
| class | [MemoryLogIOData](classwmx3_api_1_1_memory_log_i_o_data.html) |
|  | This class contains I/O data that has been recorded by a memory log operation. [More...](classwmx3_api_1_1_memory_log_i_o_data.html#details) |
|  | |
| class | [MemoryLogMData](classwmx3_api_1_1_memory_log_m_data.html) |
|  | This class contains user memory data that has been recorded by a memory log operation. [More...](classwmx3_api_1_1_memory_log_m_data.html#details) |
|  | |
| class | [MemoryLogOptions](classwmx3_api_1_1_memory_log_options.html) |
|  | This class contains additional options for a memory log operation. [More...](classwmx3_api_1_1_memory_log_options.html#details) |
|  | |
| class | [MemoryLogDatas](classwmx3_api_1_1_memory_log_datas.html) |
|  | This class contains data that has been logged using the memory log operation. This class contains data for one cycle. [More...](classwmx3_api_1_1_memory_log_datas.html#details) |
|  | |
| class | [MemoryLogData](classwmx3_api_1_1_memory_log_data.html) |
|  | This class contains data that has been logged using the memory log operation. This class contains data over multiple cycles. [More...](classwmx3_api_1_1_memory_log_data.html#details) |
|  | |
| class | [LogChannelOptions](classwmx3_api_1_1_log_channel_options.html) |
|  | This class contains options for a log operation channel. [More...](classwmx3_api_1_1_log_channel_options.html#details) |
|  | |
| class | [LogFilePathA](classwmx3_api_1_1_log_file_path_a.html) |
|  | This class contains the file path for a log operation. The file path is specified as a char string. [More...](classwmx3_api_1_1_log_file_path_a.html#details) |
|  | |
| class | [LogFilePathW](classwmx3_api_1_1_log_file_path_w.html) |
|  | This class contains the file path for a log operation. The file path is specified as a wchar\_t string. [More...](classwmx3_api_1_1_log_file_path_w.html#details) |
|  | |
| class | [DetailLogState](classwmx3_api_1_1_detail_log_state.html) |
|  | This enumerator class enumerates the states of data logging channels. There are several more states compared to [LogState](classwmx3_api_1_1_log_state.html). Also see [Log Statuses](_w_m_x_d_o_c__f_u_n_c__l_o_g__s_t_a_t_u_s.html). [More...](classwmx3_api_1_1_detail_log_state.html#details) |
|  | |
| class | [DetailLogBufferStatus](classwmx3_api_1_1_detail_log_buffer_status.html) |
|  | This class contains the status of a log buffer. [More...](classwmx3_api_1_1_detail_log_buffer_status.html#details) |
|  | |
| class | [DetailLogStatus](classwmx3_api_1_1_detail_log_status.html) |
|  | This class contains the status of a data logging operation. Compared to [LogStatus](classwmx3_api_1_1_log_status.html), there are several additional statuses. Also see [Log Statuses](_w_m_x_d_o_c__f_u_n_c__l_o_g__s_t_a_t_u_s.html). [More...](classwmx3_api_1_1_detail_log_status.html#details) |
|  | |
| class | [DetailLogMemoryStatus](classwmx3_api_1_1_detail_log_memory_status.html) |
|  | Reserved. [More...](classwmx3_api_1_1_detail_log_memory_status.html#details) |
|  | |
| class | [LogApiLogInput](classwmx3_api_1_1_log_api_log_input.html) |
|  | This class specifies the log data to be collected by the Log module. [More...](classwmx3_api_1_1_log_api_log_input.html#details) |
|  | |
| class | [LogApiLogOutput](classwmx3_api_1_1_log_api_log_output.html) |
|  | This class contains data of the Log module that has been logged using the memory log operation. This class contains data over multiple cycles. [More...](classwmx3_api_1_1_log_api_log_output.html#details) |
|  | |
| class | [LogType](classwmx3_api_1_1_log_type.html) |
|  | This enumerator contains the type of log. [More...](classwmx3_api_1_1_log_type.html#details) |
|  | |
| class | [ApiLogType](classwmx3_api_1_1_api_log_type.html) |
|  | This enumerator contains the type of API log. [More...](classwmx3_api_1_1_api_log_type.html#details) |
|  | |
| class | [ApiLogInfo](classwmx3_api_1_1_api_log_info.html) |
|  | This class contains API log information for the command or response of one API function call. [More...](classwmx3_api_1_1_api_log_info.html#details) |
|  | |
| class | [ApiLogOptions](classwmx3_api_1_1_api_log_options.html) |
|  | This class contains API log options. [More...](classwmx3_api_1_1_api_log_options.html#details) |
|  | |
| class | [ApiLogState](classwmx3_api_1_1_api_log_state.html) |
|  | This enumerator class enumerates the states of the API log. [More...](classwmx3_api_1_1_api_log_state.html#details) |
|  | |
| class | [ApiLogStatus](classwmx3_api_1_1_api_log_status.html) |
|  | This class contains the status of the API log. [More...](classwmx3_api_1_1_api_log_status.html#details) |
|  | |
| class | [Log](classwmx3_api_1_1_log.html) |
|  | **This class contains log functions.**  [More...](classwmx3_api_1_1_log.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const unsigned int | [maxLogBufferSize](namespacewmx3_api_1_1constants.html#aae97a0508b580f86c246085f8c286fa5) = ((unsigned int)2048 \* 1024) |
|  | The buffer size of a log channel. Up to this many samples can be stored in the log buffer without being written to file before samples get overwritten (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogBufferSampleSize](namespacewmx3_api_1_1constants.html#aab10540c93c3e54d3bb8a8ec06b25219) = 80 |
|  | The maximum number of samples that can be stored in the log buffer before a buffer overflow occurs (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogChannel](namespacewmx3_api_1_1constants.html#a498402f60089fcf1527bc697fa71fb85) = 16 |
|  | The number of log channels (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogHeaderBytes](namespacewmx3_api_1_1constants.html#a528d08cc6578c86d49bb8dc2be494181) = 4096 |
|  | The maximum number of bytes in the log header string (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogHeaderLines](namespacewmx3_api_1_1constants.html#a801cce4214db4a1abb313eaae45fb650) = 2048 |
|  | The maximum number of lines in the log header string (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogDirSize](namespacewmx3_api_1_1constants.html#a1d382232ef477565dbe058de55841d38) = 260 |
|  | The maximum number of characters in the log file directory (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogFileNameSize](namespacewmx3_api_1_1constants.html#a285fc48734748d7266782a7d55253e01) = 260 |
|  | The maximum number of characters in the log file name (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogDataSize](namespacewmx3_api_1_1constants.html#a97da74de6e80395de5e9ba5c9e6e59a9) = (32 \* 1024) |
|  | The maximum amount of data in bytes that can be collected per communication cycle per channel (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogDelimiterSize](namespacewmx3_api_1_1constants.html#adaeb7828387b575a87a418134f4ff319) = 8 |
|  | The maximum number of characters in the log delimiter (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxLogPrecision](namespacewmx3_api_1_1constants.html#a5e3c28938814d93ed42b36244fdd5725) = 20 |
|  | The maximum value that can be specified for the precision parameter (the maximum number of subdecimal digits in the log output)(also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogBufferSize](namespacewmx3_api_1_1constants.html#a507e69b0e8b7ab5426d6f11a6c98d82f) = 1024 |
|  | The buffer size of a memory log channel. Up to this many samples can be stored in the memory log buffer without being read before samples get overwritten (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogChannel](namespacewmx3_api_1_1constants.html#a01018f58dd0e151350e4b68c790e0a47) = 16 |
|  | The number of memory log channels (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogAxesSize](namespacewmx3_api_1_1constants.html#a72c81cc5d76a632506ab6f7eb9c83620) = 8 |
|  | The maximum number of axes that can be logged at once by the memory log (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogDataSize](namespacewmx3_api_1_1constants.html#aa92a1bfce4c8a959df97925b66ebbcdd) = 100 |
|  | The maximum number of samples that may be read from the memory log at once (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogIoInputByteSize](namespacewmx3_api_1_1constants.html#affc4650a30e569b887a35fd05dd44d9e) = 128 |
|  | The maximum number of I/O input bytes that can be logged at once by the memory log. A byte is fully counted toward this limit even if only one bit of the byte is logged (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogIoOutputByteSize](namespacewmx3_api_1_1constants.html#a605a88aba9ee6ae2399597d23739f914) = 128 |
|  | The maximum number of I/O output bytes that can be logged at once by the memory log. A byte is fully counted toward this limit even if only one bit of the byte is logged (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogMDataByteSize](namespacewmx3_api_1_1constants.html#a7481c360521487b6350687125d9bf2a9) = 128 |
|  | The maximum number of user memory bytes that can be logged at once by the memory log. A byte is fully counted toward this limit even if only one bit of the byte is logged (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |
| static const int | [maxMemLogTriggerEventSize](namespacewmx3_api_1_1constants.html#ac4e970698cab05da54a3194eae128a6f) = 32 |
|  | The maximum number of events that can be configured to trigger the memory data log (also see [Log Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__l_o_g.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [LogApi.h](_log_api_8h.html)



