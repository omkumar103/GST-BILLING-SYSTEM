print("\t                         ***************                         ")

print("\t                WELCOME TO THE PROGRAM                         ")

print("\t                         ***************                         ")

print("\tThis Program Is To Make GST BILL For Stationary Items Of Year 2020.")

print("\t                         ***************                         ")


import pymysql
#Connecting To MySQL
try:
    db=pymysql.connect(host="localhost",user="root",password="2006")
    print("Connected Successfully !! ")
except Exception as e:
    print("Connction Not Established")

#Creating Database
try:
    cr=db.cursor()
    cr.execute("create database GST;")
    print("Successfully Created !! ")
except Exception as e:
    print("Database Already exist !! ")

#Using Database
try:
    cr.execute("use GST;")
    print("Database In Use !! ")
except Exception as e:
    print("Database Does Not Exist !! ")

#Creating Table
try:
    cr.execute("create table GST_BILL_2020(\
    S_No int primary key,\
    Product_Name varchar(20),\
    Batch_No char(4),\
    Quantity int,\
    Purchase_Price int,\
    Sale_Price int,\
    GST int,\
    Discount int,\
    Profit int,\
    Final_Amount int);")
    print("Table Created !! \n ")
except Exception as e:
    print("Table Already Existed !! ")

#Inserting Values To The Table
    '''
try:
    N_1=input("Enter The First Product: ")
    B_1=input("Enter The Batch Number: ")
    CQ_1=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_1=int(input("Enter The Total Quantity: "))
    Purchase_1=CQ_1*Q_1
    print("The Purchase Price Of The Product Is: ",Purchase_1)
    Sale_1=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_1=int(input("Enter The GST For The Product: "))
    GSTCost_1=Purchase_1*GST_1//100
    DiscountAmount_1=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_1=Sale_1+DiscountAmount_1
    SP_1=ListingP_1-DiscountAmount_1
    Discount_1=ListingP_1-SP_1
    D_1=Discount_1*100/ListingP_1
    print("The Product Name Is: ",N_1)
    print("The Batch Number Of The Product Is: ",B_1)
    print("The Quantity For The Product Is: ",Q_1)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_1)
    print("The Sale Price For The Product Is: ",Sale_1)
    print("GST On The Product Is: ",GST_1)
    print("The Discount On The Product is: ",D_1)
    ProfitAmount_1=Sale_1-Purchase_1-GSTCost_1
    print("The Profit Amount On The Product Is: ",ProfitAmount_1)
    P_1=ProfitAmount_1*100//Purchase_1
    print("The Profit(%) On The Product Is: ",P_1)
    GSTonSP_1=GST_1*100//Purchase_1
    FA_1=Sale_1+GSTonSP_1-DiscountAmount_1
    print("The Final Amount Is: ",FA_1)
    data=(1,N_1,B_1,Q_1,Purchase_1,Sale_1,GST_1,D_1,P_1,FA_1)
    add_data="insert into GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("First Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_2=input("Enter The Second Product: ")
    B_2=input("Enter The Batch Number: ")
    CQ_2=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_2=int(input("Enter The Total Quantity: "))
    Purchase_2=CQ_2*Q_2
    print("The Purchase Price Of The Product Is: ",Purchase_2)
    Sale_2=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_2=int(input("Enter The GST For The Product: "))
    GSTCost_2=Purchase_2*GST_2//100
    DiscountAmount_2=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_2=Sale_2+DiscountAmount_2
    SP_2=ListingP_2-DiscountAmount_2
    Discount_2=ListingP_2-SP_2
    D_2=Discount_2*100/ListingP_2
    print("The Product Name Is: ",N_2)
    print("The Batch Number Of The Product Is: ",B_2)
    print("The Quantity For The Product Is: ",Q_2)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_2)
    print("The Sale Price For The Product Is: ",Sale_2)
    print("GST On The Product Is: ",GST_2)
    print("The Discount On The Product is: ",D_2)
    ProfitAmount_2=Sale_2-Purchase_2-GSTCost_2
    print("The Profit Amount On The Product Is: ",ProfitAmount_2)
    P_2=ProfitAmount_2*100//Purchase_2
    print("The Profit(%) On The Product Is: ",P_2)
    GSTonSP_2=GST_2*100//Purchase_2
    FA_2=Sale_2+GSTonSP_2-DiscountAmount_2
    print("The Final Amount Is: ",FA_2)
    data=(2,N_2,B_2,Q_2,Purchase_2,Sale_2,GST_2,D_2,P_2,FA_2)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Second Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_3=input("Enter The Third Product: ")
    B_3=input("Enter The Batch Number: ")
    CQ_3=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_3=int(input("Enter The Total Quantity: "))
    Purchase_3=CQ_3*Q_3
    print("The Purchase Price Of The Product Is: ",Purchase_3)
    Sale_3=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_3=int(input("Enter The GST For The Product: "))
    GSTCost_3=Purchase_3*GST_3//100
    DiscountAmount_3=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_3=Sale_3+DiscountAmount_3
    SP_3=ListingP_3-DiscountAmount_3
    Discount_3=ListingP_3-SP_3
    D_3=Discount_3*100/ListingP_3
    print("The Product Name Is: ",N_3)
    print("The Batch Number Of The Product Is: ",B_3)
    print("The Quantity For The Product Is: ",Q_3)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_3)
    print("The Sale Price For The Product Is: ",Sale_3)
    print("GST On The Product Is: ",GST_3)
    print("The Discount On The Product is: ",D_3)
    ProfitAmount_3=Sale_3-Purchase_3-GSTCost_3
    print("The Profit Amount On The Product Is: ",ProfitAmount_3)
    P_3=ProfitAmount_3*100//Purchase_3
    print("The Profit(%) On The Product Is: ",P_3)
    GSTonSP_3=GST_3*100//Purchase_3
    FA_3=Sale_3+GSTonSP_3-DiscountAmount_3
    print("The Final Amount Is: ",FA_3)
    data=(3,N_3,B_3,Q_3,Purchase_3,Sale_3,GST_3,D_3,P_3,FA_3)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Third Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_4=input("Enter The Fourth Product: ")
    B_4=input("Enter The Batch Number: ")
    CQ_4=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_4=int(input("Enter The Total Quantity: "))
    Purchase_4=CQ_4*Q_4
    print("The Purchase Price Of The Product Is: ",Purchase_4)
    Sale_4=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_4=int(input("Enter The GST For The Product: "))
    GSTCost_4=Purchase_4*GST_4//100
    DiscountAmount_4=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_4=Sale_1+DiscountAmount_4
    SP_4=ListingP_4-DiscountAmount_4
    Discount_4=ListingP_4-SP_4
    D_4=Discount_4*100/ListingP_4
    print("The Product Name Is: ",N_4)
    print("The Batch Number Of The Product Is: ",B_4)
    print("The Quantity For The Product Is: ",Q_4)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_4)
    print("The Sale Price For The Product Is: ",Sale_4)
    print("GST On The Product Is: ",GST_4)
    print("The Discount On The Product is: ",D_4)
    ProfitAmount_4=Sale_4-Purchase_4-GSTCost_4
    print("The Profit Amount On The Product Is: ",ProfitAmount_4)
    P_4=ProfitAmount_4*100//Purchase_4
    print("The Profit(%) On The Product Is: ",P_4)
    GSTonSP_4=GST_4*100//Purchase_4
    FA_4=Sale_4+GSTonSP_4-DiscountAmount_4
    print("The Final Amount Is: ",FA_4)
    data=(4,N_4,B_4,Q_4,Purchase_4,Sale_4,GST_4,D_4,P_4,FA_4)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Fourth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_5=input("Enter The Fifth Product: ")
    B_5=input("Enter The Batch Number: ")
    CQ_5=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_5=int(input("Enter The Total Quantity: "))
    Purchase_5=CQ_5*Q_5
    print("The Purchase Price Of The Product Is: ",Purchase_5)
    Sale_5=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_5=int(input("Enter The GST For The Product: "))
    GSTCost_5=Purchase_5*GST_5//100
    DiscountAmount_5=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_5=Sale_5+DiscountAmount_5
    SP_5=ListingP_5-DiscountAmount_5
    Discount_5=ListingP_5-SP_5
    D_5=Discount_5*100/ListingP_5
    print("The Product Name Is: ",N_5)
    print("The Batch Number Of The Product Is: ",B_5)
    print("The Quantity For The Product Is: ",Q_5)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_5)
    print("The Sale Price For The Product Is: ",Sale_5)
    print("GST On The Product Is: ",GST_5)
    print("The Discount On The Product is: ",D_5)
    ProfitAmount_5=Sale_5-Purchase_5-GSTCost_5
    print("The Profit Amount On The Product Is: ",ProfitAmount_5)
    P_5=ProfitAmount_5*100//Purchase_5
    print("The Profit(%) On The Product Is: ",P_5)
    GSTonSP_5=GST_5*100//Purchase_5
    FA_5=Sale_5+GSTonSP_5-DiscountAmount_5
    print("The Final Amount Is: ",FA_5)
    data=(5,N_5,B_5,Q_5,Purchase_5,Sale_5,GST_5,D_5,P_5,FA_5)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Fifth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_6=input("Enter The Sixth Product: ")
    B_6=input("Enter The Batch Number: ")
    CQ_6=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_6=int(input("Enter The Total Quantity: "))
    Purchase_6=CQ_6*Q_6
    print("The Purchase Price Of The Product Is: ",Purchase_6)
    Sale_6=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_6=int(input("Enter The GST For The Product: "))
    GSTCost_6=Purchase_6*GST_6//100
    DiscountAmount_6=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_6=Sale_6+DiscountAmount_6
    SP_6=ListingP_6-DiscountAmount_6
    Discount_6=ListingP_6-SP_6
    D_6=Discount_6*100/ListingP_6
    print("The Product Name Is: ",N_6)
    print("The Batch Number Of The Product Is: ",B_6)
    print("The Quantity For The Product Is: ",Q_6)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_6)
    print("The Sale Price For The Product Is: ",Sale_6)
    print("GST On The Product Is: ",GST_6)
    print("The Discount On The Product is: ",D_6)
    ProfitAmount_6=Sale_6-Purchase_6-GSTCost_6
    print("The Profit Amount On The Product Is: ",ProfitAmount_6)
    P_6=ProfitAmount_6*100//Purchase_6
    print("The Profit(%) On The Product Is: ",P_6)
    GSTonSP_6=GST_6*100//Purchase_6
    FA_6=Sale_6+GSTonSP_6-DiscountAmount_6
    print("The Final Amount Is: ",FA_6)
    data=(6,N_6,B_6,Q_6,Purchase_6,Sale_6,GST_6,D_6,P_6,FA_6)
    add_data="insert into GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Sixth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_7=input("Enter The Seventh Product: ")
    B_7=input("Enter The Batch Number: ")
    CQ_7=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_7=int(input("Enter The Total Quantity: "))
    Purchase_7=CQ_7*Q_7
    print("The Purchase Price Of The Product Is: ",Purchase_7)
    Sale_7=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_7=int(input("Enter The GST For The Product: "))
    GSTCost_7=Purchase_7*GST_7//100
    DiscountAmount_7=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_7=Sale_7+DiscountAmount_7
    SP_7=ListingP_7-DiscountAmount_7
    Discount_7=ListingP_7-SP_7
    D_7=Discount_7*100/ListingP_7
    print("The Product Name Is: ",N_7)
    print("The Batch Number Of The Product Is: ",B_7)
    print("The Quantity For The Product Is: ",Q_7)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_7)
    print("The Sale Price For The Product Is: ",Sale_7)
    print("GST On The Product Is: ",GST_7)
    print("The Discount On The Product is: ",D_7)
    ProfitAmount_7=Sale_7-Purchase_7-GSTCost_7
    print("The Profit Amount On The Product Is: ",ProfitAmount_7)
    P_7=ProfitAmount_7*100//Purchase_7
    print("The Profit(%) On The Product Is: ",P_7)
    GSTonSP_7=GST_7*100//Purchase_7
    FA_7=Sale_7+GSTonSP_7-DiscountAmount_7
    print("The Final Amount Is: ",FA_7)
    data=(7,N_7,B_7,Q_7,Purchase_7,Sale_7,GST_7,D_7,P_7,FA_7)
    add_data="insert into GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Seventh Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_8=input("Enter The Eighth Product: ")
    B_8=input("Enter The Batch Number: ")
    CQ_8=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_8=int(input("Enter The Total Quantity: "))
    Purchase_8=CQ_8*Q_8
    print("The Purchase Price Of The Product Is: ",Purchase_8)
    Sale_8=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_8=int(input("Enter The GST For The Product: "))
    GSTCost_8=Purchase_8*GST_8//100
    DiscountAmount_8=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_8=Sale_8+DiscountAmount_8
    SP_8=ListingP_8-DiscountAmount_8
    Discount_8=ListingP_8-SP_8
    D_8=Discount_8*100/ListingP_8
    print("The Product Name Is: ",N_8)
    print("The Batch Number Of The Product Is: ",B_8)
    print("The Quantity For The Product Is: ",Q_8)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_8)
    print("The Sale Price For The Product Is: ",Sale_8)
    print("GST On The Product Is: ",GST_8)
    print("The Discount On The Product is: ",D_8)
    ProfitAmount_8=Sale_8-Purchase_8-GSTCost_8
    print("The Profit Amount On The Product Is: ",ProfitAmount_8)
    P_8=ProfitAmount_8*100//Purchase_8
    print("The Profit(%) On The Product Is: ",P_8)
    GSTonSP_8=GST_8*100//Purchase_8
    FA_8=Sale_8+GSTonSP_8-DiscountAmount_8
    print("The Final Amount Is: ",FA_8)
    data=(8,N_8,B_8,Q_8,Purchase_8,Sale_8,GST_8,D_8,P_8,FA_8)
    add_data="insert into GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Eighth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_9=input("Enter The Ninth Product: ")
    B_9=input("Enter The Batch Number: ")
    CQ_9=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_9=int(input("Enter The Total Quantity: "))
    Purchase_9=CQ_9*Q_9
    print("The Purchase Price Of The Product Is: ",Purchase_9)
    Sale_9=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_9=int(input("Enter The GST For The Product: "))
    GSTCost_9=Purchase_9*GST_9//100
    DiscountAmount_9=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_9=Sale_9+DiscountAmount_9
    SP_9=ListingP_9-DiscountAmount_9
    Discount_9=ListingP_9-SP_9
    D_9=Discount_9*100/ListingP_9
    print("The Product Name Is: ",N_9)
    print("The Batch Number Of The Product Is: ",B_9)
    print("The Quantity For The Product Is: ",Q_9)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_9)
    print("The Sale Price For The Product Is: ",Sale_9)
    print("GST On The Product Is: ",GST_9)
    print("The Discount On The Product is: ",D_9)
    ProfitAmount_9=Sale_9-Purchase_9-GSTCost_9
    print("The Profit Amount On The Product Is: ",ProfitAmount_9)
    P_9=ProfitAmount_9*100//Purchase_9
    print("The Profit(%) On The Product Is: ",P_9)
    GSTonSP_9=GST_9*100//Purchase_9
    FA_9=Sale_9+GSTonSP_9-DiscountAmount_9
    print("The Final Amount Is: ",FA_9)
    data=(9,N_9,B_9,Q_9,Purchase_9,Sale_9,GST_9,D_9,P_9,FA_9)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Ninth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

try:
    N_10=input("Enter The Tenth Product: ")
    B_10=input("Enter The Batch Number: ")
    CQ_10=int(input("Enter The Cost(in Rs.) Per Quantity: "))
    Q_10=int(input("Enter The Total Quantity: "))
    Purchase_10=CQ_10*Q_10
    print("The Purchase Price Of The Product Is: ",Purchase_10)
    Sale_10=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
    GST_10=int(input("Enter The GST For The Product: "))
    GSTCost_10=Purchase_10*GST_10//100
    DiscountAmount_10=int(input("Enter The Discount(Amount) On The Product: "))
    ListingP_10=Sale_10+DiscountAmount_10
    SP_10=ListingP_10-DiscountAmount_10
    Discount_10=ListingP_10-SP_10
    D_10=Discount_10*100/ListingP_10
    print("The Product Name Is: ",N_10)
    print("The Batch Number Of The Product Is: ",B_10)
    print("The Quantity For The Product Is: ",Q_10)
    print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_10)
    print("The Sale Price For The Product Is: ",Sale_10)
    print("GST On The Product Is: ",GST_10)
    print("The Discount On The Product is: ",D_10)
    ProfitAmount_10=Sale_10-Purchase_10-GSTCost_10
    print("The Profit Amount On The Product Is: ",ProfitAmount_10)
    P_10=ProfitAmount_10*100//Purchase_10
    print("The Profit(%) On The Product Is: ",P_10)
    GSTonSP_10=GST_10*100//Purchase_10
    FA_10=Sale_10+GSTonSP_10-DiscountAmount_10
    print("The Final Amount Is: ",FA_10)
    data=(10,N_10,B_10,Q_10,Purchase_10,Sale_10,GST_10,D_10,P_10,FA_10)
    add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(add_data,data)
    db.commit()
    print("Tenth Data Entered Successfully !! ")
except Exception as e:
    print("The Data Could Not Be Entered")

'''
#Main Menu 
print("\t          **********MAIN MENU**********          ")
print("1.To Add Product To The Table")
print("2. To Update Product To The Table")
print("3. To Remove Product From The Table")
print("4. To Search Record From The Table")
print("5. To Show The Whole Table")
print("6. Exit")
print("\n")
choice=int(input("Enter your choice from the above menu: "))
if choice==1:
    print("          **********Adding Product To The Table**********          ")
    def Add_record():
        try:
            S_No=int(input("Enter The S.No. Of The Product: "))
            Name=input("Enter The Product Name: ")
            BatchNo=input("Enter The Batch Number: ")
            CostperQuantity=int(input("Enter The Cost(in Rs.) Per Quantity: "))
            TotalQuantity=int(input("Enter The Total Quantity: "))
            Purchase=CostperQuantity*TotalQuantity
            print("The Purchase Price Of The Product Is: ",Purchase)
            Sale=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
            GST=int(input("Enter The GST For The Product: "))
            GSTCost=Purchase*GST//100
            DiscountAmount=int(input("Enter The Discount(Amount) On The Product: "))
            ListingP=Sale+DiscountAmount
            SP=ListingP-DiscountAmount
            Discount=ListingP-SP
            D=Discount*100//ListingP
            print("The Product Name Is: ",Name)
            print("The Batch Number Of The Product Is: ",BatchNo)
            print("The Quantity For The Product Is: ",TotalQuantity)
            print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase)
            print("The Sale Price For The Product Is: ",Sale)
            print("GST On The Product Is: ",GST)
            print("The Discount On The Product is: ",D)
            ProfitAmount=Sale-Purchase-GSTCost
            print("The Profit Amount On The Product Is: ",ProfitAmount)
            P=ProfitAmount*100//Purchase
            print("The Profit(%) On The Product Is: ",P)
            GSTonSP=GST*100//Purchase
            FA=Sale+GSTonSP-DiscountAmount
            print("The Final Amount Is: ",FA)
            data=(S_No,Name,BatchNo,CostperQuantity,TotalQuantity,Sale,GST,D,P,FA)
            add_data="insert into  GST_BILL_2020 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cr.execute(add_data,data)
            db.commit()
            print("Data Entered Successfully !! ")
        except Exception as e:
            print("The Data Could Not Be Entered Easily ! ",e)
    Add_record()
