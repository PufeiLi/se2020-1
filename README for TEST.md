# test work
--------

## 测试前准备工作
1. 替换三角函数的UI
2. UI完善：增加一个测试的按钮，点击按钮开始测试，弹出测试窗口 
3. 设定测试指标：函数测试误差<0.001，窗口显示结果正确；误差>0.001，显示结果错误，打补丁
4. 设定测试内容

--------
### **1.测试目的**
  - 软件测试是为了发现错误而执行程序的过程
  - 测试目的在于尽可能多地发现并排除软件中潜藏的错误，最终把一个高质量的三角函数计算包交给用户使用

### **2.测试数据设置和指标**
  - 测试数据设置：
     - 测试次数：1000次
     - 测试的随机输入数值范围：（0,360）
  - 测试指标
     - 函数测试误差：0.001    

### **3.测试内容**
  - 判断输入：
     - 输入为数值，则进行计算；
     - 输入为非数值，则弹出输入错误
  - 输入数值位数：
     - 
  - 测试平均计算误差
     - 平均计算误差的计算方法：对测试过程中每次计算误差求和/测试中计算次数1000 *（*注：测试过程中计算产生误差的次数的计算：对每一次的计算都计算测试误差，<0.001，则记一次错误*）*
     - 函数测试误差<0.001，窗口显示结果正确
     - 函数测试误差>0.001，窗口显示结果错误

### **4.测试文件**
  - **python：**
     - Test_sin_se.py文件：是python语言编写的文件，实现对sin_se功能模块的的测试
     - Test_cos_se.py文件：功能如上
     - Test_tan_se.py文件：功能如上
     - Test_cot_se.py文件：功能如上
  - **matlab：**
     - Test_sin_se.m文件：是matlab语言编写的文件，实现对sin_se功能模块的的测试
     - Test_cos_se.m文件：功能如上
     - Test_tan_se.m文件：功能如上
     - Test_cot_se.m文件：功能如上

### **5.测试操作**
  - 运行程序，在运行界面上点击测试按钮，弹出对应的测试窗口，显示测试结果
  - 测试结果分析：
       A、测试窗口显示结果正确，则表示函数测试误差小于0.001；
       B、测试窗口显示结果错误，误差大于0.001

### **6.测试用例简述
  - test1：输入非数字字符
    - 输入非数字字符，点击计算没有结果，后台有报错
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/non-numeric_character.png)
    - 后台报错：![](https://github.com/PufeiLi/se2020-1/blob/test/non-numeric_error.png)
    - 打补丁：----
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/non-numeric_correct.bmp)
  - test2：输入数字位数过长
    - 输入5位数及以上，计算就会卡住
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/longnum.png)
    - 打补丁：----
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/longnum_correct.bmp)
  - test3：调用测试模块
    - 初始测试结果：测试结果未全部通过，测试结果显示：matlab语言的sin tan cot 函数有报错，不满足误差小于0.001的要求
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/Init_test_result.png)
    - 打补丁：
         - 1.sin_se()：
         - 2.tan_se()：
         - 3.cot_se()：
    - 测试通过：两种语言编写三角函数包的误差都小于0.001，测试全部通过，即界面显示pass！
    - 图示：![](https://github.com/PufeiLi/se2020-1/blob/test/corr_test_result.bmp)

### **6.测试界面**
 
- 测试界面如下：![](https://github.com/PufeiLi/se2020-1/blob/test/Testing_interface.png)

- 测试情况说明：
      
      - 输入非数字字符：![](http://github.com/PufeiLi/se2020-1/blob/test/non-numeric_error.png)
      
      - 输入过长数值：![](https://github.com/PufeiLi/se2020-1/blob/test/longnum_correct.bmp)

      - 测试成功界面：![](https://github.com/PufeiLi/se2020-1/blob/test/corr_test_result.bmp)


