## 数据统计

1. **省/市/区县/基站信息**的资料在[这里](../test/JSCMCC/data/)
2. `省区域.csv`、`市区域.csv`、`县区区域.csv`文件中每行数据中的字段以英文逗号`,`分隔，具体格式说明如下：

   | 序号 | 字段名称   | 类型 | 备注                             |
   | :- | :----- | :- | :----------------------------- |
   | 1  | 区域ID   | 字符 | 该区域对象在系统中的编号。编号具有唯一性，唯一地表示一个区域 |
   | 2  | 区域名称   | 字符 | 区域名称                           |
   | 3  | 上级区域ID | 字符 | 999表示不关注上级                     |
3. `基站.csv`文件中每行数据中的字段以英文逗号`,`分隔，具体格式说明如下：

   | 序号 | 属性     | 字段类型 | 备注                             |
   | :- | :----- | :--- | :----------------------------- |
   | 1  | 基站ID   | 字符   | 该基站对象在系统中的编号。编号具有唯一性，唯一地表示一个基站 |
   | 2  | 基站名称   | 字符   |                                |
   | 3  | 基站类型   | 字符   |                                |
   | 4  | 所属区县ID | 字符   | 与区县区域资源信息表中区域ID对应              |
   | 5  | 基站状态   | 字符   | 基站状态可能为：在网、工程、退网               |
4. 统计河南省本地网（地级市）的数量，县区的数量，全省可用基站的数量（不含工程标记和退网标记）以及全省基站的数量，并输出至文件`count.csv`，结果分为四行，每行一个数字：
   - 第一行为本地网数
   - 第二行为县区数
   - 第三行为可用基站数
   - 第四行为基站数；
5. 输出的结果是：

       18
        188
        49772	
        50000