elif choice==2:
    print("          **********Updating Product To The Table**********          ")
    def update_record(n):
        try:
            data="select* from GST_BILL_2020 where S_No='%s'"%n
            cr.execute(data)
            n1=cr.rowcount
            if n1!=0:
                print("Record Found And Enter New Values: ")
                Product_Name=input("Enter The Product Name: ")
                Batch_No=input("Enter The Batch Number: ")
                CostperQuantity=int(input("Enter The Cost(in Rs.) Per Quantity: "))
                Quantity=int(input("Enter The Total Quantity: "))
                Purchase_Price=CostperQuantity*Quantity
                print("The Purchase Price Of The Product Is: ",Purchase_Price)
                Sale_Price=int(input("Enter The Sale Price(in Rs.) Of The Product: "))
                GST=int(input("Enter The GST For The Product: "))
                GSTCost=Purchase_Price*GST//100
                DiscountAmount=int(input("Enter The Discount(Amount) On The Product: "))
                ListingP=Sale_Price+DiscountAmount
                SP=ListingP-DiscountAmount
                D=ListingP-SP
                Discount=D*100//ListingP
                print("The Product Name Is: ",Product_Name)
                print("The Batch Number Of The Product Is: ",Batch_No)
                print("The Quantity For The Product Is: ",Quantity)
                print("The Purchase Price(in Rs.) Of The Product Is: ",Purchase_Price)
                print("The Sale Price For The Product Is: ",Sale_Price)
                print("GST On The Product Is: ",GST)
                print("The Discount On The Product is: ",Discount)
                ProfitAmount=Sale_Price-Purchase_Price-GSTCost
                print("The Profit Amount On The Product Is: ",ProfitAmount)
                Profit=ProfitAmount*100//Purchase_Price
                print("The Profit(%) On The Product Is: ",Profit)
                GSTonSP=GST*100//Purchase_Price
                Final_Amount=Sale_Price+GSTonSP-DiscountAmount
                print("The Final Amount Is: ",Final_Amount)
                data="update GST_BILL_2020 set\
                Product_Name='%s',Batch_No='%s',Quantity='%s',Purchase_Price='%s',\
                Sale_Price='%s',GST='%s',Discount='%s',Profit='%s',Final_Amount='%s'\
                where S_No='%s'"%(Product_Name,Batch_No,Quantity,Purchase_Price,Sale_Price\
                                  ,GST,Discount,Profit,Final_Amount,n)
                cr.execute(data)
                db.commit()
                print("Data Entered Successfully !! ")
            else:
                print("Record Not Found ! ")
        except Exception as e:
            print("The Data Could Not Be Entered Easily ! ",e)
    SNo=int(input("Enter the S.No. : "))
    update_record(SNo)
            
