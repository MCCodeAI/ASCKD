

✅ 内容分块功能已成功实施并验证完成！

主要成果：

所有sdbody内容（body_s, h1, h2）现在会在超过8,192 tokens时自动分块
使用段落级分割策略保持语义完整性
正确建立了composes和follows关系
所有chunk都在token限制内（测试最大值：7,813 tokens）
验证结果：

测试文件成功分成16个chunk
第1个chunk建立infile引用
后续chunks建立composes（指向第1个chunk）和follows（指向前一个chunk）关系
请查看walkthrough了解详细实现和测试结果。


WMX3 User Manual: SimuApi.h File Reference



| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Macros](#define-members) 
SimuApi.h File Reference 

| Classes | |
| --- | --- |
| class | [SimuAxisState](classwmx3_api_1_1simu_api_1_1_simu_axis_state.html) |
|  | This enumerator class enumerates the simulator axis states. [More...](classwmx3_api_1_1simu_api_1_1_simu_axis_state.html#details) |
|  | |
| class | [SimuErrorCode](classwmx3_api_1_1simu_api_1_1_simu_error_code.html) |
|  | This enumerator class enumerates the Simu library error codes. [More...](classwmx3_api_1_1simu_api_1_1_simu_error_code.html#details) |
|  | |
| class | [SimuAxisSignal](classwmx3_api_1_1simu_api_1_1_simu_axis_signal.html) |
|  | This class describes the simulator axis signal. [More...](classwmx3_api_1_1simu_api_1_1_simu_axis_signal.html#details) |
|  | |
| class | [SimuAxisData](classwmx3_api_1_1simu_api_1_1_simu_axis_data.html) |
|  | This class describes the simulator axis data. [More...](classwmx3_api_1_1simu_api_1_1_simu_axis_data.html#details) |
|  | |
| class | [SimuIoData](classwmx3_api_1_1simu_api_1_1_simu_io_data.html) |
|  | This class describes the simulator IO data. [More...](classwmx3_api_1_1simu_api_1_1_simu_io_data.html#details) |
|  | |
| class | [SimuMasterInfo](classwmx3_api_1_1simu_api_1_1_simu_master_info.html) |
|  | This class describes the simulator master information. [More...](classwmx3_api_1_1simu_api_1_1_simu_master_info.html#details) |
|  | |
| class | [Simu](classwmx3_api_1_1simu_api_1_1_simu.html) |
|  | **This class contains Simu API functions.**  [More...](classwmx3_api_1_1simu_api_1_1_simu.html#details) |
|  | |

| Macros | |
| --- | --- |
| #define | **SIMUAPIFUNC**   HRESULT |
|  | |




* [simu](dir_b95b1c29731b5660a7109d816f9c0663.html)
* [include](dir_23bd7f0f6b8cae3eed424feea7836638.html)
* [SimuApi.h](_simu_api_8h.html)



