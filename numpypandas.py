'''
                                                     --------------
                                                    | DATA SCIENCE |
                                                     --------------

What is  Data?

    Data is an raw fact consisting of wanted and unwanted data, it is a unprocessed data.

What is information?

    It is a processed data or wanted data

What is science?

    Study of things is called science.

What is data science?

    ->Study of data is known as data science.
    ----------          -------         ----------------
   | Past data | ----> | Model | ----> | Future outcome |
    ----------          -------         ----------------
    ->It is a process of extracting the past data to train a model, so that it can predict the future outcome.
    
PROCESS INVOLVED IN DATA SCIENCE:

     -----------------        ---------------         ---------------------         --------------------         -----------------------         ------------------         ---------         -------------
    | Data extraction |----> | Data cleaning | ----> | Feature Engineering | ----> | Data visualization | ----> | Business Intelligence | ----> | Machine learning | ----> | Testing | ----> | Deployement |
     -----------------        ---------------         ---------------------         --------------------         -----------------------         ------------------         ---------         -------------

1) DATA EXTRACTION:

    ->It is a process of extracting the data from different sources.
    ->Sources are nothing but files, database, data warehouse, application and software, companies.

    ->Skills required:
        Excel, powerbi, sql and database.

2) DATA CLEANING:

    -> It is a process of removing the unwanted data by extracting or keeping the wanted data.

    ->Skills required:
        Python, numpy, pandas, powerbi.

3) FEATURE ENGINEERING:(Optional)

    ->It is a process of creating new columns with the help of existing data.
    
    ->Skills required:
        Numpy, pandas, powerbi

4)DATA VISUALIZATION:

    ->It is a process of converting the normal data into graphical or pictorial representation.

    ->Skills required:
        PowerBI, Matplotlip

NOTE: IF YOU KNOW ALL THIS FOUR PROCESS YOU CAN BECOME DATA ANALYST.

5)BUSINESS INTELLIGENCE:

    ->It is nothing but having the proper domain knowledge such as agriculture, food industry, products, healthcare etc...
    ->Business intelligence developer will take the data provided by the data analyst and he will create the dashboard which will help the company to take the better decision.

6)MACHINE LEARNING:

    ->It is a heart of data science.
    ->It is a process of training a model so that it can predict the future outcome.

7)TESTING:

    ->We are going to test the machine learning model, the accuracy should be between 93-98.

8)Deployement:

    ->Based on the accuracy, the model will be available for real world use.

                                                 -------
                                                | NUMPY |
                                                 -------
NUMPY:

    ->Numpy stands for Numerical python. It is a python library which is used to create array, perform fast mathematical operation on array.

ARRAY:

    ->It is a collection of homogenous elements enclosed within square brackets.

HOW TO CREATE ARRAY:

    ->Import NUMPY as np
    ->var=np.array(col)
    ->We can pass all the collection, but list and tuple will work properly.
    ->String is considered as an single value.
    ->Set and Dictionary is considered as an single object. 

    ->Example:
        ""import numpy as np
          arr=np.array([1,2,3,4])
          print(arr)""

          Output : [1,2,3,4]

    ->If we are passing heterogenous values, it will convert into based on priorities.
    ->Priorities:(Right to left)
            Bool -> int -> float -> complex -> str -> set(object) -> dict(object)

    ->Example:
        ""import numpy as np
          arr=np.array([1,2,3,4.5])
          print(arr)""

          Output : [1.  2.  3.  4.5]

TYPES OF ARRAY:

    ->1-Dimension Array(1-D), 2-Dimension Array(2-D), 3-Dimension Array(3-D), N-Dimension Array(N-D)

    ->1-D ARRAY:

        ->It is a one dimension array just like a single row.
        ->Example:
            arr=np.array([4,5,6,7])

    ->2-D ARRAY:

        ->It is a two dimension array just like a matrix or table, consisting of rows and columns.
        ->Example:
            arr=np.array([[1,2,3],[4,5,6]])
        NOTE: The number of elements should be same in all the rows but it can have n number of rows.

    ->3-D ARRAY:

        ->It ia a three dimension array, it's an collection of 2-D Array, consisting of layers, rows and columns.
        ->One 2-D Array is known as one layer.
        ->Example:
            arr=np.array([[[1,2],[4,5]],[[3,6],[7,8]]])
        NOTE: Number of rows and number of columns should be same in each and every layer, the number of layers can be anything.

ATTRIBUTES:

    ->D-TYPE:

        ->It is used to check the data type of an elements present in an array.
        ->SYNTAX: array.dtype
        ->Example:
            ""a=np.array([23,45,'a'])
            a.dtype""

            OUTPUT: dtype('<U21')

    ->NDIM:

        ->It will return the dimension of the array
        ->SYNTAX: array.ndim
        ->EXAMPLE:
            ""a=np.array([[1,2,3],[4,5,6]])
            a.ndim""

            OUTPUT: 2

    ->SHAPE:

        ->It will return the number of layers, rows and columns
        ->SYNTAX: array.shape

        ->FOR 1-D: It will return the number of elements in the form of tuple.
        ->EXAMPLE:
            ""a=np.array([23,45,'a'])
              a.shape""

              OUTPUT: (3,)

        ->FOR 2-D: It will return number of rows and number of columns in the form of tuple. 
        ->EXAMPLE:
            ""a=np.array([[1,2,3],[4,5,6]])
              a.shape""

              OUTPUT:(2,3)

        ->FOR 3-D: It will return the number of layers, number of rows and number of columns in the form of tuple.
        ->EXAMPLE:
            ""a=np.array([[[1,2,3],[3,4,5]],[[6,7,8],[0,9,8]]])
              a.shape""

              OUTPUT:(2,2,3)

    ->RESHAPE:
        
        ->It is used to convert one dimension of array into another dimension of array.
        ->SYNTAX:variable.reshape(argument)

        ->CONVERTING 1-D TO 2-D:
            ->SYNTAX: arr.reshape(r,c)
            ->EXAMPLE: 
                ""arr=np.array([2,3,4,5,6,7,8,9])
                  arr.reshape(2,4)""

                  OUTPUT: array([[2,3,4,5],
                                 [6,7,8,9]])

        ->CONVERTING 2-D TO 1-D (0R) 3-D TO 1-D:
            ->SYNTAX: arr.reshape(-1)

        ->CONVERTING 1-D TO 3-D (or) 2-D TO 3-D:
            ->SYNTAX: arr.reshape(l,r,c)   #  1-D:: l*r*c == Total number of elements (or) 2-D:: l*r*c == r*c
            ->EXAMPLE:
                ""arr=np.array([2,3,4,5,6,7,8,9])
                  arr.reshape(2,2,2)""

                  OUTPUT: [[[2 3]
                            [4 5]]
                            [[6 7]
                            [8 9]]]


IN BUILT FUNCTIONS TO CREATE ARRAY:

    ->ARANGE():

        ->It is used to create an array between the specified range. It can be both integer or float value.
        ->SYNTAX: np.arange(start,end,step)
        ->EXAMPLE:
            ""np.arange(1,10,2)""

              OUTPUT: [1,3,5,7,9]
    
    ->RANDOM.RAND():

        ->It is used to create an array filled with random float values between 0 to 1.
        ->SYNTAX: np.random.rand(arg)

        ->FOR 1-D:
            ->EXAMPLE:
                ""np.random.rand(5)""

                  OUTPUT: [0.1234, 0.4567, 0.8756, 0.8668, 0.1356]

        ->FOR 2-D:
            ->EXAMPLE:
                ""np.random.rand(2,2)""

                  OUTPUT: [[0.28284101 0.52525609]
                           [0.65065845 0.14479339]]

        ->FOR 3-D:
            ->EXAMPLE:
                ""np.random.rand(2,2,2)""

                  OUTPUT: [[[0.84084999 0.39698436]
                            [0.6093761  0.94250294]]
                            [[0.24604128 0.83879027]
                            [0.04771319 0.64084509]]]

22/05/2026:

    ->RANDOM.RANDN():

        ->It is used to create an array filled with random floating values between -infinity to +infinity, but mostly we get the values which are nearest to 0.
        ->SYNTAX: np.random.randn(argument)

        ->FOR 1-D:
            ->EXAMPLE:
                ""np.random.randn(n)""

                  OUTPUT: [-0.04162116 -0.64521733]

        ->FOR 2-D:
            ->EXAMPLE:
                ""np.random.randn(r,c)""

                  OUTPUT: [[ 0.17827036 -2.11665433]
                           [-0.51722295 -1.74553929]]

        ->FOR 3-D:
            ->EXAMPLE:
                ""np.random.randn(l,r,c)""

                  OUTPUT: [[[-0.37344305 -1.26238412]
                            [ 0.59162008  0.35088529]]

                            [[ 0.09768678  0.64048047]
                            [ 0.55532276 -0.77380541]]]

    ->RANDOM.RANDINT():
        
        ->It is used to create an array filled with random integer values between the specified range.
        ->SYNTAX: np.random.randint(start,end,arguments) #in arguments for 2-D or 3-D, it should be given as collection values

        ->FOR 1-D:
            ->EXAMPLE:
                ""np.random.randint(1,10,5)""

                  OUTPUT: [8 6 5 2 8]

        ->FOR 2-D:
            ->EXAMPLE:
                ""np.random.randint(1,10,(2,5))""

                  OUTPUT: [[1 9 9 3 6]
                           [8 9 9 7 6]]

        ->FOR 3-D:
            ->EXAMPLE:
                ""np.random.randint(1,10,(2,2,2))""

                  OUTPUT: [[[7 4]
                            [5 5]]

                            [[3 1]
                            [6 9]]

                            [[9 5]
                            [1 7]]]

    ->LINSPACE():

        ->It is used to create an array with equally spaced values between the specified range. 
        ->By default it will generate only floating values.
        ->SYNTAX: np.linspace(start,end,arguments)
        ->EXAMPLE:
            ""np.linspace(1,10,5)""

              OUTPUT: [ 1.    3.25  5.5   7.75 10.  ]

    ->ZEROS():

        ->It is used to create an array filled with zeros.
        ->When we know the length of the array but we dont know what values to pass, we can use zeros
        ->SYNTAX: np.zeros(arg)

        ->FOR 1-D:
            ->EXAMPLE:
                ""np.zeros(5)""

                  OUTPUT: [0. 0. 0. 0. 0.]

        ->FOR 2-D:
            ->EXAMPLE:
                ""np.zeros((2,5))""

                  OUTPUT:[[0. 0. 0. 0. 0.]
                          [0. 0. 0. 0. 0.]]

        ->FOR 3-D:
            ->EXAMPLE:
                ""np.zeros((2,2,5))""

                  OUTPUT: [[[0. 0. 0. 0. 0.]
                            [0. 0. 0. 0. 0.]]

                            [[0. 0. 0. 0. 0.]
                            [0. 0. 0. 0. 0.]]]
            
    ->ONES():

        ->It is used to create an array filled with one.
        ->When we know the length of the array but we dont know what values to pass, we can use ones.
        ->SYNTAX: np.ones(arg)

        ->FOR 1-D:
            ->EXAMPLE:
                ""np.ones(5)""

                  OUTPUT: [1. 1. 1. 1. 1.]

        ->FOR 2-D:
            ->EXAMPLE:
                ""np.ones((2,5))""

                  OUTPUT:[[1. 1. 1. 1. 1.]
                          [1. 1. 1. 1. 1.]]

        ->FOR 3-D:
            ->EXAMPLE:
                ""np.ones((2,2,5))""

                  OUTPUT: [[[1. 1. 1. 1. 1.]
                            [1. 1. 1. 1. 1.]]

                            [[1. 1. 1. 1. 1.]
                            [1. 1. 1. 1. 1.]]]

    ->VIEW()

        ->It is used to copy the content from one array to another array
        ->If we do mofification for one array it will also affect the another array
        ->SYNTAX: Desti_var=Sor_var.view()
        ->Example:
            ""import numpy as np
              a=np.array([2,3,4,5])
              b=a.view()
              b[0]=10
              print(a,b)""

              OUTPUT: [10  3  4  5] [10  3  4  5]

    ->COPY()

        ->It is used to copy the content from one array to another array
        ->If we do mofification for one array it will not affect the another array
        ->SYNTAX: Desti_var=Sor_var.copy()
        ->Example:
            ""import numpy as np
              a=np.array([2,3,4,5])
              b=a.copy()
              b[0]=10
              print(a,b)""

              OUTPUT: [2  3  4  5] [20  3  4  5]

23/05/2026:

    ->INDEXING:

        ->It is a process of fetching or extracting single element from the array.
        
        ->FOR 1-D:
            ->SYNTAX: Var[Index]
            ->EXAMPLE:
                ""arr=np.array([1,2,3,4])
                  print(arr[1])""

                  OUTPUT: 2
        
        ->FOR 2-D:
            ->SYNTAX: Var[Row_idx][Col_idx] or Var[Row_idx,Col_idx]
            ->EXAMPLE:
                ""arr=np.array([[1,2,3,4][5,6,7,8]])
                  print(arr[1][2])""

                  OUTPUT: 7

        ->FOR 3-D:
            ->SYNTAX: Var[Layer_idx][Row_idx][Col_idx] or Var[Layer_idx,Row_idx,Col_idx]
            ->EXAMPLE:
                ""arr=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
                  print(arr[1][1][3])""

                  OUTPUT: 8
    
    ->SLICING:

        ->It is a process of extracting the group of elements in an ordered sequence.
        ->SYNTAX: Var[start,end,step] #FOR FORWARD: STEP->+VE, START<(END+1)
        ->SYNTAX: Var[start,end,step] #FOR REVERSE: STEP->-VE, START>(END-1)

        ->FOR 1-D:
            ->FORWARD:
                ->SYNTAX: Var[start,end,step]
                ->EXAMPLE:
                    ""arr=np.array([1,2,3,4])
                    print(arr[0:2])""

                    OUTPUT: [1 2]

            ->REVERSE:
                ->SYNTAX: Var[start,end,step] #Step should be negative, start>end
                ->EXAMPLE:
                    ""arr=np.array([1,2,3,4])
                      print(arr[4:2-1:-1])""

                      OUTPUT: [4 3]
            
        ->FOR 2-D:
            ->FORWARD:
                ->SYNTAX: Var[Row_slicing,Col_slicing]
                ->EXAMPLE:
                    ""arr=np.array([[1,2,3,4],[5,6,7,8]])
                      print(arr[0:3,0:2])""

                      OUTPUT: [[1 2]
                              [5 6]]

            ->REVERSE:
                ->SYNTAX: Var[Row_slicing,Col_slicing]
                ->EXAMPLE:
                    ""arr=np.array([[1,2,3,4],[5,6,7,8]])
                      print(arr[::-1,4:1:-1])""

                      OUTPUT: [[8 7]
                               [4 3]]

        ->FOR 3-D:
            ->FORWARD:
                ->SYNTAX: Var[Layer_slicing,Row_slicing,Col_slicing]
                ->EXAMPLE:
                    ""arr=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
                      print(arr[0:1,0:3,0:3])""

                      OUTPUT: [[[1 2 3]
                                [5 6 7]]]

            ->REVERSE:
                ->SYNTAX: Var[Layer_slicing,Row_slicing,Col_slicing]
                ->EXAMPLE:
                    ""arr=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
                      print(arr[::-1,::-1,3:1:-1])""

                      OUTPUT: [[[8 7]
                               [4 3]]
                               [[8 7]
                               [4 3]]]

25/05/2026:

->INBUILT OPERATIONS OF ARRAY:

    ->There are three types of operations we can perform on array.
        ->1) Inbuilt functions.
        ->2) Array to Array operations.
        ->3) Array with constant operations.

    ->INBUILT FUNCTIONS:

        ->MAX:

            ->Max will help user to find maximum value from the array.
            ->SYNTAX: np.max(arr) #arr means collection name
            ->EXAMPLE:
                ""a=np.array([10,20,30,40])
                  print(np.max(a))""

                  OUTPUT: 40

        ->MIN:

            ->Min will give minimum value from the array.
            ->SYNTAX: np.min(arr) #arr means collection name
            ->EXAMPLE:
                ""a=np.array([10,20,30,40])
                  print(np.min(a))""

                  OUTPUT: 10

        ->MEAN:

            ->This attribute will help user to find the average value of the collection
            ->SYNTAX: np.mean(arr) #arr means collection name
            ->EXAMPLE:
                ""a=np.array([10,20,30,40])
                  print(np.mean(a))""

                  OUTPUT: 25.0

        ->MODE:

            ->Mode operation is not present in numpy

        ->MEDIAN:

            ->This attribute  will help user to find middle value from the array
            ->SYNTAX: np.median(arr) #arr means collection name
            ->If the length of the collection is even, then it will take 2 middle values and make average of them to find the median.
            ->EXAMPLE:
                ""a=np.array([10,20,30,40])
                  print(np.median(a))""

                  OUTPUT: 25.0

        ->ABS:

            ->It will help users to make all of the values of an array into positive number
            ->SYNTAX: np.abs(arr) #arr means collection name.
            ->EXAMPLE:
                ""a=np.array([-10,20,-30,40])
                  print(np.median(a))""

                  OUTPUT: [10,20,30,40] 
        
        ->SIZE:

            ->It will help user to find number of elements of the array.
            ->SYNTAX: np.size(arr) #arr means collection name
            ->EXAMPLE:
                ""a=np.array([-10,20,-30,40])
                  print(np.size(a))""

                  OUTPUT: 5

        ->SORT:

            ->It will help user to sort the array
            ->SYNTAX: np.sort(arr) #ascending
            ->EXAMPLE:
                ""a=np.array([-10,20,-30,40])
                  print(np.sort(a))""

                  OUTPUT: [-30,-10,20,40]

        ->SUM:

            ->It will calculate sum of the elements present in the array.
            ->SYNTAX: np.sum(arr)
            ->EXAMPLE:
                ""a=np.array([10,20,30,40])
                  print(np.sum(a))""

                  OUTPUT: 100

26/05/2026:

        ->VARIANCE:

            ->In numpy .var function is used to calculate the variance of array elements.
            ->Variance measures the spread of data by calculating the average of the squared value from the value
            ->SYNTAX: np.var(arr) #arr means collection name
            ->EXAMPLE:
                ""arr=np.array([2,4,6,8,10])
                  print(np.var(arr))""

                  OUTPUT: 8.0

        ->STANDARD DEVIATION:

            ->It is used to calculate the standard deviation of array elements.
            ->Standard deviation is square root of variance, present in average distance of data points from mean value. 
            ->SYNTAX:np.std(arr) #arr means collection name
            ->EXAMPLE:
                ""arr=np.array([2,4,6,8,10])
                  print(np.std(arr))""

                  OUTPUT: 2.8284271247461903

    ->ARRAY WITH CONSTANT OR SCALAR:

        ->It will perform operations on each and every value present in the array with a constant
        ->EXAMPLE:
            ""arr=np.array([2,4,6,8,10])
            print(arr+2)
            print(arr*2)
            print(arr-2)
            print(arr/2)
            print(arr//2)
            print(arr%2)

            OUTPUT: [ 4  6  8 10 12]
                    [ 4  8 12 16 20]
                    [0 2 4 6 8]
                    [1. 2. 3. 4. 5.]
                    [1 2 3 4 5]
                    [0 0 0 0 0]

27/05/2026:

    ->ARRAY WITH ARRAY OPERATION:

        ->To perform array with array operation the length of the arrays should be same 
        NOTE: There are multiple operations that user can perform within two or more that two arrays only when the length of the arrays are same.

        ->ARITHMETIC OPERATION:

            ->Arithmetic  operations in numpy arrays allow as to perform fast mathematical calculations on entire dataset without using any loop

        ->RELATIONAL OPERATOR:

            ->Relational operators are used to compare array elements and returns a boolean result.

        ->BITWISE OPERATOR:

            ->Bitwise operator in numpy are used to work on binary level of numbers, allowing user to compine, compare and modify integer values.

                                            --------
                                           | PANDAS |
                                            --------

->What is Pandas ?

    ->Pandas is a python library that used for data manipulation, data filtering and data Analysis.
    ->It provides powerful, Expressive data structures to work with structured data.  

->Why we should use pandas?

    ->data manipulation.
    ->data filtering.
    ->data analysis.  

->DATA CLEANING:

    ->It is a process of removing unwanted data from a dataset .

->DATA STRUCTURES IN PANDAS:

    ->In pandas their are two data Structures:
        ->SERIES:
            ->It is 1D (One Dimensional) data which is looking like a single spreadsheet column having index level. 
        ->DATAFRAME:  
            ->It is 2D (Two Dimensional) data structure which is looking like a full spread sheet having rows and columns.  

->SERIES

    ->CREATION OF SERIES:

        ->BY USING PANDAS:

            ->EXAMPLE:
                import pandas as pd
                s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
                s

                OUTPUT:
                a    1
                b    2
                c    3
                d    4
                e    5
                dtype: int64

            (OR)

            ->EXAMPLE:
                s = pd.Series([1,2,3,4,5])
                s

                OUTPUT:
                0    1
                1    2
                2    3
                3    4
                4    5
                dtype: int64

            (OR)

            ->EXAMPLE:

                import pandas as pd
                mock = pd.Series(['1','1*','2','2*'],index=['Sreeleela','DEepthi Sunaina','Samantha','Anupama Parameswaran'],name='Actresses')
                mock

                OUTPUT:

                Sreeleela                1
                DEepthi Sunaina         1*
                Samantha                 2
                Anupama Parameswaran    2*
                Name: Actresses, dtype: str

        ->BY USING NUMPY ARRAY:

            ->EXAMPLE:

                import pandas as pd
                import numpy as np
                arr = np.array([1,2,3,4,5])
                se = pd.Series(arr)
                se

                OUTPUT:

                import numpy as np
                arr = np.array([1,2,3,4,5])
                se = pd.Series(arr)
                print(se)

        ->BY USING DICTIONARY:

            ->EXAMPLE:
                data = {'Biriyani':100,'Chicken':150,'Mutton':200}
                s = pd.Series(data,name='Price of food')
                print(s)

                OUTPUT:

                Biriyani    100
                Chicken     150
                Mutton      200
                Name: Price of food, dtype: int64

        ->BY USING SCALAR:

            ->EXAMPLE:
                seri = pd.Series('good',index = ['a','b','c'],name = 'greet')
                seri

                OUTPUT:

                a    good
                b    good
                c    good
                Name: greet, dtype: str

->ATTRIBUTES OF SERIES:

    ->EXAMPLE:
        s = pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
        
        #VALUES
        s.value #array([1, 2, 3, 4, 5,6])

        #INDEX
        s.index #Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='str')

        #DATATYPE:
        s.dtype #dtype = int64

        #DIMENSION
        s.ndim

        #SHAPE
        s.shape

        #SIZE
        s.size

        #NAME
        s.name

        #HEAD
        s.head() # it will give first 5 values with index if we don't pass values

        #TAIL 
        s.tail() # it will give last 5 values with index if we don't pass values

        #SAMPLE
        s.sample()

        #INFO
        s.info()

->AGGREGATION FUNCTION:

    ->EXAMPLE:
        price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
        price.sum()
        price.min()
        price.max()
        price.mean()
        price.median() # for median we need to sort the array.
        price.mode()

    ->VALUE COUNTS:
        ->it used to count how many times each unique values appears after counting it returns result in a sorted order by their frequency. 
        ->This attribute is also called as frequency counter.   

*Example:-*
```python
se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
se.value_counts()
#Output
12    2
34    2
45    1
76    1
66    1
89    1
Name: count, dtype: int64
```  
**describe()**
* It returns a statistical overview.
* For numerical data it will provide count, mean, standard deviation, min, max, etc,. 

*Example:-*
```python
se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
se.describe()
#Output
count     8.000000
mean     46.000000
std      28.660575
min      12.000000
25%      28.500000
50%      39.500000
75%      68.500000
max      89.000000
dtype: float64
```
**sort_values**  
* It is used to sort the Series by its data values, not index.
* As default it will return in ascending order.
* If user want to get in descending order we need to pass ascending = False

*Example:-*
```python
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price.sort_values()
#output
harshed     1200
Prudhvi     1250
Madhavan    3500
Sanjay      5000
Name: purchase, dtype: int64
```
```python
# descending order
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price.sort_values(ascending = False)
#Output
Sanjay      5000
Madhavan    3500
Prudhvi     1250
harshed     1200
Name: purchase, dtype: int64
```
**unique()**
* it is used to return an array of distinct values in order of first appearance.  
*Example:-*
```python
se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
se.unique()
# output
array([12, 45, 34, 76, 66, 89])
```
**nunique**
* it will give number of unique values.  
```python
se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
se.nunique()
#output
6
```
**Indexing**  
* Elements can be accessed by their positions or by their label name.

*Example:-*
```python
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price['harshed']
#output
np.int64(1200)
```
**Slicing**
* Python slice notation is same like Series slice notation(syntax).

*Example:-*
```python
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price[0:2]
#output
harshed     1200
Madhavan    3500
Name: purchase, dtype: int64
```
```python
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price[0:4:2]
#output
harshed    1200
Prudhvi    1250
Name: purchase, dtype: int64
```
## Modification 
* To modify any data inside the Series we need to follow same notation(Syntax) like list
* *Syntax* variable[index] = new Value

*Example: *
```python
price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
price['harshed'] = 3000
price
#Output 
harshed     3000
Madhavan    3500
Prudhvi     1250
Sanjay      5000
Name: purchase, dtype: int64
```
## DataFrame: 
* DataFrame is a 2D( two Dimensional) Structure that having rows and columns.
* Each and Every column is called as Series.    

**Use of DataFrame:**
* preprocessing of data
* Data cleaning
* Data Modification 
* Data Filtering

## How to create a DataFrame:  
`df = pd.DataFrame`  

**Method 1 by using Dictionary**   
***Example:-***
```python
#Program
df = pd.DataFrame({
    'Name':['Madhavan', 'Sanjay', 'Harshed', 'Prudhvi'],
    'Age':[22, 23, 21, 25],
    'City':['Ulluthurpettai', 'Kadalur', 'Kanniyakumari', 'Kalasthri']
})
df
#output

Name	        Age	City
0	Madhavan	22	Ulluthurpettai
1	Sanjay	    23	Kadalur
2	Harshed	    21	Kanniyakumari
3	Prudhvi	    25	Kalasthri
```
->BY USING LIST:

->EXAMPLE:

df2 = pd.DataFrame([['A',30,'Delhi'],['B',25,'Chennai'],['C',28,'Mumbai'],['D',22,'Kolkata']], columns=['Name','Age','location'])

OUTPUT:

.  |Name|Age| City
0	A	30	Delhi
1	B	25	Chennai
2	C	28	Mumbai
3	D	22	Kolkata

->BY USING SERIES:

->EXAMPLE:

    s1 = pd.Series(['Nobita', 'Gian', 'Sunio'])
    s2 = pd.Series([1, 67, 70])
    s3 = pd.Series(['Doraemon', 'Singing', 'Money'])
    df3 = pd.DataFrame({'Name':s1, 'Marks':s2, 'Powers':s3})
    df3

    OUTPUT:

    .   Name	Marks power
    0	Nobita	1	  Doraemon
    1	Gian	67	  Singing
    2	Sunio	70	  Money


->READING FROM AN DATASET:

    ->Based on the file type it can be excel, csv, html, Json   

    ->SYNTAX:
        ->variable = pd.read_csv()` 

    ->EXAMPLE:
        df = pd.read_csv('filelocation_csv') #for a csv file
        df = pd.read_excel('filelocation_excel') #for a excel file



STEPS INVOLVED IN EDA
SLICING
LOC AND ILOC
BOOLEAN FILTERING
STEPS INVOLVED IN DATA CLEANING
GROUPBY
CONCATENATION
JOINS
FEATURE ENGINEERING

10/06/2026:

    ->GROUP BY:

        ->It is used to group all the rows that have same values in a particular column
        ->SYNTAX:
            ->var=df.groupby('catewgorical_col')
        ->The column which is having less number of unique values is known as categorical column.
        ->Example:
            a=df.groupby('class')
'''

