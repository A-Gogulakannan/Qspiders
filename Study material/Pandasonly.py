'''   
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

        ->EXAMPLE:
            se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
            se.value_counts()
            
            OUTPUT:

            12    2
            34    2
            45    1
            76    1
            66    1
            89    1
            Name: count, dtype: int64

    ->DESCRIBE:

        ->It returns a statistical overview.
        ->For numerical data it will provide count, mean, standard deviation, min, max, etc,. 

        ->EXAMPLE:
            se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
            se.describe()

            OUTPUT:

            count     8.000000
            mean     46.000000
            std      28.660575
            min      12.000000
            25%      28.500000
            50%      39.500000
            75%      68.500000
            max      89.000000
            dtype: float64
            
    ->SORT_VALUES():

        ->It is used to sort the Series by its data values, not index.
        ->As default it will return in ascending order.
        ->If user want to get in descending order we need to pass ascending = False

        ->EXAMPLE:
            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price.sort_values()
            
            OUTPUT:

            harshed     1200
            Prudhvi     1250
            Madhavan    3500
            Sanjay      5000
            Name: purchase, dtype: int64

        ->EXAMPLE:(DESCENDING ORDER)
            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price.sort_values(ascending = False)
            
            OUTPUT:

            Sanjay      5000
            Madhavan    3500
            Prudhvi     1250
            harshed     1200
            Name: purchase, dtype: int64

    ->UNIQUE:
        -> it is used to return an array of distinct values in order of first appearance.  
        
        ->EXAMPLE:
            se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
            se.unique()
            
            OUTPUT:

            array([12, 45, 34, 76, 66, 89])

    ->NUNIQUE:
        ->It will give number of unique values.  

        ->EXAMPLE:
            se = pd.Series([12, 45, 34, 76, 12, 66, 34, 89])
            se.nunique()

            OUTPUT:

            6

    ->INDEXING:
        ->Elements can be accessed by their positions or by their label name.

        ->EXAMPLE:
            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price['harshed']

            OUTPUT:

            np.int64(1200)

    ->SLICING:
        ->Python slice notation is same like Series slice notation(syntax).

        ->EXAMPLE:
            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price[0:2]
            
            OUTPUT:

            harshed     1200
            Madhavan    3500
            Name: purchase, dtype: int64
            

            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price[0:4:2]

            OUTPUT:

            harshed    1200
            Prudhvi    1250
            Name: purchase, dtype: int64

    ->MODIFICATION: 
        ->To modify any data inside the Series we need to follow same notation(Syntax) like list
        ->SYNTAX:
             variable[index] = new Value
        ->EXAMPLE:
            price = pd.Series([1200, 3500, 1250, 5000],index =['harshed', 'Madhavan', 'Prudhvi', 'Sanjay'], name = 'purchase')
            price['harshed'] = 3000
            price

            OUTPUT:

            harshed     3000
            Madhavan    3500
            Prudhvi     1250
            Sanjay      5000
            Name: purchase, dtype: int64

    ->DATAFRAME:
        ->DataFrame is a 2D( two Dimensional) Structure that having rows and columns.
        ->Each and Every column is called as Series.    

        ->USE OF DATAFRAME
            ->preprocessing of data
            ->Data cleaning
            ->Data Modification 
            ->Data Filtering

        ->HOW TO CREATE A DATAFRAME:
            ->SYNTAX:
                df = pd.DataFrame()  

            ->BY USING DICTIONARY:
                ->EXAMPLE:
                    df = pd.DataFrame({
                        'Name':['Madhavan', 'Sanjay', 'Harshed', 'Prudhvi'],
                        'Age':[22, 23, 21, 25],
                        'City':['Ulluthurpettai', 'Kadalur', 'Kanniyakumari', 'Kalasthri']
                    })
                    df

                    OUTPUT:

                    Name	        Age	City
                    0	Madhavan	22	Ulluthurpettai
                    1	Sanjay	    23	Kadalur
                    2	Harshed	    21	Kanniyakumari
                    3	Prudhvi	    25	Kalasthri
                    
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

    ->CONCATENATION:
        ->It is a process of merging two or more data frames
        ->TYPES:
            ->Vertical concatenation:
                ->It will merge all the rows of the first data frame with next dataframe.
                ->In this concatenation will happen row by row.
                ->It means new rows will be added below the existing rows.
                ->SYNTAX:
                    pd.concat([df1,df2,...],axis=0)
                ->EXAMPLE:
                    data={"id":[1,2,3,4,5],"E_name":["N","S","L","P","T"],"des":["SE","DS","DA","DS","DA"]}
                    data1={"id":[101,102,103],"Dname":['SE','DS','DA']}
                    df1=pd.DataFrame(data)
                    df2=pd.DataFrame(data1)
                    pd.concat([df1,df2],axis=0)

                    OUTPUT:

                        id	E_name	des	Dname
                    0	1	N	    SE	NaN
                    1	2	S	    DS	NaN
                    2	3	L	    DA	NaN
                    3	4	P	    DS	NaN
                    4	5	T	    DA	NaN
                    0	101	NaN	    NaN	SE
                    1	102	NaN	    NaN	DS
                    2	103	NaN	    NaN	DA


            ->Horizontal concatenation:
                ->It will attach the columns side by side.
                ->It will not merge the columns even if names are same.
                ->EXAMPLE:
                    data={"id":[1,2,3,4,5],"E_name":["N","S","L","P","T"],"des":["SE","DS","DA","DS","DA"]}
                    data1={"id":[101,102,103],"Dname":['SE','DS','DA']}
                    df1=pd.DataFrame(data)
                    df2=pd.DataFrame(data1)
                    pd.concat([df1,df2],axis=1)

                    OUTPUT:

                        id	E_name	des	id	    Dname
                    0	1	    N	SE	101.0	SE
                    1	2	    S	DS	102.0	DS
                    2	3	    L	DA	103.0	DA
                    3	4	    P	DS	NaN	    NaN
                    4	5	    T	DA	NaN	    NaN

        NOTE:if both dataframes having different column names, it will return many null values. We will perform vertical concatenation only when we are having same columns in all dataframes.As vertical concatenation creates more null values when columns are different, we will go for horizontal concatenation.

        NOTE:If we are having same column names in all the data frame then go for vertical concatenation.If we are having different column names in all the data frame then go for horizontal concatenation.


->FEATURE ENGINEERING:

    ->Creating a new column.
    ->Adding a new column to existing data frame.
    ->Modifying or transforming existing column.

    ->EXAMPLE:
        df=pd.DataFrame({'sname':['akshaya','riswath','mani','arun','sunil','nandha'],'English':[100,48,70,60,90,80],"Tamil":[98,38,99,87,89,90],"Science":[78,49,49,90,99,74],"Social":[30,19,60,49,70,77]})
        df["Total"]=df["English"]+df["Tamil"]+df["Science"]+df["Social"]
        df["per"]=df["Total"]/4
        grade=[]
        for i in df["per"]:
        if i>90:
            grade.append("O")
        elif i>80:
            grade.append("A")
        elif i>70:
            grade.append("B")
        elif i>60:
            grade.append("C")
        elif i>45:
            grade.append("C-")
        else:
            grade.append("Fail")
        df["grade"]=grade

        OUTPUT:

            sname	English	Tamil  Science	Social	Total	per	    grade
        0	akshaya	    100	   98	    78	    30	  306	76.50	    B
        1	riswath	     48	   38	    49	    19	  154	38.50	 Fail
        2	mani	     70	   99	    49	    60	  278	69.50	    C
        3	arun	     60	   87	    90	    49	  286	71.50	    B
        4	sunil	     90	   89	    99	    70	  348	87.00	    A
        5	nandha	     80	   90	    74	    77	  321	80.25	    A

->PIVOT TABLE:
    ->Pivot table is used to summarize the data in table format by grouping and aggregating it.
    ->If you want to apply multiple aggregate function on multiple columns at a time.
    ->SYNTAX:
        pd.Pivot_table(values=['col1',....'coln'],index='Categorical_column', aggfunc=['fname1',....]
    ->EXAMPLE:
        df=pd.read_csv("titanic.csv")
        df.info()
        df.pivot_table(values=['sex'],index='cabin',aggfunc=["count","sum"])

->DATE RANGE:
    ->It is used to generate the dates between the given limit or specified range
    ->SYNTAX:
        ->pd.date_range(start='yyyy-mm-dd', periods=no,freq='str')
    ->Start+end
    ->Start+periods

    ->CODE MEANING:
        D-DAY
        h-HOUR
        min-MINUTE
        s-SECOND
        W-WEEKLY
        W-MON - EVERY MONDAY
        ME-MONTH END
        MS-MONTH START
        YE-YEAR END
        YS-YEAR START

->DATE TIME:
    ->pd.to_datetime(data,format='')
    ->FORMATS: '%Y-%m-%s %H:%M:%S' ->Format is optional. Use format='mixed' when date formats are different
    ->It is used to convert the string into date time format.
    ->EXAMPLE:
        data='26-06-2017 12:55:36'
        pd.to_datetime(data,format='%d-%m-%Y %H:%M:%S')

        OUTPUT:

        Timestamp('2017-06-26 12:55:36')

    ->EXAMPLE:
        df=pd.DataFrame({'Name':["GAJA","SAAD","MAHESH","REDDY"],'DOB':["2001-01-01","02/02-2002","03-03-2003","04-04-2004"]})
        df["DOB"]=pd.to_datetime(df["DOB"],format='mixed')
        df

'''