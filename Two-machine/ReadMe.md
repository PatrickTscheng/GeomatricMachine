# 双机器模拟
文件说明
sim2.py 和 direct2.py 为两个执行程序，输入模拟需要的数值，执行后输出结果
individual.py buffer.py two_machine.py 是类文件，不能直接运行

## sim2.py
调用 two_machine.py 以及 individual.py buffer.py 三个类文件
* individual.py 模拟一个机器的运行状态
* buffer.py 模拟两个机器中间的 buffer 即缓冲区的状态
* two_machine.py 模拟，两个机器运行状态下，反回每次运行区间结束后各机器的状态
sim2.py 执行后输出 result_sim.txt 文件，显示出随着时间段变化，机器运行的状态所发生的改变

## direct2.py
direct2.py 为直接计算概率方式，通过建立的简单数学模型，通过矩阵运算直接得出机器的参数
得到的结果保存在 result1.txt 文件内