elif choice==3:
    print("          **********Removing Product From The Table**********          ")
    def del_record(n):
        try:
            data="Delete from GST_BILL_2020 where S_No='%s' "%n
            cr.execute(data)
            n1=cr.rowcount
            if n1!=0:
                db.commit
                print("Record Deleted")
            else:
                print("Record Not Deleted")
        except Exception as e:
            print("The Value Could Not Be Deleted",e)
    SNo=int(input("Enter S.No. : ")) 
    del_record(SNo)

elif choice==4:
    print("          **********Searching In The Record**********          ")
    def search_record(SNo):
        try:
            table="Select *from GST_BILL_2020 where S_No={}".format(SNo)
            cr.execute(table)
            data=cr.fetchone()
            if data[0]==SNo:
                print("Record Found ! ",data)

            else:
                print("Record Not Found ! ")
        except Exception as e:
            print("Searching Not Done Due ! ",e)
    SNo=int(input("Enter Any S.No. To Search: "))
    search_record(SNo)
            
elif choice==5:
    print("          **********Showing The Whole Table**********          ")
    def show_table():
        try:
            table=cr.execute("select*from GST_BILL_2020; ")
            data=cr.fetchall()
            for table in data:
               print(table)
        except Exception as e:
            print("The Table Cannot Be Displayed",e)
    show_table()
elif choice==6:
    print("          **********Thank You For Serveying The Menu !! **********           ")
else:
    print("          **********Invalid Choice Is Entered !! **********          ")
    print("Please Select The Option From The Above Given Menu")
